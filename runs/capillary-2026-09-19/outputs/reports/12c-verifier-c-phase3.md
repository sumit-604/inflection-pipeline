# Verifier C, PHASE 3: valuation-adherence audit, CAPILLARY

Run folder: runs/capillary-2026-09-19. Executed 2026-10-10. Model: claude-opus-5-5 (effort xhigh).
Scope: the deferred valuation half. B10 and 10-valinputs.md (stage 10), B11 and 11-valuation.md (stage 11), outputs/expectation-ledger.md, and the extended scope: B14 and 14-thesis.md (Role 2 decision rules and position sizing). Check 15 (skill-to-source fidelity) runs on every section-1b chunk B11 cites.
Phase 1 (Gate 0 and Emerging Moat) is in outputs/blocks/B12c.yaml and outputs/reports/12c-verifier-c.md. This pass does not change it.

Rule sources opened: prompts/12-verifiers-pipeline.md (Verifier C section); frameworks/Master_Project_Prompt_v3_6.md (Role 1 l.104-952, Role 2 l.956-1191, RULES l.1515-1531); .claude/skills/section-1b/SKILL.md and chunks 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 12, 14, 15, 17; frameworks/Section_1B_v3.3_Amendments.md (A2, A4.1-A4.4); Section_1B_v3_5_1_Reconciliation.md (A9); Section_1B_v3_8_Amendments.md (A18, A19); Section_1B_v3_9_Amendments.md (full); Section_1B_v3_10_Amendments.md (A26); FTTCP_v2_1_Consolidated.md (Pillar 1 integration l.429-451, hybrid ban l.68); Market_Implied_Assumptions_v1_0.md (Step 1); prompts/11-valuation-pipeline.md (wrapper overrides); .claude/agents/stage-14-thesis.md (B14 schema). Operator authority: outputs/final/fttcp-deliberation.md, OPERATOR-APPROVED VALUATION PILLARS (l.160-180) and overrides O1 to O11 (l.15-27).

Method. I audit rule application, not company quality, and not source fidelity. Verifier A owns whether a number sits in a PDF. I opened no source PDF: no finding below turns on a figure's presence in a filing. Where a rule depends on arithmetic, I re-derived it from the stage's own stated inputs. Operator rulings bind. I test whether each stage applied and disclosed them, not whether the operator should have ruled them.

---

## 0. SUMMARY

- 140 rule checks. 131 pass. 9 fail. Phase 3 adherence 93.6%.
- Valuation half (B10, B11, ledger, check 15, operator rulings): 114 of 121, 94.2%.
- Role 2 extended scope (B14): 17 of 19, 89.5%.
- Severity: 0 CRITICAL, 1 MAJOR, 8 MINOR.
- No REWORK trigger fires. Rules 7, 11, 12, 13 and 14 pass. The acceptance rate is above 60% on a denominator of 140.
- No finding changes the decision. Every reading gives no position at Rs 566.65.
- The MAJOR finding is a chunk defect. Chunk 15 drops the source clause that defines the "governing track" in the A20.5 test. B11 then used Track 2 (16.8x) and printed a relative-route threshold of 24.0x. The source reading uses the track that sets the entry zone, Track 1 (13.1x), so the threshold is 18.7x.
- Operator rulings O1 to O11 are applied and disclosed. B11 values on the approved 30x and reports the divergence on every surface: worksheet, flags, Step 1C, 4G, verdict card.
- Twelve observations need an operator ruling or a framework text fix. They are not counted as fails (Section 11).

---

## 1. GROWTH SYMMETRY CHECKS (rule 4, first block; Section 1B v3.10 A26, Master v3.7 Rules F to J)

| # | Rule | Result | Anchor | Pass? |
|---|---|---|---|---|
| GS1 | 2C-w worksheet line stated in full | Present, all six fields | 11-valuation.md l.374; chunk 17 l.8 | PASS |
| GS2 | Basis declared; HISTORICAL not used where forward evidence exists (26.1) | RUN-RATE for FY27 (Results Q1 FY27 p.9, filed), then GUIDANCE-DISCOUNTED FY28-FY30 (20%+ x 0.72 = 14.4%, approved 15%) | l.318 | PASS |
| GS3 | Historical CAGR beside the basis; >10 pp divergence named with confirm-by (26.1) | 42.2% shown; divergence -20.3 pp; confirm-by H1 FY27 cc organic (Nov-2026) and FY28 revenue Rs 1,225 Cr (May-2028); both on ledger L2, L3 | l.320 | PASS |
| GS4 | Margin bridge lever by lever, evidence line each (26.2) | Five levers, each with evidence and confirm-by: +260 printed, +65 organic leverage, +109 Kognitiv, +175 SessionM, -74 Optum warrant; Year 3 19.90% | l.342-350 | PASS (observation O-9) |
| GS5 | Trailing 3-year average not the base; bear per OR-11 | Base from bridge; bear = run-rate 17.15% less 200 bps, margin-reset reading stated | l.333 | PASS |
| GS6 | Lift above 400 bps names the paying chain (26.2, Rule F) | 535 bps; FTTCP Step 4.5 Chain 3 named; B14 carries it as Chain 3 | l.352; 14-thesis.md l.142 | PASS |
| GS7 | No per-input shading (26.3) | No input lowered "to be conservative". The second revenue reading is sized through L3 (p 0.45) and the dispersion cap, not by cutting the base | l.326 | PASS (net cash hold: see F-V6) |
| GS8 | Weights key to trailing Role 5 delivery, period stated (26.4) | Grade B, 25/50/25, "trailing three quarters of listed delivery (under four)" | l.525; chunk 17 l.24 | PASS |
| GS9 | 2D table complete; standing check answered | Nine rows; "credits the transition" with reasons | l.392-402 | PASS |
| GS10 | Catalyst credit split stated; nothing credited twice (26.1 with A4) | Revenue 100% / Pillar 3 0%; 3a pays on growth machinery; line B credited once via ledger L5, L6 | l.181, l.374, l.543 | PASS |
| GS11 | Pillar 3 premium on the Entrepreneur Ledger carries its supports / does-not-support line (Rule G) | B11 claims no ledger credit (l.175). B14 states the line | 14-thesis.md l.115 | PASS |
| GS12 | Symmetric bar: a base that prices hope flagged as loudly as one that prices the past | B11 flags that the base needs organic near 20% (l.326, l.666), the A14 fade (l.324) and the scenario-vs-ledger split (l.536) | as cited | PASS |

Growth symmetry: 12 of 12.

---

## 2. ROLE 1 PILLAR MECHANICS AND STRUCTURE (rule 4, second block; rule 5)

| # | Rule | Result | Anchor | Pass? |
|---|---|---|---|---|
| M1 | Converter gate stated before pillar math (A17.0) | NON-CONVERTER, three tests, operator Part 1 | l.91 | PASS |
| M2 | Consumption clause: consumed blocks read, gaps named, FTTCP mechanical gate | Debt Capacity and Market-Implied NOT FOUND, named; FTTCP ran and signed off | l.19-23 | PASS |
| M3 | Single-credit map verified before valuing | Stated for ROCE, capital base, base year, cash, complexity, line B | l.30 | PASS |
| M4 | Continuous Pillar 1 formula; base rounded to one decimal | 0.5 x 10.90 + 7.5 = 12.949, 12.9x | l.141; chunk 01 l.8-13 | PASS |
| M5 | FTTCP ROCE verdict is sole authority; correct row | RECOVERING p 0.65 Moderate; ">60% with Strong" row not met; 60/40 row (FTTCP round-down) | l.131; FTTCP l.68, l.438-439 | PASS |
| M6 | Pillar 1 current-ROCE endpoint: A21 run-rate reading disclosed | TTM 6.84% used (operator-approved). The A21 reading (Q1 FY27 annualised 13.6%) and its 19.2x result are not shown; B11 states "Section 1B supports about 17x" as the single reading | l.136-141, l.232 | FAIL MINOR (F-V4) |
| M7 | Normalization route single, declared, disclosure line, 9.1 and 9.2 | Route A-Operational; stripped items with amounts; blend operational-consistent; IPO 20% test disclosed at 19.0% | l.143 | PASS (observation O-7) |
| M8 | ROCE recovery route stated | "Pillar 1 (60/40 blend row)" | l.145 | PASS |
| M9 | Pillar 2 multiplier vs determination; override disclosed | GROWTH-INDUCED (O3); 1.15x (O4); band reading 1.00x shown; Track 2 at 1.00x = 14.9x shown | l.150-160 | PASS |
| M10 | Offset rules (offset only on 0.80x growth band; none on structural) | Offset 0 with reason | l.156 | PASS |
| M11 | Pillar 3 from injected EM, catalyst, evidence; +6x cap | 3a +2x (O9), 3b 0 (EM 24 < 25), 3c 0; cap not reached; 3a documented-tier caveat disclosed | l.166-173 | PASS |
| M12 | A16 gate: minimum ROCE = valuation r; eligibility year | r 14.5% (OR-21); FY28E 17.0% crosses; eligible FY28; bear NO | l.164 | PASS |
| M13 | Shared-catalyst flag | YES, named, Role 3 stress test called | l.175 | PASS |
| M14 | Strategic premium and single credit | +0x; recovery in Pillar 1 bars the optionality route | l.179 | PASS |
| M15 | UA qualifiers evidenced; Amendment 3 order | All three fail, each anchored; F2 = F | l.187-188 | PASS |
| M16 | Sector cap absolute; G2 and G3 | 45x; override N, conditions 1 and 4 fail | l.189-191 | PASS |
| M17 | H range +/-7.5%, nearest 0.5x | 15.57 to 18.10 gives 15.5x to 18.0x | l.209 | PASS |
| M18 | Track 1: r worksheet line, RRM formula and bounds, macro check | r 14.5% (14.0 + 0.5 complexity; durability and governance 0 with NOT FOUND basis); RRM 0.88; CoE gap 60 bps | l.213-215 | PASS (observation O-6) |
| M19 | Both tracks through every fair value, entry and the card | Track 1 = Track 2 at 30x; pillar cross-checks printed | l.494-502, l.675-689 | PASS |
| M20 | Divergence >15%: fit stated; conservative-track entry (OR-1) | 22.5%; fit stated; OR-1 moot because O5 sets 30x on both tracks | l.217 | PASS |
| M21 | Hurdle Ratio on probability-weighted A21 EPS CAGR; bull grade gate; band; OR-2 | HR 0.75 (ledger), base 1.13, bull 1.70 (grade B); STOP; caps nothing | l.279-289; chunk 06 l.39; v3.9 l.117 | PASS |
| M22 | Tier assignment (A4.3) | Tier A: Tier B fails on Gate 0 AVERAGE and EM 24 | l.26; v3.3 l.170-178 | PASS |
| M23 | A21 run-rate base; one-offs; annual divergence >25% stated | Single-quarter annualised; fraud loss, treasury income, tax stated; 77.6% divergence, governing reason given | l.97-127 | PASS |
| M24 | A24 decomposition: three tiers plus residual, Rs Cr, Rs/share, % CMP; four-percentage verdict | Present | l.576-584 | PASS (observation O-1) |
| M25 | A25 fast-growth flag and gate tests | Y on +42.7% run-rate and FIRING (OR-12); starter fails at CMP; Rs 415.2 gate | l.592-603 | PASS |
| M26 | Step 1C display: PENDING, pillar, approved base, gap, governing (A20.1, 20.9) | All printed | l.240-249 | PASS (threshold: F-V1) |
| M27 | Relative PE expression (A15) | Absolute, market PE with stamp, relative, bands NOT FOUND, B8 NONE, conclusion | l.236 | PASS |
| M28 | Recognition gap resolved; matrix cell (override 13) | CLOSED at 81.4x vs TO about 19x; PRICED NARRATIVE (TRAP) | l.255-261 | PASS |
| M29 | Market-implied Reading 1 basis (chunk 14 l.18; MIA l.27, l.29) | Reading 1 solved at r 14.5%, not at the operator's required return | l.263-267 | FAIL MINOR (F-V5) |
| M30 | Market-implied Reading 2, story, spread, flag | 45x cap reading and 30x reading both shown; story; spread; PRICED-WE-ARE-LATE stated at the governing multiple | l.268-275 | PASS |
| M31 | 2A bear and bull rules | Bear: lower of 37.2%, 12%, triggers failing; bull at guidance, grade B | l.316 | PASS |
| M32 | 2B bear and bull rules | Bear current - 200 bps (OR-11); bull guided floor at grade B | l.333 | PASS |
| M33 | A14 fade shown, value effect stated | FY30 EPS Rs 19.67, -Rs 50 at 30x; approved scenarios bind (O11) | l.324 | PASS |
| M34 | SOM cross-check | Justified excess named (SessionM step) | l.322 | PASS |
| M35 | DCF: Master parameter sets, terminal cap with macro stamp, TV share | 4/5/6%, 14/12/11%; cap 6.0%; TV 88.2% so weight 20%; grid shown | l.445-477 | PASS |
| M36 | 4B methods agreement; outlier named when spread >30% | 69.0%; outlier is P/E at 30x | l.504-511 | PASS |
| M37 | 4C and 4D from the grade; re-weighting rule checked | Good weights; rule not triggered; alternatives shown | l.513-536 | PASS |
| M38 | 4E entry divisor (OR-8), 30% price, MoS price, A19 beside the zone | 640.1 / 1.953125 = 327.7; / 2.197 = 291.4; MoS 229.4 (reference, A25 governs) | l.624-635 | PASS |
| M39 | 4F upside/downside | 0.24x, below 2x | l.637-644 | PASS |
| M40 | 4G table complete; failure reported | Check 6 FAILS at 30x (Year-3 pillar about 24x); reported, not revised under A20.9 | l.646-657 | PASS (observation O-2) |
| M41 | 4H-pre four elements | Value vs price, MoS row, dispersion 111.7% Small, edge PROCESS | l.659-666 | PASS |
| M42 | 4H card, all fields and later-layer lines | Tier line first; converter; both tracks; Step 1C; A24; A19; decision bands | l.670-701 | PASS |
| M43 | Override 3: every unresolved input with both readings and the separating observation | Item 6 (B7 Year-3 net debt) has neither | l.744 | FAIL MINOR (F-V6) |
| M44 | One improvement, one mechanism | Line B once through EPS (O8); D2 not carried (base taxed at 25%); complexity only in r; cash only in Pillar 2 | l.30, l.543, l.562 | PASS |
| M45 | Chunk citations beside pillar rows, multipliers, caps, rulings (wrapper override 16) | Present throughout | l.195-207 and passim | PASS |
| M46 | Macro sheet month stamp; staleness flag | August 2026 stamp; FLAG-MACRO-STALE | l.27 | PASS |

Role 1 mechanics: 43 of 46.

---

## 3. STRUCTURAL RULES 6, 7, 11, 12

| # | Rule | Result | Anchor | Pass? |
|---|---|---|---|---|
| S1 | Rule 6: B09 candidates >=3 or the exact sentence | 6 candidates; demand_externally_verifiable true | B09-tam.yaml l.48-55 | PASS |
| S2 | Rule 6: stage 11 catalysts cite a candidate or carry the MODERATE cap | Ledger column populated; L5, L6 carry "evidence-thin, magnitude capped MODERATE" | 11-valuation.md l.547-560 | PASS |
| S3 | Rule 7: Section 1A matrix, >=2 methods, weights | Matrix; P/E 80%, DCF 20%; triangulation table | l.36-83, l.492-500 | PASS |
| S4 | Rule 11: Section 2 reaches Year 4 in all cases | FY30 bear, base, bull | l.313, l.358-362 | PASS |
| S5 | Rule 11: exit basis = entry basis, both stated | Forward at both ends (O6) | l.95, l.379 | PASS |
| S6 | Rule 11: resolution calendar per slice | SessionM, Kognitiv, unmigrated remainder; window, class, event, tracker row | l.382-386 | PASS |
| S7 | Rule 11: within-hold resolved at exit; bear at failure | Through consolidated EPS (O8); bear carries L5, L6 at failure | l.388 | PASS |
| S8 | Rule 11: beyond-hold re-dated, or zero where no event | Remainder has no nameable event, zero | l.386 | PASS |
| S9 | Rule 11: transition dual display | Static and resolution exits, delta Rs 0 | l.388 | PASS |
| S10 | Rule 12: FV path today to end-Year-3, governing track | Four rows at 30x machinery | l.609-614 | PASS |
| S11 | Rule 12: FV CAGR line | 37.9% (34.0% on triangulated end-point) | l.616 | PASS |
| S12 | Rule 12: label and decomposition line | COMPOUNDER; decomposition with static share and no re-rating lever | l.618-620 | PASS |
| S13 | Rule 12: FV-step lines or stated none | None (O8), tracking equivalents shown | l.622 | PASS |
| S14 | Rule 12: label on the verdict card | Present | l.694 | PASS |

Structural rules: 14 of 14. No REWORK from rules 6, 7, 11 or 12.

---

## 4. EXPECTATION LEDGER AND GATES (rules 13, 14)

| # | Rule | Result | Anchor | Pass? |
|---|---|---|---|---|
| EL1 | Ledger exists in the Appendix A schema | Eight columns as v3.9 l.139 | expectation-ledger.md l.17 | PASS |
| EL2 | At least one downside row | Four: D1, D3, D4, D5 | l.27-30 | PASS |
| EL3 | Every row has a confirm-by date | 12 of 12 | l.19-30 | PASS |
| EL4 | Every row has a confirming metric and threshold | 12 of 12 | l.19-30 | PASS |
| EL5 | Each probability in [0.00, 1.00] | 0.15 to 0.90 | l.19-30 | PASS |
| EL6 | Tier matches p (>=0.50 T2, <0.50 T3) | L1 0.85, L2 0.75, L4 0.55 in T2; L3, L5, L6, U1, U2 in T3; downside netted against T2 (chunk 09 l.29) | l.56-67 | PASS |
| EL7 | Status valid; decay shows the 25% step | All OPEN; no decayed row | l.19-30 | PASS |
| EL8 | 14(a): no credit off-ledger | Every T2 and T3 credit maps to a row; D2 dropped and named | 11-valuation.md l.578-581; ledger l.32 | PASS |
| EL9 | 14(b): residual above 25% caps at starter | Residual 15.0%; no position at CMP | l.581, l.584 | PASS (observation O-1) |

Arithmetic ties (rule-level only): T2 gross 4.199 + 34.013 + 6.897 = 45.11; downside 7.20 + 7.50 + 15.12 + 2.78 = 32.60; T2 net 12.51; T3 11.72 + 8.36 + 13.38 + 2.25 + 11.12 = 46.84; base rows L1 to L6 less D1, D4 = 118.44 = 175.80 - 57.36 (expectation-ledger.md l.69-71; 11-valuation.md l.566). Rules 13 and 14: 9 of 9. No REWORK.

---

## 5. OPERATOR RULINGS: APPLICATION AND DISCLOSURE

| Ruling | Applied as ruled? | Disclosed? | Anchor | Pass? |
|---|---|---|---|---|
| O1 operating ROCE basis | Yes | Yes, with company and AR bases shown | 11-valuation.md l.135, l.143 | PASS |
| O2 proof-gate period | Yes (quarter, annualised) | Yes | l.31 (YAML flags), l.718 | PASS |
| O3 cash GROWTH-INDUCED | Yes | Yes; INDETERMINATE cap superseded | l.155, l.160 | PASS |
| O4 Pillar 2 1.15x | Yes | Yes, band reading 1.00x and its 14.9x | l.157-160 | PASS |
| O5 exit 30x both tracks | Yes | Yes, on every surface (+78.6% / +129.0%, DCF 16.7x, 4G, Step 1C) | l.219-232, l.682-684 | PASS |
| O6 forward basis, end-FY29 on FY30 EPS | Yes | Yes | l.95 | PASS |
| O7 EPS definition and Rs 57 bridge | Yes; bridge date anchored 31-Mar-2026 with five readings | Yes (FLAG-BRIDGE) | l.729-739 | PASS |
| O8 line B zero | Yes | Yes | l.384-388, l.543 | PASS |
| O9 grade B, 3a +2x, bull at face value | Yes | Yes, Verifier B conflict recorded | l.25, l.173, l.279 | PASS |
| O10 peer set | Yes | Yes | l.242 | PASS |
| O11 scenarios and weights | Yes; Excellent sensitivity shown | Yes, with the A14 and ledger divergences | l.299, l.534 | PASS |

Operator rulings: 11 of 11.

---

## 6. STAGE 10 ASSEMBLY (B10)

| # | Rule | Result | Anchor | Pass? |
|---|---|---|---|---|
| A1 | Deliberation authority carried; conflicts logged | 12 conflicts with both values and the one used | B10-valinputs.yaml l.228-240 | PASS |
| A2 | Approved pillars block copied in full | Present | l.150-168 | PASS |
| A3 | Unresolved inputs listed with where-it-might-be | 10 rows | l.241-251 | PASS |
| A4 | C.2 probabilities flagged NOT operator-ruled | Present | l.25, l.273 | PASS |
| A5 | Phase-1 verifier corrections carried | F-G2 not carried: cash_evidence repeats the struck "FY26 helped by payable days 66.6 to 37.0" | l.112; B12c.yaml l.11 | FAIL MINOR (F-V7) |

Stage 10: 4 of 5.

---

## 7. SKILL-TO-SOURCE FIDELITY (check 15)

B11 reports "Chunk-versus-source disagreements found: none" and opened no Section 1B source file (11-valuation.md l.776). That was within its wrapper (prompts/11-valuation-pipeline.md l.11-13). The check below finds three divergences. Each is a finding against the chunk, for an operator fix. B11 is re-checked against the source reading.

| # | Chunk (path, line) | Source (file, line) | Result |
|---|---|---|---|
| C1 | 01 l.8-13 Pillar 1 formula | Master l.282-289 | Match |
| C2 | 01 l.21-29 ROCE selection table | FTTCP l.435-441 (governs Pillar 1 selection) | Match (Master l.296 stale: O-4) |
| C3 | 01 l.42-57 Route A, 9.1, 9.2 | v3.5.1 l.24-34 | Match |
| C4 | 02 l.10-35 bands, test, offsets | Master l.315-339 | Match |
| C5 | 03 l.14-41 3a, 3b, 3c | v3.3 l.144-160; Master l.375-383 | Match |
| C6 | 03 l.8, 12 l.10-14 A16 gate | Master l.371 | Match |
| C7 | 04 l.10-24 strategic premium | Master l.395-401; FTTCP l.447-449 | Match |
| C8 | 05 l.8-19, l.57-59 UA, cap, uplift | Master l.410-450 | Match |
| C9 | 06 l.52-57 two-tier hurdle | v3.3 l.170-186 | Match |
| C10 | 06 l.37-49 Hurdle Ratio | v3.3 l.30-40; v3.9 l.117 | Match |
| C11 | 06 l.92 4G | Master l.897 | **DIVERGES** (F-V2) |
| C12 | 06 l.26-33 dual track, entry | Master l.564, l.824; OR-8 | Match |
| C13 | 07 l.6-29, l.54-77 26.1 to 26.3 | v3.10 l.24-64 | Match |
| C14 | 08 l.10-17 A21 | v3.9 l.66-70 | Match |
| C15 | 08 l.31 A24 tier multiple | v3.9 l.108-113 with l.58 | **DIVERGES** (F-V3) |
| C16 | 08 l.38-44 A25 | v3.9 l.126-131, l.241 | Match (Master l.1168 omits Gate 0: O-5) |
| C17 | 09 l.8-48 A22, A23, Appendix A | v3.9 l.79-97, l.139-144 | Match |
| C18 | 10 l.8-52 A18 | v3.8 l.11-36 | Match |
| C19 | 12 l.26-63 A19 | v3.8 l.46-61 | Match |
| C20 | 14 l.12-21 Readings 1 and 2 | Market_Implied_Assumptions_v1_0.md l.27-32 | Match |
| C21 | 15 l.92 A20.5 governance rule | v3.9 l.40 | **DIVERGES** (F-V1) |
| C22 | 15 l.96 A20.9 approved base binds | v3.9 l.58 | Match |
| C23 | 15 l.26-40, l.55-62 RRM, r, DCF | Master l.559-562, l.776-797 | Match (term undefined in both: O-6) |
| C24 | 17 l.20-43 Rule E, 4D weights | v3.10 l.68; Master l.853-858 | Match |

Check 15: 21 of 24.

**C21 / F-V1 (MAJOR).** Chunk 15 l.92: "**20.5 Governance rule.** Pillar destination (governing track) more than 30% below the adjusted peer base (pillar < 0.70 × adjusted peer base) → the RELATIVE multiple governs the exit". Source v3.9 l.40: "Compare the pillar destination PE (the governing-track destination that sets the entry zone) against the base-case adjusted peer base of 20.3". The chunk drops "that sets the entry zone". The chunk never defines "governing track". B11 read it as the track that "fits this business better" and used Track 2 16.8x (11-valuation.md l.245-246). B11's own l.217 says that under OR-1 "the more conservative track (Track 1) would set the entry zone on a pillar base". On the source text the A20.5 pillar is Track 1. Re-check of B11 on the source reading: relative route opens above 13.055 / 0.70 = 18.65x, about 18.7x (B11: 24.0x). Pillar gap to 30x is 56.5% (B11: 44.0%). The value travels to B11 YAML l.66, the card l.684, unresolved input 2 l.740 and B14 monitoring row 13 (14-thesis.md l.341). The statement "Section 1B reaches 30x only if the adjusted peer base is 30x or higher" does not change. The decision survives. Fix: restore the source parenthetical in chunk 15.

**C11 / F-V2 (MINOR).** Chunk 06 l.92: "If any check fails, revise the exit PE and recalculate." Source Master l.897: "If any check fails, revise the exit PE downward and recalculate." The chunk drops "downward", which makes 4G two-sided. No B11 value changes. B11 quoted the Master text correctly (l.657). Fix: restore "downward".

**C15 / F-V3 (MINOR).** Chunk 08 l.31 holds two sentences that point different ways when an approved base exists and no peer table does: "The destination PE in each tier is the governing Section 1B destination (the operator-approved base where one exists)" and "without one, the tier multiple is the pillar destination". Source v3.9 l.110-112 says "Destination PE (Section 1B)" and l.58 says "value on the approved base unless the operator re-rules". B11 used 30x (consistent with the source) and showed the pillar sensitivity (residual 47.9%, l.586). No B11 value changes. The wrapper carries the same tension (prompts/11-valuation-pipeline.md l.133-140). Fix: carve out the approved base in the second sentence.

---

## 8. ROLE 2 EXTENDED SCOPE (B14 against Master Role 2 and v3.9 A25)

| # | Rule | Result | Anchor | Pass? |
|---|---|---|---|---|
| R1 | Header block | Five fields with Verifier C corrections beside stage values | 14-thesis.md l.10-19 | PASS |
| R2 | One-line thesis template; A19 label | All template elements; COMPOUNDER and "price ahead of value" | l.25 | PASS |
| R3 | Snapshot, incl. fast-growth flag and converter | Present | l.33-51 | PASS |
| R4 | 3A references Gate 0 | Yes, with both readings of the deal-breakers | l.57-63 | PASS |
| R5 | 3B triggers: timeline, confidence, confirms, kills | Seven ranked rows; ledger p shown as stage 11's | l.65-77 | PASS |
| R6 | 3C to 3F present | Present | l.79-101 | PASS |
| R7 | 3G every row filled or NOT FOUND; Pillar 3 line; single credit; ledger lifts no cap | Present | l.103-115 | PASS |
| R8 | 3.5: five chains minimum, [INFERENCE] each, PENDING LIVE VERIFICATION named, bridge chain carried | Eight chains; five live links marked | l.119-193 | PASS (observation O-11) |
| R9 | Section 4 cross-reference; hardest verdict wins | 18 rows | l.197-216 | PASS |
| R10 | Section 5 incl. A19 two lines, Hurdle band, return-matrix counts | 0 of 9 at 25%; 3 of 9 at 15% | l.220-243 | PASS |
| R11 | Pillar cross-check FV CAGR honours A16 pre-crossover years | Today's pillar FV at 16.8x includes +2x Pillar 3 before the FY28 crossover | l.234; B14 YAML l.30 | FAIL MINOR (F-R1) |
| R12 | Section 7 decision rules traced; conflict flagged | BUY NOW, DIPS, WATCHLIST, INSUFFICIENT, AVOID each traced; AVOID vs WATCHLIST flagged | l.294-302 | PASS (observation O-3) |
| R13 | Entry conjunction in the box | Present | l.287-290 | PASS |
| R14 | Position size: dispersion cap; A25 starter, add, trim; Gate 0 and Promoter bind the ladder | Small cap from 111.7%; starter fails at 54.9%; Gate 0 bars Medium, consistent with v3.9 l.241 | l.304-311 | PASS |
| R15 | OR-14 promoter routing | STRUCTURE; 4 of 4 heads from filed sources; tripwires named; lifts no cap | l.310 | PASS |
| R16 | Thesis-broken triggers measurable; time stop | Seven items | l.314-321 | PASS |
| R17 | Section 8 checklist specific and measurable | 13 rows, green and red thresholds | l.327-341 | PASS |
| R18 | Section 9, narrative, publish flag | Present | l.345-386 | PASS |
| R19 | YAML consistent with the verdict box | position_size "Small" on an AVOID verdict whose box says "NONE at CMP" | B14 YAML l.8; 14-thesis.md l.278 | FAIL MINOR (F-R2) |

Role 2 extended: 17 of 19.

---

## 9. FINDINGS REGISTER

| ID | Severity | Location | Rule | Stated | Recomputed / required |
|---|---|---|---|---|---|
| F-V1 | MAJOR | chunk 15 l.92; B11 11-valuation.md l.245-248, l.684, l.740; B11 YAML l.66; B14 l.341 | Check 15; v3.9 A20.5 (l.40) | Relative route opens above 24.0x (Track 2 16.8x / 0.70); pillar 44.0% below 30x | On the source reading the governing-track pillar is Track 1 (sets the entry zone under OR-1 as written): opens above 18.7x (13.055 / 0.70); gap 56.5%. Fix the chunk; restate both thresholds |
| F-V2 | MINOR | chunk 06 l.92 | Check 15; Master 4G l.897 | "revise the exit PE and recalculate" | "revise the exit PE downward and recalculate". No B11 value changes |
| F-V3 | MINOR | chunk 08 l.31; prompts/11 l.133-140 | Check 15; v3.9 A24 l.110-112 with A20.9 l.58 | Tier multiple: approved base, and also pillar when no peer table | Approved base governs where one exists; pillar shown as sensitivity. B11 already did this |
| F-V4 | MINOR | 11-valuation.md l.136-141, l.232 | A21 (v3.9 l.67, l.237); Rule J symmetric bar | Pillar 1 current endpoint TTM 6.84%; "Section 1B supports about 17x" with no other reading | Show reading (b): A21 run-rate endpoint 13.56% gives Pillar 1 14.9%, base 15.0x, C 17.25x, Track 2 about 19.3x (deliberation l.82 printed 19.2x), Track 1 about 15.2x. Operator-approved TTM stands; 30x is still +56% above |
| F-V5 | MINOR | 11-valuation.md l.263-267 | Chunk 14 l.18; MIA l.27, l.29 (Reading 1 at the operator's required return) | Reading 1: FY30 EPS Rs 9.75, EPS CAGR 11.9% at r 14.5% | At 25%: end-FY29 value Rs 1,106.7; (1,106.7 - 57) / 81.4 = Rs 12.90; EPS CAGR 22.8%. Flag unchanged |
| F-V6 | MINOR | 11-valuation.md l.744 (item 6), l.370 | Wrapper override 3 (prompts/11 l.37-43); rule 4 | B7 Year-3 net debt NOT FOUND; net cash held at Rs 469.7 Cr; no both-readings line | Reading (a) static hold (A19.0, deployed to M&A, deck May-2026 p.63 per B11). Reading (b) no new M&A, interim base FCF Rs 389.4 Cr accrues: +Rs 47.3 per share; weighted base FV Rs 687.4; 25% entry Rs 351.9; 30% entry Rs 312.9; base CAGR 6.6%. Separating observation: FY27 AR cash and any Reg 30 acquisition. Decision unchanged |
| F-V7 | MINOR | B10-valinputs.yaml l.112 | Phase-1 corrections carried into B10 (B12c F-G2) | "FY26 helped by payable days 66.6 to 37.0" | FY23 to FY26 move consumed cash; FY26 receivable days 98.3 to 89.8 and payable days 30.9 to 37.0 helped CFO (B12c.yaml l.11). B11 does not rely on it (O3 governs); B14 corrected it (l.212) |
| F-R1 | MINOR | 14-thesis.md l.234; B14 YAML l.30 | A16 (chunk 12 l.10-13): no Pillar 3 in pre-crossover years | Pillar FV CAGR 33.7% (Rs 173.9 to Rs 415.4) | Today is FY27, pre-crossover (FY27E 11.7% < r 14.5%, 11-valuation.md l.164). Today's pillar FV at C 14.835x = Rs 160.3; FV CAGR about 37.4%. Label COMPOUNDER unchanged |
| F-R2 | MINOR | B14 YAML l.8 | YAML must agree with the Section 7 box | position_size "Small" | "none (ceiling Small)". Schema enum lacks a none value (.claude/agents/stage-14-thesis.md l.61): fix the schema |

---

## 10. RECOMPUTED VALUES

- Destination PE: concur. Pillar Track 2 16.8x (15.5x to 18.0x) and Track 1 13.1x (12.0x to 14.0x) re-derive from the approved inputs. Governing 30x is the operator's ruling (O5).
- Decision: concur. No position at Rs 566.65. Hurdle STOP on every reading.
- Step 1C relative-route threshold on the source reading: 18.7x (Track 1), not 24.0x.
- Sensitivities owed to the record (not replacements): Track 2 about 19.3x on the A21 current endpoint; reading (b) base FV Rs 687.4 and 25% entry Rs 351.9 if interim FCF accrues; Reading 1 EPS CAGR 22.8%; B14 pillar FV CAGR about 37.4%.

---

## 11. OBSERVATIONS FOR THE OPERATOR (not counted as fails)

- **O-1 Net cash in the A24 decomposition (framework silent).** v3.9 A24 (l.108-113) names three earnings tiers and a residual. It does not say where the equity bridge sits, and the E2E worked case carries no bridge (l.177-183). B11, following the deliberation (l.122), puts Rs 57 in T1. Reading (b), bridge outside the tiers: T1 36.9%, T1 + T2 44.9%, residual 25.0% (at the 25% starter-cap line), A25 starter price about Rs 339 instead of Rs 415. No decision changes at CMP. The re-entry gate in B14 moves by Rs 76. Rule it.
- **O-2 Master 4G vs an approved base.** Master l.897 says revise the exit PE down when a 4G check fails. A20.9 (v3.9 l.58) and the wrapper (prompts/11 l.184-186) say value on the approved base. B11 followed the approved base and reported check 6 FAIL (30x vs a Year-3-metric pillar of about 24x). At /finalize, either re-rule O5 or record that 4G yields to an approved base.
- **O-3 Verdict conflict.** Role 2 Section 7 (Master l.1129) fires AVOID on Gate 0 AVERAGE and on U/D 0.24x. RULES (Master l.1521) default Gate 0 below 60 to WATCHLIST. B11 says WATCHLIST; B14 says AVOID under hardest-verdict-wins and flags it, as in KISSHT. Stage 13 must reconcile. A standing ruling closes it.
- **O-4 Stale Master text.** Master l.296 still carries the banned hybrid label "RECOVERING-to-FIRING (probability >60%)". FTTCP l.438 (sole Pillar 1 authority) and chunk 01 read "RECOVERING, probability >60% with Strong catalysts". Fix the Master.
- **O-5 Master Role 2 A25 text.** Master l.1168 lists dispersion, Promoter and Sector Literacy as binding the fast-growth ladder. v3.9 l.241 says "The top-level sizing rules (Gate 0, Promoter) still bind the ladder's ceiling." B14 followed v3.9. Align the Master.
- **O-6 "Fundamental Base PE" undefined.** Master l.559 and chunk 15 l.26 use it without a definition. B11 and the deliberation use C (14.835x), giving 13.1x. On F (16.835x) Track 1 would be 14.8x. Define it.
- **O-7 O1 is a standing rule for all names** (deliberation l.17) but sits in neither SKILL.md's ruled list nor CLAUDE.md OPERATOR RULINGS. It displaces the Route A 20% test, which reads 19.0% on unutilised IPO proceeds at 30-Jun-2026 (11-valuation.md l.143). Record it.
- **O-8 Wrapper ambiguity.** prompts/11 l.235-240 says to carry the probability-weighted EPS CAGR "to expected_cagr_prob_weighted". B11 carries the 4D expected return (1.3%), which matches Master 4H. The 26.7% EPS CAGR has no YAML field. Add one.
- **O-9 Bridge lever sizes are an allocation.** B11 splits the approved total in the draft C.2 proportions (l.340). Each lever has an evidence line, so 26.2 passes. The bridge does not independently evidence the 22.0% FY30 margin.
- **O-10 Approved base vs stage 11's own probabilities.** Scenario weights put 75% on base-or-better; the ledger gives the base revenue lift p 0.45 and credits 47.5% of the base increment (l.536, l.566). B11 disclosed it with the separating observation (Q2 FY27). The operator should ratify or replace the ledger probabilities at /finalize (FLAG-C2-PROBABILITIES).
- **O-11 Chain confirm-by lines.** B14 names three new monitors (Chains 1, 2, 3) for the ledger owner (l.193). They are not credited in price, so no off-ledger credit. Add them to expectation-ledger.md or the tracker.
- **O-12 Phase-1 block model string.** outputs/blocks/B12c.yaml l.4 reads "claude-opus-5". The agent frontmatter is claude-opus-5-5. The orchestrator compares the two. This phase-3 block carries the correct string.

Not in scope: rule 9 (stage 13 narrative) and rule 10 (Halt 1 dossier at /finalize). Neither artifact is among the phase-3 inputs.

---

## 12. COUNTS

| Group | Passed | Checked |
|---|---|---|
| Growth symmetry | 12 | 12 |
| Role 1 mechanics | 43 | 46 |
| Structural rules 6, 7, 11, 12 | 14 | 14 |
| Ledger rules 13, 14 | 9 | 9 |
| Operator rulings O1-O11 | 11 | 11 |
| Stage 10 assembly | 4 | 5 |
| Check 15 skill-to-source | 21 | 24 |
| **Valuation half** | **114** | **121 (94.2%)** |
| Role 2 extended (B14) | 17 | 19 (89.5%) |
| **Phase 3 total** | **131** | **140 (93.6%)** |

REWORK: none. No CONFIRMED Verifier A item is in scope here. Rules 7, 11, 12, 13 and 14 pass. Acceptance 93.6% on 140.

---

```yaml
stage: B12c
company: "CAPILLARY"
run_date: "2026-09-19"
model: "claude-opus-5-5"
status: complete
scope: "phase-3 valuation half: B10, B11, expectation-ledger.md, B14 extended scope (Role 2 decision rules and sizing); check 15 skill-to-source on every chunk B11 cites"
phase1_block: "outputs/blocks/B12c.yaml (gate0 and emoat; unchanged by this pass)"
gate0: {rules_checked: 0, fails: [], status: "PHASE 1, see B12c.yaml"}
emoat: {rules_checked: 0, fails: [], status: "PHASE 1, see B12c.yaml"}
valuation:
  rules_checked: 121
  rules_passed: 114
  breakdown: {growth_symmetry: "12 of 12", role1_mechanics: "43 of 46", structural_rules_6_7_11_12: "14 of 14", ledger_rules_13_14: "9 of 9", operator_rulings_o1_o11: "11 of 11", stage10_assembly: "4 of 5", check15_skill_to_source: "21 of 24"}
  fails:
    - {id: F-V1, severity: MAJOR, location: "chunk 15 l.92; 11-valuation.md l.245-248, l.684, l.740; B11 YAML l.66; 14-thesis.md l.341", rule: "check 15; Section 1B v3.9 A20.5 (l.40) 'the governing-track destination that sets the entry zone'", stated: "relative route opens above 24.0x (Track 2 16.8x / 0.70); pillar 44.0% below 30x", recomputed: "Track 1 sets the entry zone under OR-1 as written (B11 l.217): opens above 18.7x (13.055 / 0.70); gap 56.5%; 30x still needs an adjusted base >= 30x; decision survives; fix the chunk"}
    - {id: F-V2, severity: MINOR, location: "chunk 06 l.92", rule: "check 15; Master 4G l.897", stated: "revise the exit PE and recalculate", recomputed: "revise the exit PE downward and recalculate; no B11 value changes"}
    - {id: F-V3, severity: MINOR, location: "chunk 08 l.31; prompts/11-valuation-pipeline.md l.133-140", rule: "check 15; v3.9 A24 l.110-112 with A20.9 l.58", stated: "tier multiple is the approved base, and also the pillar when no peer table exists", recomputed: "approved base governs where one exists, pillar as sensitivity; B11 already applied this; no value changes"}
    - {id: F-V4, severity: MINOR, location: "11-valuation.md l.136-141, l.232", rule: "A21 (v3.9 l.67, l.237) run-rate base for every Section 1B pillar; Rule J symmetric bar", stated: "Pillar 1 current endpoint TTM 6.84%; Section 1B supports about 17x, single reading", recomputed: "reading (b) A21 endpoint 13.56%: Pillar 1 14.9%, base 15.0x, C 17.25x, Track 2 about 19.3x (deliberation l.82: 19.2x), Track 1 about 15.2x; operator-approved TTM stands; disclose both"}
    - {id: F-V5, severity: MINOR, location: "11-valuation.md l.263-267", rule: "chunk 14 l.18; Market_Implied_Assumptions_v1_0.md l.27, l.29: Reading 1 at the operator's required return", stated: "Reading 1 FY30 EPS Rs 9.75, EPS CAGR 11.9% at r 14.5%", recomputed: "at 25%: Rs 1,106.7 end-FY29 value, FY30 EPS Rs 12.90, EPS CAGR 22.8%; flag unchanged"}
    - {id: F-V6, severity: MINOR, location: "11-valuation.md l.744 (item 6), l.370", rule: "wrapper override 3 (prompts/11 l.37-43): both readings and separating observation for every unresolved input", stated: "B7 Year-3 net debt NOT FOUND; net cash held at Rs 469.7 Cr; no both-readings line", recomputed: "reading (b) no new M&A, interim base FCF Rs 389.4 Cr accrues: +Rs 47.3/share, weighted base FV Rs 687.4, 25% entry Rs 351.9, 30% entry Rs 312.9, base CAGR 6.6%; separating observation FY27 AR cash and any Reg 30 acquisition; decision unchanged"}
    - {id: F-V7, severity: MINOR, location: "B10-valinputs.yaml l.112", rule: "phase-1 Verifier C corrections carried into assembly (B12c F-G2)", stated: "FY26 helped by payable days 66.6 to 37.0", recomputed: "66.6 to 37.0 is FY23 to FY26 and consumed cash; FY26 receivable days 98.3 to 89.8 and payable days 30.9 to 37.0 helped CFO; no B11 value depends on it (O3 governs)"}
role2_extended:
  rules_checked: 19
  rules_passed: 17
  fails:
    - {id: F-R1, severity: MINOR, location: "14-thesis.md l.234; B14 YAML l.30", rule: "A16 (chunk 12 l.10-13): no Pillar 3 in pre-crossover years", stated: "pillar FV CAGR 33.7% (Rs 173.9 to Rs 415.4)", recomputed: "today (FY27, ROCE 11.7% < r 14.5%) at C 14.835x = Rs 160.3; FV CAGR about 37.4%; label COMPOUNDER unchanged"}
    - {id: F-R2, severity: MINOR, location: "B14 YAML l.8", rule: "YAML agrees with the Section 7 box (14-thesis.md l.278 'NONE at CMP')", stated: "position_size: Small", recomputed: "none (ceiling Small); add a none value to the schema enum (.claude/agents/stage-14-thesis.md l.61)"}
expectation_ledger: {present: true, downside_row: true, all_rows_confirm_by: true, all_rows_metric_threshold: true, prob_in_range: true, decay_status_valid: true, off_ledger_credit: false, residual_pct_cmp: 15.0, residual_starter_cap_ok: true, fails: [], note: "residual 15.0% with net cash in T1; 25.0% if the bridge sits outside the tiers (observation O-1)"}  # rules 13-14; any fail = REWORK stage 11
business_understanding_narrative: {status: "NOT IN SCOPE (stage 13 output not among phase-3 inputs; rule 9 runs at /finalize)", fails: []}  # rule 9; any fail = REWORK stage 13
skill_to_source: {rows_checked: 24, divergences: 3, chunks_with_findings: ["references/15-cost-of-capital-relative-valuation.md l.92 (MAJOR)", "references/06-summary-sanity-hurdle.md l.92 (MINOR)", "references/08-run-rate-base-price-decomposition.md l.31 (MINOR)"], b11_self_report: "none found; B11 opened no Section 1B source file"}
rework_triggers: "none fired: rules 7, 11, 12, 13, 14 pass; acceptance 93.6% on a denominator of 140"
recomputed_destination_pe: ""
recomputed_decision: ""
recomputed_values:
  - "Step 1C relative-route threshold on the source reading: 18.7x (Track 1), not 24.0x"
  - "Track 2 on the A21 current-ROCE endpoint: about 19.3x (sensitivity; operator-approved TTM 16.8x stands)"
  - "Net cash reading (b): base weighted FV Rs 687.4, 25% entry Rs 351.9 (sensitivity)"
  - "Market-implied Reading 1 at 25%: EPS CAGR 22.8% (stated 11.9%)"
  - "B14 pillar FV CAGR with A16 timing: about 37.4% (stated 33.7%)"
findings:
  - {id: F-V1, stage: "chunk 15 / B11 / B14", severity: MAJOR, summary: "chunk drops 'that sets the entry zone' from A20.5; B11 used Track 2; threshold 24.0x should be 18.7x"}
  - {id: F-V2, stage: "chunk 06", severity: MINOR, summary: "4G 'downward' dropped"}
  - {id: F-V3, stage: "chunk 08 / wrapper", severity: MINOR, summary: "A24 tier-multiple sentences conflict when an approved base exists without a peer table"}
  - {id: F-V4, stage: B11, severity: MINOR, summary: "A21 run-rate reading of the Pillar 1 current endpoint (about 19.3x) not disclosed"}
  - {id: F-V5, stage: B11, severity: MINOR, summary: "market-implied Reading 1 solved at r, not at the 25% required return"}
  - {id: F-V6, stage: B11, severity: MINOR, summary: "B7 Year-3 net debt unresolved input lacks both readings and the separating observation"}
  - {id: F-V7, stage: B10, severity: MINOR, summary: "phase-1 F-G2 cash-mechanism correction not carried"}
  - {id: F-R1, stage: B14, severity: MINOR, summary: "pillar FV CAGR cross-check credits Pillar 3 before the A16 crossover"}
  - {id: F-R2, stage: B14, severity: MINOR, summary: "position_size Small on an AVOID verdict with NONE at CMP; schema lacks none"}
observations_for_operator:
  - "O-1 net cash placement in A24 (source silent): T1 46.9% / residual 15.0% / starter Rs 415 vs bridge outside tiers T1+T2 44.9% / residual 25.0% / starter about Rs 339"
  - "O-2 Master 4G 'revise downward' vs A20.9 approved base: re-rule O5 at /finalize or record that 4G yields"
  - "O-3 verdict conflict AVOID (Role 2 s7) vs WATCHLIST (RULES Gate 0 below 60; B11): standing ruling needed, as KISSHT"
  - "O-4 Master l.296 carries the banned hybrid label; FTTCP l.438 and chunk 01 are correct"
  - "O-5 Master l.1168 omits Gate 0 from what binds the A25 ladder; v3.9 l.241 includes it"
  - "O-6 'Fundamental Base PE' undefined (Master l.559, chunk 15 l.26); on F Track 1 would be 14.8x"
  - "O-7 O1 standing rule (all names) not recorded in SKILL.md or CLAUDE.md; it displaces the Route A 20% test (19.0%)"
  - "O-8 wrapper prompts/11 l.239-240 ambiguity: prob-weighted EPS CAGR 26.7% has no YAML field"
  - "O-9 margin bridge lever sizes allocated from the approved total in draft C.2 proportions"
  - "O-10 ledger probabilities (L3 0.45) vs scenario weights (75% base-or-better): ratify or replace at /finalize"
  - "O-11 three B14 chain monitors not yet on expectation-ledger.md"
  - "O-12 phase-1 B12c.yaml model string 'claude-opus-5' differs from frontmatter claude-opus-5-5"
critical_count: 0
major_count: 1
minor_count: 8
phase3_checks_passed: 131
phase3_checks_total: 140
acceptance_rate: 93.6
framework_adherence_pct_valuation_half: 94.2
framework_adherence_pct_role2_extended: 89.5
```
