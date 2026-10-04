# STAGE 12c: VERIFIER C, FRAMEWORK ADHERENCE, VALUATION SCOPE (PHASE 3)

Run runs/kissht-2026-09-19. Company KISSHT (OnEMI Technology Solutions Ltd). Audited 04-Oct-2026.
Model claude-opus-5-5. Fresh context. No other verifier output and no maker reasoning was read
beyond the artifacts named below.

## 0. SCOPE, INPUTS, METHOD

Artifacts audited:
- outputs/blocks/B10-assembly.yaml (B10). The 10-assembly report was not opened; B10 YAML is the
  sole Stage 11 input and was audited directly.
- outputs/blocks/B11-valuation.yaml, outputs/reports/11-valuation.md (B11), outputs/expectation-ledger.md.
- outputs/blocks/B14-thesis.yaml, outputs/reports/14-thesis.md (B14), extended scope: Role 2
  decision rules and position sizing.
- Operator-approved inputs: outputs/final/fttcp-deliberation.md Section 5 (lines 119-197); the gate
  file outputs/final/fttcp-signoff-gates-2026-10-04.md Section 2 was read for the Pillar 1 basis.

Rule sources read: prompts/12-verifiers-pipeline.md (Verifier C); prompts/11-valuation-pipeline.md
(wrapper overrides); frameworks/Master_Project_Prompt_v3_6.md (v3.7) Role 1 lines 104-952, Role 2
lines 956-1191, RULES lines 1515-1531; frameworks/Section_1B_v3.3_Amendments.md; Section_1B_v3_8,
v3_9, v3_10 Amendments; Section 1B v3.11 draft (main repo, unmerged, read-only). The v3.5.1, v3.6
and v3.7 layers were checked through the chunks that carry them (no rule this run turned on text
those chunks did not carry). FTTCP v2.3 rules entered through the chunks; the FTTCP source file was
not opened.

Skill chunks read for check 15 (the skill B11 used is the main-repo copy: the kissht worktree skill
carries no A27 text, and B11 cites A27 rules from "the skill only"):
C:\Users\SUMIT SHARMA\repos\inflection-pipeline\.claude\skills\section-1b\references\ chunks 01, 02
(Pillar 2L rows), 03, 04, 05, 06, 07, 08, 09, 10, 11 (17.0-17.4), 12 (FV path lines), 15 (r table
lines), 17.

Gate 0 (B01) and Emerging Moat (B07) were audited in phase 1 (outputs/blocks/B12c.yaml: 52 and 28
rules, classification AVERAGE concur, EM 15.6-16.6 MODEST concur). Not re-run here.

Source spot checks (Verifier A owns number fidelity; these are framework-basis checks only):

| Item | Source | Result |
|---|---|---|
| AUM Rs 8,001 Cr Jun-26 | Concall_Aug_2026_Transcript [page 3] line 113; Investor_Presentation_1 | Present |
| Q1 FY27 PAT 950.77 mn | results 20260729-9867adf0 [page 5] line 211 | Present |
| GNPA 2.25% Q1 FY27; CRAR 40.2% | Concall_Aug_2026 [page 5] lines 190, 197 | Present |
| FY27 guidance "gross NPA below 2.25%" | Concall_Jun_2026 [page 9] line 298; announcement 20260528-a44af40e line 103 | Present (feeds F23) |
| Rs 1,231.98 Cr = Si Creva equity, not consolidated | AR [page 57] AOC-1: share capital 100.00 + reserves 12,219.84 mn | Confirmed (feeds F8) |
| Consolidated total equity 31-Mar-2026 Rs 13,427.84 mn (Rs 1,342.78 Cr) | AR [page 98] line 11664; AR [page 10] KPI "Net Worth 1,343"; AR [page 35] "net worth ... ₹1,343 crore" | Confirmed (feeds F4, F8) |
| Standalone parent total equity Rs 9,640.57 mn | AR [page 66] line 7517; AR [page 131] net-assets table | Confirmed |

Severity scale per prompts/12: CRITICAL (materially wrong, would change a decision) / MAJOR (wrong,
decision likely survives) / MINOR (imprecision, presentational).

## 1. HEADLINE

- CRITICAL 0. MAJOR 10. MINOR 17. Rules checked 95; passed 78; acceptance 82.1%.
- Decision concur: AVOID (B14). It rests on the Section 7 Gate 0 AVERAGE prong, which no finding
  below moves. The U/D prong that B14 also cites does not fire under Section 4F as written (F6, F9).
- Expectation Ledger and decomposition gates (rules 13, 14): PASS. No off-ledger credit. Residual
  -2.4% of the post-raise market value. No REWORK trigger from this verifier.
- Rules 7, 11, 12 (method plurality, A18 exit construction, A19 FV path): PASS.
- Destination PE: the governing Track 1 partner multiple 18.62x sits within 1x of every as-written
  reading of the cap (F1). Two operator-approved inputs depart from Section 1B as written: the
  partner-slice blended cap (F1) and the own-book P/B band (F2). Both are disclosed operator rulings.
  Both need either a framework amendment or a re-rule before /finalize sign-off.
- One open input can move the governing Track 1 by more than 1x: the capital base behind the ~34%
  partner RoE (F3). Its basis is NOT FOUND. It is graded MAJOR because it is unresolved, not shown
  wrong.
- The BOOK open item resolves now from the AR (F8). Rs 1,231.98 Cr is Si Creva's equity. The
  consolidated figure is Rs 1,342.78 Cr. The own-book base stands. The consolidated-equity row, the
  RoE path and the "+Rs 10.8/share" sensitivity do not.

## 2. VALUATION (B11) COMPLIANCE TABLES

### 2A. Growth symmetry first (Section 1B v3.10 A26; Master v3.7 Rules F-J)

| # | Rule | Result | Note / recomputed |
|---|---|---|---|
| V1 | 2C-w line present; basis declared; historical CAGR beside it | PASS | B11 §2C-w. MINOR F19: "RUN-RATE" extrapolates the Q1 QoQ growth pace (13.2% for three more quarters), not the exit-quarter level the 26.1 definition names. Definition-faithful run-rate PAT 380.32 sits 13.8% below FY27 base and 39.0% below FY28 (B11 §4D-2) |
| V2 | Base not HISTORICAL where forward evidence exists (26.1) | PASS | Base below the audited +73% AUM / +75% PAT; confirm-by rows 1-2 named |
| V3 | Margin bridge lever by lever; trailing average not the base (26.2) | PASS | §2B. MINOR F18: levers not split (finance cost, mix, credit cost bps NOT FOUND); the -48 bps net is read from the operator FY28 figure |
| V4 | No per-input shading; both readings plus separating observation (26.3) | PASS | Reading A / B on return on AUM; five override-3 entries. MINOR F20 on the fade-anchor separating observation |
| V5 | Weights keyed to trailing 4Q, period stated (26.4) | PASS | Grade C, 2 quarters, stated |
| V6 | 2D standing check answered | PASS | §2D last row |
| V7 | Catalyst credit split revenue vs Pillar 3, no double credit | PASS | 100% / 0% |
| V8 | Pillar 3 Entrepreneur Ledger line (Rule G) | PASS | B14 §3G "does not support ... because" line present |

### 2B. Pillar mechanics

| # | Rule | Result | Note / recomputed |
|---|---|---|---|
| V9 | Continuous Pillar 1 formula applied as written | FAIL (F5, MAJOR) | ~34% → 24 + 0.3 x 1.0 = 24.3x, not 24.5x. Track 1 18.47x (-0.15x) |
| V10 | FTTCP RoA/RoE verdict sole Pillar 1 authority; STAGNANT → current | PASS | T4 STAGNANT used (B10 roce_status label conflates T3/T4, MINOR F27) |
| V11 | A27.1 operating RoE in Pillar 1, surplus cash out of the denominator, worksheet complete | FAIL (F3, MAJOR) | ~34% basis NOT FOUND; "operating ROCE __% vs reported __%" field absent |
| V12 | A27.1 cash-line mechanics: face value, constant on path, outside discounts, HR Current PE ex cash | PASS | Rs 9.98/share added after each discount; FV CAGR on total |
| V13 | A27.1 surplus cash derived per definition (cash base less earmarked, encumbered, base-case spend) | FAIL (F4, MAJOR) | Cash base NOT FOUND; IPO general-purpose remainder at the parent not classified |
| V14 | Single-credit route stated | PASS | "not credited" |
| V15 | Pillar 2L band matches determination; both readings | PASS | 1.00x operator; 0.80x reading quantified. MINOR F23 |
| V16 | No growth offset on lender multiplier | PASS | |
| V17 | Pillar 3 matches injected EM/catalyst/evidence; A16 gate stated | PASS | +0x. MINOR F26 (3a qualifiers not tested on slice-own figures) |
| V18 | UA in Amendment 3 order; qualifiers evidenced | PASS | Listed 5 months fails; not applied |
| V19 | Sector cap absolute | FAIL (F1, MAJOR) | Partner slice 22.67x blend is not a cap row |
| V20 | A27.2 partner slice runs rows A-H on own figures, worksheet line | PASS | §1B.1 slice line present |
| V21 | A27.2 own-book slice earns its multiple; no round number; worksheet line | FAIL (F2, MAJOR) | P/B 0.8/1.0/1.2x not earned; no slice worksheet line |
| V22 | Both tracks carried through every FV and the card | PASS | |
| V23 | >15% divergence: conservative track sets entry | PASS | 17.9%, Track 1 |
| V24 | Range H ±7.5%, rounded 0.5x, cap-bounded | PASS | 17.0-20.0x / 21.0-22.67x |
| V25 | r worksheet line (A12A/B/C, A13) | PASS | 14 + 0.5 + 0.5 + 0.5 = 15.5%; RRM 0.76 |
| V26 | CONVERTER classification before pillar math | PASS | NON-CONVERTER, test (a) fails, not ambiguous |

### 2C. Hurdle, returns, entry, conclusion

| # | Rule | Result | Note / recomputed |
|---|---|---|---|
| V27 | HR formula; bull gated on grade C (base + 5 pp) | PASS | 2.04 / 2.30 / 2.54 reproduce; Track 1 1.79 disclosed |
| V28 | A27.3 one basis at HR (forward basis → Current PE on forward EPS) | FAIL (F11, MINOR) | Current PE 19.70x is on A21 run-rate EPS 18.25 under a FORWARD label. Forward form: 359.57 / 29.89 = 12.03x with FY28→FY31 CAGR; HR value invariant (2.04) because both forms reduce to FY31 EPS x destination / (CMP − cash) |
| V29 | Tier line and tier assignment (A4.3) | PASS | Tier A; fails Tier B quality gates |
| V30 | 4D weights match grade | PASS | 35/45/20; 19.3% / 27.8% reproduce |
| V31 | SOM cross-check | PASS | 41.4% vs 61.4% |
| V32 | Entry = operating Y3 FV / 1.25^N + cash (A18.5, A27.1) | PASS | 727.76 / 2.1773 + 9.98 = 344.2; 30% price 301.5; MoS 243.9 reproduce |
| V33 | MoS evidence row; fast-growth carve-out | PASS | 30% mixed; size not price |
| V34 | U/D = base / bear per 4F | FAIL (F6, MAJOR) | 0.80x uses the partner-exit stress, not the bear case |
| V35 | Dispersion cap | PASS | 51.5% → Medium |
| V36 | Value vs price (market-implied PENDING named), edge | PASS | |
| V37 | Step 1C PENDING; no fabricated peer multiple | PASS | |
| V38 | A21 base declared; >25% divergence stated with governing choice | PASS | -13.8% / -39.0% |
| V39 | Recognition gap resolved; posture per CLAUDE.md matrix | PASS | OPEN forward, counter-reading stated; VALUE-TRAP RISK |
| V40 | Decision line consistent with Role 2 Section 7 rules | FAIL (F12, MINOR) | WATCHLIST printed; Section 7 Gate 0 AVERAGE gives AVOID; B14 corrects |

### 2D. Input discipline and gates

| # | Rule | Result | Note |
|---|---|---|---|
| V41 | Consumption clause: missing blocks named, not recomputed | PASS | Debt Capacity, FTTCP Part B, Market-Implied NOT FOUND, named |
| V42 | Override-3 both readings on every unresolved input | PASS | Five entries; BOOK readings misframed (V43) |
| V43 | BOOK conflict readings consistent with the filed record | FAIL (F8, MAJOR) | AR resolves it |
| V44 | One improvement, one mechanism | PASS | Governance in r and promoter size cap are separate framework channels |
| V45 | Signal Gate (wrapper override 5; prompts/12 rule 6) | FAIL (F7, MAJOR) | No catalyst cites a candidate; no MODERATE cap applied |
| V46 | Chunk citations beside rows (override 16) | PASS | |

### 2E. Rules 7, 11, 12

| # | Rule | Result |
|---|---|---|
| V47 | Rule 7: Section 1A matrix + ≥2 methods or justified single-method exception | PASS (matrix present; SOTP 100% with one-paragraph justification; P/E and P/B printed as cross-checks) |
| V48 | Rule 11: Year 4 committed (FY31, all cases); exit basis = entry basis (forward, stated); option calendar (none; Invincible Minds zero as narrative); dual display stated | PASS |
| V49 | Rule 12: FV path table (governing Track 1, base), FV CAGR line 21.2%, label COMPOUNDER with decomposition, FV-step lines (none), label on card | PASS. FV CAGR reproduces: (737.74 / 414.02)^(1/3) − 1 = 21.2%. MINOR F25: the "today" row is the 31-Mar-2027 valuation date |

Valuation: 49 rules, 39 PASS, 10 FAIL (8 MAJOR: F1-F8; 2 MINOR: F11, F12).

## 3. EXPECTATION LEDGER AND DECOMPOSITION GATES (rules 13, 14)

| # | Check | Result |
|---|---|---|
| L1 | Ledger exists in Appendix A schema | PASS |
| L2 | ≥1 downside row | PASS (D1 -65.09 at 0.70; D2 -112.14 at 0.15) |
| L3 | Every row has confirm-by | PASS (D3, W1 included) |
| L4 | Every row has metric and threshold | PASS |
| L5 | Probabilities in [0, 1] | PASS on credited rows. MINOR F21: D3, W1 carry "n/a" |
| L6 | Tier matches p (≥0.50 T2) | PASS (rows 1, 2 T2; row 3 T3; downsides netted into T2 as in the v3.9 Appendix B worked case) |
| L7 | Status values valid | PASS (OPEN; annotated "watch, uncredited" on D3, W1, MINOR F21) |
| L8 | No credit off-ledger (14a) | PASS. Every decomposition credit is a ledger row. Base rows reconcile: 380.32 + 205.29 + 102.48 − 65.09 = 623.00 |
| L9 | Residual starter cap (14b) | PASS. Residual -2.4% (-0.4% at CMP x diluted shares); verdict AVOID, size none |

Arithmetic reproduced: T1 6,061.43; effective multiple 2,567.40 / 242.68 = 10.579; T2 142.81 x 10.579
= 1,510.8; T3 162.9; residual -180.1.

## 4. ROLE 2 (B14) DECISION RULES AND POSITION SIZING

| # | Rule (Master Role 2 §7 and RULES) | Result | Note |
|---|---|---|---|
| R1 | Verdict per Section 7 as written | PASS | Gate 0 AVERAGE (55/160, Core 51) → AVOID |
| R2 | AVOID trigger list accurate | FAIL (F9, MAJOR) | U/D prong cited at 0.80x; does not fire under 4F |
| R3 | Rule conflict (RULES "Gate 0 below 60 → default WATCHLIST") surfaced; hardest wins | PASS | Specific Section 7 rule over a default; flagged for operator |
| R4 | INSUFFICIENT CONVICTION not used as AVOID substitute | PASS | |
| R5 | Entry conjunction stated in the verdict box | PASS | |
| R6 | Size tier walk (CO / Large / Medium / Small) | PASS | |
| R7 | Promoter cap binds (Part 2.6 Small ceiling) | PASS | |
| R8 | Dispersion cap | PASS | 51.5% → Medium; Small tighter |
| R9 | A25 fast-growth ladder: starter test, add, trim, residual cap | PASS | T1 + T2 100.2%, residual -2.4%; add blocked by ceiling |
| R10 | YAML position_size consistent with verdict | FAIL (F10, MAJOR) | "Small" against AVOID and card "None now" |
| R11 | Section 5 fields complete (5-year FV) | FAIL (F13, MINOR) | NOT COMPUTED; Year-4 FV Rs 875.3 given, reproduces |
| R12 | Section 5 carries A19 FV CAGR and label | PASS | |
| R13 | 3x3 matrix counts | PASS | 5/9 ≥25%, 7/9 ≥15% reproduce |
| R14 | Rule F: ≥5 chains, each with [INFERENCE], four questions, PENDING LIVE VERIFICATION marks | PASS | 7 chains |
| R15 | Rule G: ledger filled, Pillar 3 line, cap not lifted | PASS | |
| R16 | Rule I: "success catalogue pending" stated | PASS | §7 transition filter |
| R17 | Rule H readiness block | PASS | |
| R18 | Cross-reference table; hardest verdict wins | PASS | |
| R19 | Re-open path framework-consistent | FAIL (F14, MINOR) | Posture condition (VALUE-TRAP RISK) carried as an aside, not a condition |
| R20 | Monitoring checklist measurable | PASS | |
| R21 | Thesis-broken specific and measurable | PASS | |
| R22 | Tier A / B assignment | PASS | |

Role 2: 22 rules, 18 PASS, 4 FAIL (2 MAJOR, 2 MINOR).

## 5. SKILL-TO-SOURCE FIDELITY (check 15)

| # | Chunk | Source compared | Result |
|---|---|---|---|
| C1 | 01 Pillar 1, A27.1 | Master §1B Pillar 1 lines 278-309; v3.11 27.1 and Interaction bullet 1 | PASS |
| C2 | 02 Pillar 2L rows | Master lines 351-365; v3.3 A7 | PASS |
| C3 | 03 Pillar 3 | v3.3 A4.1, A4.2; Master line 371 (A16) | PASS |
| C4 | 04 single credit, A27.2 | v3.11 27.2 | PASS |
| C5 | 05 cap table, A27.4, R1 pending | Master cap table lines 418-448; v3.11 27.4; v3.9 App C R1 | PASS |
| C6a | 06 HR EPS CAGR basis | v3.11 Interaction "Amendments 21 to 24" | FAIL (F15, MINOR) |
| C6b | 06 entry table exponent | v3.8 18.5; v3.11 27.1 | FAIL (F16, MINOR) |
| C7 | 07 revenue basis, bridge, fade | v3.10 26.1-26.3; Master 2A/2B | PASS |
| C8 | 08 A21/A24/A25 | v3.9 A25 line 126; Master line 1163 | FAIL (F17, MINOR) |
| C9 | 09 A22/A23 ledger | v3.9 A22, A23, App A | PASS |
| C10 | 10 A18 | v3.8 A18; v3.11 27.3 | PASS |
| C11 | 11 A17 gate | v3.7 A17 via chunk text | PASS |
| C12 | 12 A19 path lines | v3.8 19.0-19.1; v3.11 27.1 | PASS |
| C13 | 15 r table lines | v3.6 A12, A13; Master lines 559-562 | PASS |
| C14 | 17 worksheet, Rule E | v3.10 26.4; Master 4D | PASS |

Chunk fidelity: 15 checks (06 counted twice), 12 PASS, 3 FAIL. No chunk divergence changes a B11
value. B11's statement "No chunk disagreed with a source file on a point this run needed" holds in
effect, not in letter (F15).

## 6. FINDINGS

### MAJOR

**F1. Partner-slice cap 22.67x is not a Section 1B cap row.** Location: B11 §1B.1 row G;
B11.pillar_detail.sector_cap_used 22.67; deliberation override 3.
- Rule: Master §1B Sector Reality Cap ("The destination PE CANNOT exceed the sector cap"; the
  Category-Break Override "is the ONLY mechanism by which it can be raised", lines 416, 454); v3.11
  27.2 ("then the slice's own sector cap row"); chunk 05 line 67 ("Until ruled, classify to an
  existing row and state the classification"). CLAUDE.md NEVER: no exit PE from outside Section 1B.
- Text: the blend 1/3 x 18x + 2/3 x 25x is not a row. No "asset-light services" row exists; the 25x
  rows nearest in kind are Logistics (asset-light) and Consulting / Engineering services (gate file
  §2 line 93). The SOTP blended cap in chunk 05 line 75 is reserved for hybrid annuity-EPC.
- Operator-ruled and disclosed by B11 ("Section 1B has no blended-row mechanism"). Not a Stage 11
  error. Reported for an operator ruling or a framework amendment (a cap row for DLG-platform fee
  businesses).
- Recomputed, two as-written readings:
  - Banks / NBFCs / MFIs 18x row: Track 2 18.0x (-4.67x), Track 1 min(18.62, 18.0) = 18.0x
    (-0.62x), divergence 0%. Track 1 today Rs 404.0 [(2,156.64 + 18 x 336.42 + 208.05) / 20.8416];
    Year-3 Rs 718.4 [(3,054.97 + 18 x 650.52 + 208.05) / 20.8416]; entry Rs 335.3; FV CAGR 21.2%
    COMPOUNDER. Midpoint today Rs 429.9; Track 2 today Rs 455.8. Prob-weighted HR about 1.84
    [2.738 x (3.523 + 0.54 x 18) / 19.70], below 1.953; bull (base + 5 pp) 2.29 → band CONDITIONAL on
    B11's prob-weighted convention (base-point HR 2.07 still PASS).
  - A single 25x row: Track 2 min(24.5, 25) = 24.5x; Track 1 18.62x unchanged.
- Severity: the governing Track 1 moves 0 to 0.62x under either reading (within tolerance) → MAJOR.
  Under rule 5 this escalates to CRITICAL if the operator assigns the 18x row, because the HR band
  flips PASS → CONDITIONAL. The decision (AVOID) does not move; the HR caps nothing (OR-2).

**F2. Own-book P/B band 0.8x / 1.0x / 1.2x is not earned under A27.2.** Location: B11 §1B.2;
B11.destination_pe.own_book_pb_approved; deliberation §5 Slice 1.
- Rule: v3.11 27.2 ("No slice carries a round number"; each slice runs its own derivation; "The
  worksheet states each slice's pillar rows"); Master Pillar 2L line 363 and §3 P/B line 770
  (lender: theoretical P/B = ROE ÷ CoE is primary).
- Text: the band is an operator choice. B11 printed the theoretical P/B (0.65x-0.87x at r 15.5%;
  0.72x-0.96x at 14%) and the slice PE-equivalent, then kept the band ("Reported, not changed"). No
  A27.2 slice worksheet line exists for the own book. The pairing 0.8x ↔ Track 1, 1.2x ↔ Track 2 has
  no Section 1B basis (B11 notes "Section 1B has no RRM track for a P/B slice").
- Recomputed on the earned lender reading (P/B = own-book RoE ÷ r, FY28 RoE 10.1% at Mar-27, FY31
  RoE 13.5% at Mar-30, per B11 §1B.2): Track 1 today 0.65x → Rs 394.6 (-19.4); Track 2 today 0.72x →
  Rs 469.0 (-62.1); Track 1 Year-3 0.871x → Rs 750.7 (+13.0); FV CAGR 23.9% COMPOUNDER; chunk-06
  entry Rs 350.2; HR at the midpoint about 2.00, still PASS.
- The three-pillar PE reading (12.5x Track 2 / 9.5x Track 1 on own PAT) values a sub-CoE book above
  book (12.5 x 10% = 1.25x implied P/B) and contradicts the lender P/B-primary rule; it is not the
  as-written answer for a lender slice.
- Severity MAJOR: values move within tolerance; decision unchanged. Operator ruling requested on
  how A27.2 applies to a lender P/B slice.

**F3. A27.1 operating RoE for the partner slice: basis NOT FOUND, strip not tested.** Location:
B11 §1B.0 A27.1 line and §1B.1 row A; B11.pillar_detail.roce_used 34.0.
- Rule: v3.11 27.1 rule 1 ("Pillar 1 uses OPERATING ROCE. Surplus cash is excluded from capital
  employed") and its worksheet line field "operating ROCE ___% vs reported ___%"; chunk 01 line 29.
- Text: the gate file §2 line 77 records "Pillar 1 on parent RoE of about 34%: basis NOT FOUND ...
  The operator names the basis for 34%." The deliberation does not name it. B11's A27.1 line omits
  the operating-vs-reported field and does not test whether the Rs 208.05 Cr surplus cash (which it
  adds at face) also sits in the ~34% denominator.
- Sensitivity [INFERENCE, labelled reading, not a fill]: parent equity outside Si Creva at Mar-27 is
  Rs 728.2 Cr [3,424.0 − 2,695.8, both B10/B11]; partner FY27 PAT 238.14 / 728.2 = 32.7%, close to
  ~34%, which is consistent with (not proof of) the cash sitting in the denominator. Ex the 208.05:
  238.14 / 520.2 = 45.8% → Pillar 1 27.8x → Track 1 21.2x (+2.5x), Track 2 still 22.67x, divergence
  6.7%; Track 1 today about Rs 455; Year-3 about Rs 817; chunk-06 entry about Rs 381, above CMP.
- B11 did show a second reading (FY26 84.4% → Track 1 22.67x, today Rs 479.3) with a reason but no
  separating observation.
- Severity MAJOR because the basis is unresolved, not shown wrong. If the operator names a basis
  with surplus cash inside the denominator, the governing Track 1 moves by more than 1x and the
  finding becomes CRITICAL under rule 5. Separating observation: the operator's named capital base
  for the ~34% figure, before /finalize sign-off.

**F4. A27.1 surplus cash not derived per definition; parent-held IPO remainder unclassified.**
Location: B11 §1B.0 A27.1 line ("cash and liquid investments: NOT FOUND in B10"); B10.net_cash_surplus_cr.
- Rule: v3.11 27.1 "Surplus cash" definition (cash, bank and liquid investments LESS earmarked
  proceeds, encumbered cash, base-case spend; "Each deduction carries its filing anchor").
- Text: the Rs 208.05 Cr line is the raise's 25% general-purpose slice only (operator figure). From
  the AR: consolidated equity 31-Mar-2026 Rs 1,342.78 Cr (AR [page 98] line 11664) against Si Creva
  equity Rs 1,231.98 Cr (AR [page 57] AOC-1). B11's own Jun-26 gap of Rs 282.0 Cr splits into
  Rs 110.8 Cr of FY26 equity outside Si Creva and Rs 171.2 Cr consistent with IPO net proceeds kept at
  the parent [INFERENCE: deck-implied Jun-26 equity 2,245.9 − 1,342.78 − Q1 PAT 95.08 = 808.0 Cr net
  IPO inflow, of which 636.8 went to Si Creva]. That Rs 171.2 Cr is not classified as surplus,
  encumbered (FLDG deposit) or spent. B14 §3G records that its use "was described two ways on the Q4
  call".
- Effect if surplus: +Rs 8.2/share on every fair value and entry line, and its after-tax treasury
  income must leave EPS (A27.1). Within tolerance → MAJOR. Operator figure governs until ruled.

**F5. Pillar 1 24.5x does not follow the formula at the stated ~34%.** Location: B11 §1B.1 row A;
deliberation §5 Slice 2.
- Rule: Master line 283; v3.6 A11 (Base PE = 24 + 0.3 x (ROE − 33)).
- 24 + 0.3 x (34 − 33) = 24.3x. 24.5x implies RoE 34.67%. B11 reported it (divergence 1) and kept
  the approved figure.
- Recomputed: Track 1 24.3 x 0.76 = 18.47x (-0.15x); today Rs 411.6 (-2.4); Year-3 Rs 733.0 (-4.7);
  entry Rs 342.0. Track 2 unchanged (cap binds). MAJOR under rule 5 (value change within tolerance).

**F6. Upside/downside built on a stress case, not the 4F bear case.** Location: B11 §4F;
B11.upside_downside_ratio 0.8; verdict card.
- Rule: Master §4F line 882 "Upside (base) / Downside (bear) ratio" at Year 3; chunk 06 line 99.
- Text: B11 divides base today-value upside (Rs 414.0, +12.0%) by the partner-exit stress (Rs 313.8,
  -15.1%). Partner exit is a ledger downside row (D2, p 0.15), not the bear case. The lens also
  compares a 31-Mar-2027 value with a 04-Oct-2026 price.
- Recomputed: Year 3 as written: bear Track 1 Rs 519.5 is above CMP → no downside → ratio not
  meaningful, ≥2x satisfied. Valuation-date lens with the bear case: 44.45 / 15.55 = 2.9x (B11's own
  figure), ≥2x. The U/D AVOID prong does not fire. MAJOR (feeds F9; decision survives on Gate 0).

**F7. Signal Gate not applied.** Location: B11 §4D-3 ledger rows 1-3; outputs/expectation-ledger.md;
B10 (no downstream_candidates field).
- Rule: prompts/11 override 5 ("every Step 2 forward catalyst must cite a downstream candidate from
  B10 ... A catalyst with no candidate anchor is graded evidence-thin and its magnitude caps at
  MODERATE"); prompts/12 rule 6. B09 carries six candidates (B09-tam.yaml lines 58-94), so the block
  exists; B10 did not carry it and B11 did not flag the gap.
- Candidates that apply: row 2 (partner originations) → "Off-book lending partner banks/NBFCs";
  row 3 (credit cost, proof gate) → "CRIF High Mark / TransUnion CIBIL ... delinquency" and "RBI Master
  Directions on Digital Lending". Citing them, marked (candidate, unverified), clears the gate with no
  value change.
- If capped instead: row 1 p 0.70 → 0.60. T2 1,293.6 Cr (17.1%); residual +0.5%; STARTER test still
  met; prob-weighted FY28 PAT 518.0; HR about 1.97 [proportional roll], still PASS by a small margin.
- MAJOR.

**F8. BOOK conflict misframed; the AR resolves it.** Location: B11 §3.3 FLAG-BOOK-BASE-CONFLICT;
§2C rows "Consolidated equity (SOTP roll)", BVPS, RoE, AUM/equity; key-assumption line "▲/▼ Book-base
conflict: up to +Rs 10.8 per share"; B11/B14 open item BOOK.
- Rule: override 3 (both readings must be real readings of the evidence); Master §2C BVPS and ROE rows.
- Text: reading (a) "1,231.98 is the consolidated FY26 net worth" is contradicted by the AR. Rs 1,231.98
  Cr is Si Creva's equity (AR [page 57] AOC-1: 100.00 + 12,219.84 mn). Consolidated total equity is
  Rs 1,342.78 Cr (AR [page 98] line 11664; KPI "Net Worth 1,343", AR [page 10]). Reading (b) "own book
  understated by up to Rs 282 Cr" is also misframed: the extra equity sits at the parent (partner-slice
  capital and possible surplus cash, F4), not in Si Creva.
- Consequences: the own-book base Rs 2,695.8 Cr (Si Creva roll) stands. The +Rs 10.8/share sensitivity
  is void. Consolidated Mar-27 equity is the BVPS route Rs 3,424.0 Cr (Rs 164.3/share). The B11 2C
  consolidated row understates equity by Rs 282 Cr and overstates the whole-company RoE path: FY28
  16.7% [623 / avg(3,424.0, 4,047.0)] not 18.0%; FY30 18.7% not 19.8%. The 2D "RoE >15%" and 4G
  "FY30 ≥17%" checks still pass.
- Related: B10.bvps_fy26_rs 131.33 divides Si Creva equity by OnEMI shares (MINOR F24; route to
  Verifier A as an unlabelled basis).
- MAJOR (wrong values; SOTP and decision unaffected). The BOOK open item can close on this extraction.

**F9. B14 cites the U/D prong as an AVOID trigger and sets a non-framework re-open price.** Location:
B14 verdict card "Triggers fired ... Upside/Downside 0.80x < 2x"; §7 decision table AVOID row; §7 FLAG
re-open path "price at or below Rs 347.2, so U/D >= 2x on the headline lens"; Narrative para 4.
- Rule: Master §7 line 1129 reads the U/D ratio of §4F (base / bear). Per F6 that ratio passes.
- Recomputed: AVOID fires on Gate 0 AVERAGE alone. Strike "U/D 0.80x" from the trigger list and the
  Rs 347.2 condition from the re-open path. The re-open path reads: Gate 0 lender-variant ruling or
  re-score; Q2 FY27 T3 STARTING; no thesis-broken trigger; price inside the zone (≤ ~Rs 350);
  posture condition per F14. MAJOR (decision survives).

**F10. B14 YAML position_size "Small" contradicts the AVOID verdict.** Location: B14-thesis.yaml line 8;
14-thesis.md YAML line 674.
- Rule: Master §7 position rules ("Small (2-3%): Everything else that qualifies as BUY"). The B14 card
  says "Position Size: None now" and the size walk says "The current verdict (AVOID) means zero".
- The machine field read by /finalize and the Notion payload carries a size the verdict forbids.
  Recomputed: position_size "None (AVOID); ceiling Small if re-opened". MAJOR.

### MINOR

- F11 (V28). A27.3 basis line: Current PE 19.70x on A21 run-rate EPS under a FORWARD label (B11 §4D-4).
  Forward form 12.03x on FY28 EPS with FY28→FY31 CAGR. HR value unchanged at 2.04.
- F12 (V40). B11 decision "WATCHLIST" (B11 §4H, YAML decision) does not apply Section 7: Gate 0
  AVERAGE → AVOID. B14 corrects; the hardest verdict governs.
- F13 (R11). B14 §5 Base and Bull 5-year FV "NOT COMPUTED". Year-4 Rs 875.3 reproduces
  [(0.8 x 4,372.9 + 18.62 x 0.54 x 1,445.6 + 208.05) / 20.8416]. A Year-5 value needs FY33 PAT,
  which B11 did not project (18.0 needs Year 4 only).
- F14 (R19). B14 §7 re-open path carries the VALUE-TRAP RISK posture as "would also", not as a
  condition. CLAUDE.md matrix: "DEEP WATCH or AVOID unless the classification is disproven". Add:
  STRUCTURAL classification disproven (ugliness ruled ARTIFACT) or proof gate fired.
- F15 (C6a). Chunk 06 line 39 keys HR EPS CAGR to the A21 run-rate base and omits the v3.11
  Interaction sentence "The A21 run-rate base and the A22 probability-weighted EPS CAGR run on the
  27.3 basis" (Section_1B_v3_11_Amendments.md line 114). Chunk 10 line 60 carries the 27.3 rule.
  B11 followed chunk 06 (F11). No B11 value changes. Operator fix to chunk 06.
- F16 (C6b). Chunk 06 line 89 "Price for the tier hurdle = Fair Value ÷ (1 + hurdle)³" against
  chunk 06 line 82 and v3.8 18.5 / v3.11 27.1 "^N". Master §4E line 867 carries the same "³".
  B11 used ^N (3.487). No value change. Operator fix to chunk 06 and the Master 4E row.
- F17 (C8). Chunk 08 line 38 reads fast-growth "OR FTTCP Revenue Transition = ACCELERATING" without
  the OR-12 reading (FIRING) that v3.9 line 126 and Master line 1163 carry. B11 used the run-rate
  leg. No value change.
- F18 (V3). Margin bridge levers not split: finance cost / mix / credit cost bps NOT FOUND; net
  -48 bps read from the operator FY28 figure. Honest NOT FOUND; no lever invented.
- F19 (V1). "RUN-RATE" label extrapolates the exit-quarter growth pace, not the exit-quarter level
  (26.1 definition). Definition-faithful run-rate PAT Rs 380.32 Cr; the base path is the operator's.
- F20 (V4). Fade anchor (20% TAM vs 46.9% SAM): the separating observation "FY28 AUM growth vs 35%"
  tests the operator's FY28 step, not the FY29-FY30 anchor. A separating observation is FY29 AUM
  growth vs 27.5% (31-May-2029) or a digital-lender segment growth print.
- F21 (L5, L7). Ledger rows D3 and W1 carry probability "n/a" and status "OPEN (watch, uncredited)".
  Both are uncredited; schema-valid only on the OPEN reading.
- F22. Rule F chain 7 (RBI inspection years; IR reply, review 30-Nov-2026) has no ledger row. Master
  Rule F: every confirm-by line feeds the ledger. Uncredited, so no 14(a) breach.
- F23 (V15). Pillar 2L second reading omits a datapoint: Q1 FY27 GNPA 2.25% sits at, not below, the
  FY27 target "gross NPA below 2.25%" (Concall_Jun_2026 [page 9] line 298; announcement 20260528
  line 103). It strengthens the 0.80x reading. Separating observation unchanged (Q2 FY27 T3 test).
- F24. B10.bvps_fy26_rs 131.33 = Si Creva equity 1,231.98 / OnEMI paid-up shares 9.3769 Cr: an
  entity-basis mismatch. Consolidated FY26 BVPS on 1,342.78 Cr is Rs 143.2. Route to Verifier A.
- F25 (V49). The A19 "today" row is the 31-Mar-2027 valuation date, 0.487 years forward of the run
  date. FV CAGR runs 3.0 years from that point. Defensible under the operator-approved forward
  valuation date; state it on the card.
- F26 (V17). Partner-slice Pillar 3a: B11 counts one qualifier (SOM ≥20%) without the capacity
  cross-check and does not address B07's capex-embedded growth (57.8%; phase-1 recompute 21.9-29.2%).
  Under 27.2 slice-own figures, the capex-embedded figure belongs to the own book (75% of issue money
  went to Si Creva), so +0x stands. State the exclusion.
- F27 (B10). B10 omits B09.downstream_candidates (F7 root), the Debt Capacity, FTTCP Part B and
  Market-Implied blocks (named by B11), and labels roce_status "STAGNANT (overridden to STARTING +1
  for T3 asset quality)", which conflates T4 RoA/RoE with T3 asset quality.

## 7. RECOMPUTED VALUES

- Destination PE: not concur on two operator-approved inputs; governing track concur within 1x.
  - Partner slice, as written: Track 2 18.0x (Banks / NBFCs / MFIs row) or 24.5x (one 25x row) vs
    22.67x; Track 1 18.0x-18.62x vs 18.62x; formula Pillar 1 24.3x not 24.5x (Track 1 18.47x).
  - Own book, earned lender P/B: 0.65x (Track 1, r 15.5%) / 0.72x (r 14%) at Mar-27 vs 0.8x / 1.2x.
- Decision: concur AVOID, on the Gate 0 AVERAGE prong only.

## 8. OPERATOR RULINGS REQUESTED

1. Partner-slice cap: assign one existing row (18x Banks / NBFCs / MFIs, or a named 25x row) or
   amend Section 1B with a DLG-platform fee row (F1).
2. Own-book slice under A27.2: earned P/B (ROE ÷ r) per track, or the three-pillar PE (F2).
3. Name the capital base of the ~34% partner RoE; state whether surplus cash sits in it (F3).
4. Classify the ~Rs 171 Cr IPO remainder at the parent under A27.1 (F4).
5. Close the BOOK open item on the AR figures in F8.

## 9. YAML

```yaml
stage: B12c
company: "KISSHT"
run_date: "2026-09-19"
model: "claude-opus-5-5"
status: complete
scope: "phase 3 valuation: B10, B11, expectation ledger, B14 (extended: Role 2 decision rules and sizing); Gate 0 and Emerging Moat audited in phase 1 (outputs/blocks/B12c.yaml), not re-run"
gate0: {rules_checked: 0, fails: [], note: "phase-1 audit carried (52 rules; AVERAGE concur; B12c.yaml)"}
emoat: {rules_checked: 0, fails: [], note: "phase-1 audit carried (28 rules; EM 15.6-16.6 MODEST concur; B12c.yaml)"}
valuation: {rules_checked: 49, fails: ["V9 Pillar 1 formula 24.3x not 24.5x (F5 MAJOR)", "V11 A27.1 operating RoE basis NOT FOUND, strip untested (F3 MAJOR)", "V13 A27.1 surplus cash not derived; parent-held IPO remainder unclassified (F4 MAJOR)", "V19 partner-slice cap 22.67x blend is not a cap row (F1 MAJOR, operator-ruled)", "V21 own-book P/B 0.8/1.0/1.2x not earned under A27.2 (F2 MAJOR, operator-ruled)", "V28 A27.3 Current PE on run-rate EPS under FORWARD label (F11 MINOR)", "V34 U/D on partner-exit stress not 4F bear (F6 MAJOR)", "V40 decision WATCHLIST vs Section 7 AVOID (F12 MINOR)", "V43 BOOK readings misframed; AR resolves (F8 MAJOR)", "V45 Signal Gate not applied (F7 MAJOR)"]}
role2_decision_sizing: {rules_checked: 22, fails: ["R2 AVOID trigger list cites U/D 0.80x (F9 MAJOR)", "R10 YAML position_size Small vs AVOID (F10 MAJOR)", "R11 5-year FV NOT COMPUTED (F13 MINOR)", "R19 re-open path omits posture condition (F14 MINOR)"]}
skill_source_fidelity: {rules_checked: 15, chunks_read: ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "15", "17"], skill_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/skills/section-1b/references/", fails: ["chunk 06 line 39 omits v3.11 Interaction: A21 base and A22 CAGR run on the 27.3 basis (F15 MINOR)", "chunk 06 line 89 exponent cubed vs ^N in 18.5/27.1 (F16 MINOR)", "chunk 08 line 38 omits OR-12 FIRING reading (F17 MINOR)"]}
expectation_ledger: {present: true, downside_row: true, all_rows_confirm_by: true, all_rows_metric_threshold: true, prob_in_range: true, decay_status_valid: true, off_ledger_credit: false, residual_pct_cmp: -2.4, residual_starter_cap_ok: true, fails: []}
business_understanding_narrative: {checked: false, note: "rule 9; stage 13 output not among this invocation's inputs; any fail = REWORK stage 13"}
recomputed_destination_pe: "Partner slice as written: Track 2 18.0x (18x row) or 24.5x (single 25x row) vs approved 22.67x blend; governing Track 1 18.0-18.62x vs 18.62x (within 1x); formula Pillar 1 24.3x (Track 1 18.47x) vs 24.5x. Own book earned P/B 0.65x (r 15.5%) / 0.72x (r 14%) at Mar-27 vs approved 0.8x / 1.2x"
recomputed_decision: ""
findings:
  - {id: F1, severity: MAJOR, location: "B11 §1B.1 row G; pillar_detail.sector_cap_used 22.67; deliberation override 3", rule: "Master §1B Sector Reality Cap and Category-Break Override; v3.11 27.2 own cap row; chunk 05 line 67", note: "1/3 x 18x + 2/3 x 25x is not a row; operator-ruled, disclosed; escalates to CRITICAL if the 18x row is assigned (prob-weighted HR PASS -> CONDITIONAL)", recomputed: "18x row: T2 18.0x, T1 18.0x, today T1 Rs 404.0, Y3 T1 Rs 718.4, entry Rs 335.3, HR pw ~1.84; 25x row: T2 24.5x, T1 18.62x"}
  - {id: F2, severity: MAJOR, location: "B11 §1B.2; destination_pe.own_book_pb_approved", rule: "v3.11 27.2 no round number, slice worksheet line; Master Pillar 2L / §3 P/B = ROE / CoE", note: "operator band not earned; no own-book slice worksheet line; 0.8x/1.2x pairing to tracks has no Section 1B basis", recomputed: "earned 0.65x/0.72x: T1 today Rs 394.6, T2 today Rs 469.0, T1 Y3 Rs 750.7, FV CAGR 23.9%, entry Rs 350.2, HR mid ~2.00"}
  - {id: F3, severity: MAJOR, location: "B11 §1B.0 A27.1 line; §1B.1 row A; pillar_detail.roce_used 34.0", rule: "v3.11 27.1 rule 1 operating ROCE; worksheet field operating vs reported", note: "~34% basis NOT FOUND (gate file §2 line 77); surplus cash inside denominator not tested; CRITICAL if basis includes surplus cash", recomputed: "reading ex Rs 208.05 Cr: 45.8% -> Pillar 1 27.8x -> T1 21.2x (+2.5x), today ~Rs 455, entry ~Rs 381"}
  - {id: F4, severity: MAJOR, location: "B11 §1B.0 A27.1 line; B10.net_cash_surplus_cr", rule: "v3.11 27.1 surplus cash definition with anchored deductions", note: "cash base NOT FOUND; ~Rs 171.2 Cr IPO net proceeds at parent unclassified [AR p.98 line 11664 vs AR p.57 AOC-1]", recomputed: "if surplus: +Rs 8.2/share on every FV and entry line; strip its treasury income from EPS"}
  - {id: F5, severity: MAJOR, location: "B11 §1B.1 row A; deliberation §5 Slice 2", rule: "Master line 283; v3.6 A11 elite formula", note: "24 + 0.3 x (34 - 33) = 24.3x; disclosed by B11", recomputed: "T1 18.47x; today Rs 411.6; Y3 Rs 733.0; entry Rs 342.0"}
  - {id: F6, severity: MAJOR, location: "B11 §4F; upside_downside_ratio 0.8; verdict card", rule: "Master §4F line 882 base / bear at Year 3; chunk 06 line 99", note: "partner-exit stress (ledger D2) used as downside; Mar-27 value vs Oct-26 price", recomputed: "Year 3: no downside (bear Rs 519.5 > CMP), n.m., >=2x; valuation-date bear lens 2.9x"}
  - {id: F7, severity: MAJOR, location: "B11 §4D-3 ledger rows 1-3; expectation-ledger.md; B10 (no downstream_candidates)", rule: "prompts/11 override 5 Signal Gate; prompts/12 rule 6", note: "no catalyst cites a B09 candidate and no MODERATE cap applied; B09 lines 58-94 hold six candidates", recomputed: "cite candidates (no change) or cap row 1 at 0.60: T2 17.1%, residual +0.5%, HR ~1.97 PASS"}
  - {id: F8, severity: MAJOR, location: "B11 §3.3 FLAG-BOOK-BASE-CONFLICT; §2C consolidated equity, BVPS, RoE rows; key assumption +Rs 10.8; open item BOOK", rule: "override 3 readings must match the filed record; Master §2C", note: "1,231.98 = Si Creva equity (AR p.57 AOC-1); consolidated 1,342.78 Cr (AR p.98 line 11664; KPI p.10 1,343); extra book sits at the parent", recomputed: "own book 2,695.8 stands; Mar-27 consolidated 3,424.0 (BVPS 164.3); RoE FY28 16.7%, FY30 18.7%; +Rs 10.8 sensitivity void; BOOK closes"}
  - {id: F9, severity: MAJOR, location: "B14 verdict card triggers; §7 AVOID row and re-open path; narrative", rule: "Master §7 line 1129 reads §4F U/D", note: "U/D prong does not fire; Rs 347.2 re-open condition is not a framework condition", recomputed: "AVOID on Gate 0 AVERAGE alone; strike U/D trigger and Rs 347.2"}
  - {id: F10, severity: MAJOR, location: "B14-thesis.yaml line 8 position_size", rule: "Master §7 position rules (Small = qualifies as BUY)", note: "machine field Small contradicts AVOID and card 'None now'", recomputed: "position_size: None (AVOID); ceiling Small if re-opened"}
  - {id: F11, severity: MINOR, location: "B11 §4D-4 hurdle basis line", rule: "v3.11 27.3 rule 1", note: "Current PE on A21 run-rate EPS under FORWARD label", recomputed: "forward form 12.03x; HR 2.04 unchanged"}
  - {id: F12, severity: MINOR, location: "B11 §4H DECISION; YAML decision", rule: "Master §7 decision rules; hardest verdict wins", note: "WATCHLIST vs Gate 0 AVERAGE AVOID rule", recomputed: "AVOID (B14)"}
  - {id: F13, severity: MINOR, location: "B14 §5 Base/Bull FV 5yr", rule: "Master Role 2 §5 template", note: "NOT COMPUTED; Year-4 Rs 875.3 reproduces", recomputed: ""}
  - {id: F14, severity: MINOR, location: "B14 §7 FLAG re-open path", rule: "CLAUDE.md transition matrix VALUE-TRAP RISK", note: "posture condition carried as aside", recomputed: "add: STRUCTURAL disproven or proof gate fired"}
  - {id: F15, severity: MINOR, location: "chunk 06 line 39", rule: "v3.11 Interaction line 114", note: "omits A21/A22 run on the 27.3 basis; chunk 10 line 60 carries it", recomputed: "no B11 value change"}
  - {id: F16, severity: MINOR, location: "chunk 06 line 89; Master §4E line 867", rule: "v3.8 18.5; v3.11 27.1 ^N", note: "cubed vs ^N", recomputed: "no B11 value change (B11 used ^3.487)"}
  - {id: F17, severity: MINOR, location: "chunk 08 line 38", rule: "v3.9 line 126 OR-12; Master line 1163", note: "ACCELERATING without OR-12 FIRING reading", recomputed: "no B11 value change"}
  - {id: F18, severity: MINOR, location: "B11 §2B", rule: "v3.10 26.2 lever by lever", note: "lever bps NOT FOUND; net -48 bps from operator FY28", recomputed: ""}
  - {id: F19, severity: MINOR, location: "B11 §2C-w basis", rule: "v3.10 26.1 RUN-RATE definition", note: "growth-pace extrapolation labelled RUN-RATE", recomputed: "definition run-rate PAT Rs 380.32 Cr"}
  - {id: F20, severity: MINOR, location: "B11 unresolved input 5 (fade anchor)", rule: "override 3 separating observation", note: "FY28 vs 35% does not separate 20% vs 46.9% anchor", recomputed: "FY29 AUM growth vs 27.5%, 31-May-2029"}
  - {id: F21, severity: MINOR, location: "expectation-ledger.md rows D3, W1", rule: "rule 13 probability and status fields", note: "probability n/a; annotated OPEN status; uncredited", recomputed: ""}
  - {id: F22, severity: MINOR, location: "B14 §3.5 chain 7", rule: "Master Rule F confirm-by feeds ledger", note: "no ledger row; uncredited", recomputed: ""}
  - {id: F23, severity: MINOR, location: "B11 FLAG-PILLAR2L-READING", rule: "Pillar 2L both readings", note: "Q1 GNPA 2.25% at the 'below 2.25%' FY27 target (Concall Jun-2026 p.9 line 298) not cited", recomputed: ""}
  - {id: F24, severity: MINOR, location: "B10.bvps_fy26_rs 131.33", rule: "single entity basis (route to Verifier A)", note: "Si Creva equity over OnEMI shares", recomputed: "consolidated FY26 BVPS Rs 143.2"}
  - {id: F25, severity: MINOR, location: "B11 §4D-5 FV path today row", rule: "v3.8 19.0 minimum rows from today", note: "today row = 31-Mar-2027 valuation date", recomputed: ""}
  - {id: F26, severity: MINOR, location: "B11 §1B.1 row D", rule: "v3.3 A4.1 3a; v3.11 27.2 slice-own figures", note: "capacity cross-check and B07 capex-embedded figure not addressed", recomputed: "+0x stands on slice-own reading"}
  - {id: F27, severity: MINOR, location: "B10 table", rule: "Consumption clause; override 5 field", note: "downstream_candidates, Debt Capacity, FTTCP Part B, Market-Implied absent; roce_status conflates T3/T4", recomputed: ""}
critical_count: 0
major_count: 10
minor_count: 17
acceptance_rate: 82.1
acceptance_basis: "78 of 95 rules passed: valuation 39/49, ledger 9/9, Role 2 18/22, chunk fidelity 12/15"
rework_triggered: false
operator_rulings_requested: ["partner-slice cap row (F1)", "own-book slice method under A27.2 (F2)", "capital base of ~34% partner RoE and surplus-cash inclusion (F3)", "A27.1 classification of ~Rs 171 Cr parent-held IPO remainder (F4)", "close BOOK open item on AR figures (F8)"]
```
