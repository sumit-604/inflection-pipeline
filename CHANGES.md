# CHANGES — FRAMEWORK AMENDMENT EXECUTION (Damodaran Integration)

*Operator directive of 13-Aug-2026. Executed 18-Aug-2026 on branch `claude/damodaran-framework-amendments-2wmk1z`. Every change below implements a confirmed placement directive from the operator's 56-point Damodaran integration review. No framework document was edited in place: each amended document is a new versioned copy, and the prior-version file is left untouched for history. Five decision gates were presented to the operator and only confirmed outcomes were implemented.*

---

## VERSIONS DETECTED AND TARGETED

| Document | Highest existing | New version created |
|---|---|---|
| FTTCP | v1.2 file (v1.3 content) | **v2.0** — `FTTCP_v2.0_Consolidated.md` |
| Master Project Prompt | v3.3 | **v3.4** — `Master_Project_Prompt_v3.4.md` |
| Section 1B (exit multiple authority) | v3.5.1 (Reconciliation) | **v3.6** — `Section_1B_v3_6_Amendments.md` (new amendment layer) |

No standalone valuation-framework-v4 draft exists in the repo, so the Role 1 valuation amendments (Tasks 4 and 5) were applied to the Master Project Prompt, per the directive's fallback instruction.

---

## FILES CREATED

| File | Task | Nature |
|---|---|---|
| `frameworks/Debt_Capacity_Assessment_v1_0.md` | Task 1 | New standalone section, runs before FTTCP |
| `frameworks/FTTCP_v2.0_Consolidated.md` | Task 2 | Copy of v1.2, everything preserved as PART A, PART B added |
| `frameworks/Market_Implied_Assumptions_v1_0.md` | Task 3 | New standalone section, runs after FTTCP, before Role 1 |
| `frameworks/Master_Project_Prompt_v3.4.md` | Tasks 4, 5 | Copy of v3.3, Role 1 and conclusion amended, sequence updated |
| `frameworks/Section_1B_v3_6_Amendments.md` | Gates A/B/C/D + Task 4 exit-PE mechanics | New amendment layer (Amendments 11-16) |
| `macro-sheet.md` | Task 6 | New standing monthly data sheet (repo root) |

## FILES DELIBERATELY NOT MODIFIED (left for history)

`FTTCP_v1.2_Consolidated.md`, `Master_Project_Prompt_v3.3.md`, `Section_1B_v3.3_Amendments.md`, `Section_1B_v3_5_1_Reconciliation.md`. Git confirms these carry no changes. Notion, live company theses, Decision Status fields, and all PARKED items were not touched.

---

## THE NEW PIPELINE ARCHITECTURE (implemented)

```
... Role 5 (concall) → Role 5.5 (if present) →
Debt Capacity Assessment v1.0 →
FTTCP v2.0 (PART A transition proof → PART B normalization engine) →
Market-Implied Assumptions v1.0 →
Role 1 (valuation, consumes the above) → Role 2 → Role 3
```

The sequence is stated in Master v3.4 (PIPELINE POSITION and Role 1 consumption clause) and in FTTCP v2.0 (Pipeline Position and the full-workup diagram). Debt Capacity runs before FTTCP because Module B7 consumes its output; Market-Implied runs after FTTCP because it uses Module B4 operating EPS and hands its spread to Role 1.

---

## AMENDMENTS APPLIED, BY TASK

### Task 1 — Debt_Capacity_Assessment_v1_0.md (created)

`[v1.0: new standalone Debt Capacity Assessment section, runs before FTTCP — Damodaran integration, operator directive 13-Aug-2026]`

Mid-cycle debt capacity computed on normalized (mid-cycle) EBIT at a default 3x coverage threshold, never trough or peak. States maximum debt at [3x] coverage on mid-cycle EBIT, current debt, and headroom or breach. Five-year EBIT/interest coverage trend line with direction (IMPROVING/STABLE/DETERIORATING). Output block consumed by FTTCP Module B7 and Role 1: current debt vs capacity, headroom %, coverage trend, one-line verdict COMFORTABLE / STRETCHED / BREACH. Worked-example placeholder table. Synthetic credit ratings and failure probabilities deliberately excluded (parked 3.3, 3.4).

### Task 2 — FTTCP v2.0 (amended)

`[v2.0: adds PART B Financial Normalization Engine (B1-B8) and the cyclical margin rule — Damodaran integration, operator directive 13-Aug-2026]`

The full v1.2/v1.3 protocol is preserved verbatim as PART A (four transitions, scored verdict system, Kernex principle, lender transition set, monitoring triggers, Step 2E ledger, worked examples). PART B, the Financial Normalization Engine, added with eight modules, each producing a named output Role 1 consumes:

- **B1 Reinvestment Funding Check** — funding channel per year (new reinvestment vs utilization ramp, hard capacity ceiling), pass/fail, cross-checked against the Debt Capacity verdict.
- **B2 Forward ROCE Projection vs Minimum ROCE Requirement** — ROCE path, crossover year, "growth premium eligible: YES from FY__ / NO" flag; default r 13.5% for micro/small caps where RRM r not yet computed (Gate E).
- **B3 Normalized Base-Year EPS** — reported vs normalized EPS, 📄-gated, named catalyst, self-withdrawing, single-credit with Section 1B Route B.
- **B4 Operating Earnings Separation** — operating EPS (the EPS that enters every multiple), stripped-items table; non-operating assets enter the equity bridge.
- **B5 Incentive and Tax Normalization** — PLI/SEZ/holidays with expiries; Year 3 on post-expiry economics.
- **B6 Capex, R&D and Brand Spend Restatement** — capitalize over default 5-yr life, restated ROCE/EPS line by line, single-credit route declaration with Section 1B Routes A/B.
- **B7 Post-Deleveraging Earnings Picture** — consumes the Debt Capacity output; paydown schedule, interest saving to PAT, Year 3 net debt for the EV bridge.
- **B8 Relative Convergence and Re-rating Potential** — relative position, companion-variable test, sector dislocation check, re-rating potential rating for the destination PE discussion.

Closed by the **consolidated FTTCP Part B Output Sheet** (single handoff to Role 1) and a single-credit map across Part B and Section 1B. Also added the **cyclical margin rule**: for flagged cyclical sectors, base = full-cycle average, bear = cycle trough, bull = cycle peak; the three-year-average convention is retired for flagged sectors.

### Task 3 — Market_Implied_Assumptions_v1_0.md (created)

`[v1.0: new standalone Market-Implied Assumptions section, runs after FTTCP and before Role 1 — Damodaran integration, operator directive 13-Aug-2026]`

Reverse-engineered growth (flat-multiple and reasonable-exit-PE readings, algebra shown) using FTTCP Module B4 operating EPS. The market's implied story in four to six plain sentences ("At ₹___, the market is assuming ___"). Spread statement ("Price assumes ___% growth; FTTCP evidence supports ___%. The spread is the trade."), with the PRICED-WE-ARE-LATE flag where the price already embeds the bull case. Output block consumed by Role 1 Section 1 and the conclusion.

### Task 4 — Role 1 valuation (Master v3.4)

`[v3.4: Role 1 consumption clause; exit-PE durability fade and complexity discount; growth-premium eligibility gate; Year 5 horizon; relative PE; operating earnings only — Damodaran integration, operator directive 13-Aug-2026]`

1. **Consumption clause** at the top of Role 1: consumes the Debt Capacity output, the FTTCP Part B output sheet (B1-B8), and the Market-Implied block; does not recompute them; verifies the single-credit map.
2. **Exit PE gains two inputs.** (a) Emerging Moat score maps to a **durability-of-growth fade horizon** (Expansion holds to Year 5, Strengthening fades by Year 4, Modest fades to industry by Year 3, None fades immediately), governing projections and DCF, replacing flat CAGR lines. (b) A **complexity discount**: high subsidiary count, dense RPT, or audit qualifications raise r by +0.5; complexity lives in r and nowhere else.
3. **Growth premium eligibility** from FTTCP Module B2: no Pillar 3 premium until projected ROCE crosses the minimum ROCE requirement; monitorable binary gate.
4. **Projection horizon**: model runs to Year 5 even on a 3-year hold, because the Year 3 buyer pays for Years 4-5; a name with no credible Year 4-5 story takes an exit-multiple haircut.
5. **Relative PE primacy**: destination PE also expressed as a relative PE (destination ÷ market PE) against the name's and sector's historical relative band, citing Module B8.
6. **Operating earnings only, everywhere**: the EPS entering every multiple is Module B4 operating EPS; non-operating assets enter via the equity bridge.
7. **Banks/NBFCs: no change** — P/B against ROE remains primary, lender carve-outs stand (noted explicitly in Pillar 2L).

### Task 5 — Valuation conclusion / verdict card (Master v3.4)

`[v3.4: four mandatory conclusion elements — value-vs-price, evidence-scaled MoS, dispersion-capped sizing, edge declaration — Damodaran integration, operator directive 13-Aug-2026]`

New Section 4H-pre and four verdict-card fields: (1) **value vs price statement** (two lines, using the market-implied flag); (2) **evidence-scaled margin of safety** (20% for mostly-📄 with catalyst inside 12 months, 30% mixed, 40% mostly 🎙️/🔍 or catalyst beyond 18 months), replacing the flat 20-30% band throughout; (3) **dispersion-capped sizing** (range width (Bull − Bear) ÷ Base: under 40% normal, 40-80% Medium cap, above 80% Small cap); (4) **edge declaration** (process / patience / information, default process).

### Task 6 — macro-sheet.md (created)

`[v1.0: new standing monthly macro sheet — Damodaran integration, operator directive 13-Aug-2026]`

Template with month stamp, rupee risk-free rate, CPI inflation, nominal GDP growth, equity risk premium including country risk, market-wide earnings growth, market PE (Nifty 50 and Nifty Smallcap 250), and a one-line GARP regime note. Every Role 1 run cites the latest sheet; DCF terminal growth may not exceed the sheet's nominal GDP (wired into Master v3.4 Section 3 DCF). Placed at repo root as a living monthly data sheet.

### Section 1B v3.6 amendments (exit-multiple authority for Task 4 mechanics and Gates A-D)

New file `Section_1B_v3_6_Amendments.md`, Amendments 11-16, each tagged inline. Amendment 11 (Gate D) Pillar 1 cap 30x with elite extension, superseding Amendment 5's 24x. Amendment 12 (Gates A/B/C) the three RRM r-table single-credit fixes. Amendment 13 complexity discount (+0.5 to r). Amendment 14 durability fade horizon from the EM score. Amendment 15 relative PE expression citing Module B8. Amendment 16 growth premium eligibility gate from Module B2.

---

## DECISION GATE OUTCOMES

Each gate was presented to the operator as a question; only confirmed outcomes were implemented.

| Gate | Question | Operator decision | Where implemented |
|---|---|---|---|
| **A** | Delete the +0.5 cash-conversion r-UP so Pillar 2 (0.65x) solely owns structural poor cash conversion? | **CONFIRMED — delete +0.5 from r** | Section 1B v3.6 Amendment 12A; Master v3.4 RRM section |
| **B** | Cap the cyclical r-surcharge at +0.75 where the Durability band is docked to Moderate/Unproven because of cyclicality? | **CONFIRMED — cap at +0.75** | Section 1B v3.6 Amendment 12B; Master v3.4 RRM section |
| **C** | Keep both, or single-home '<5 years listed' (Unproven durability band + the +0.75 r-UP)? | **SINGLE-HOME — drop the +0.75 r-UP; the Unproven durability band owns short-record risk** | Section 1B v3.6 Amendment 12C; Master v3.4 RRM section |
| **D** | Keep the Pillar 1 formula, cap at 30x (resolving the in-repo conflict with Amendment 5's 24x)? | **CONFIRMED — cap at 30x with the elite extension** | Section 1B v3.6 Amendment 11; Master v3.4 Pillar 1 ceiling resolution |
| **E** | Use 13.5% as the standing minimum ROCE requirement in Module B2 when the RRM r is not yet computed? | **CONFIRMED — 13.5%** | FTTCP v2.0 Module B2 |

---

## PARKED — NOT IMPLEMENTED (awaiting operator placement)

Listed verbatim so nothing is silently dropped:

> 2.2 intrinsic PE cross-check restatement, 2.4 regime stress, 2.5 sector percentile, 2.8 peer table basis consistency, 2.10 Seinfeld test placement beyond Module B8c, 3.2 bottom-up cost of equity rebuild, 3.3 synthetic credit rating, 3.4 truncation probability, 3.7 liquidity haircut (operator sign-off pending), 4.1-4.16 and 4.18-4.20 (protocol-layer items), 5.1-5.4 except the macro timer.

---

## ACCEPTANCE CHECKS

1. **Role sequence** in Master v3.4 shows Debt Capacity → FTTCP v2.0 → Market-Implied → Role 1, with cross-references updated in Master (PIPELINE POSITION, consumption clause, Section 1B intro) and in FTTCP v2.0 (Pipeline Position, full-workup diagram). PASS.
2. **FTTCP v2.0 Part B** has all eight modules (B1-B8), each with a named output, plus the consolidated output sheet. PASS.
3. **Role 1 consumption clause** present; Role 1 no longer recomputes the Debt Capacity, FTTCP Part B, or Market-Implied outputs. PASS.
4. **Conclusion** carries all four new elements (value-vs-price, evidence-scaled MoS, dispersion-capped sizing, edge declaration) in Section 4H-pre and the verdict card. PASS.
5. **Every new/amended file has a version-history entry; no prior-version file was modified.** Git status confirms only new files created. PASS.
6. **This CHANGES.md** lists every file, every amendment tag, every gate outcome, and the PARKED list. PASS.
7. **Dry-read test**: a fresh analyst reading the new documents in sequence (Debt Capacity v1.0 → FTTCP v2.0 → Market-Implied v1.0 → Master v3.4 with Section 1B v3.6, citing macro-sheet.md) can run the full pipeline without consulting any superseded version. PASS by construction; each new document states its place in the sequence and its inputs and outputs.

---

## PROPAGATION FOLLOW-UP FOR THE OPERATOR (not silently dropped)

The pipeline wrapper injects framework documents by name at run time. Its version references still point at the superseded versions and are the operator's routine promotion step, sequenced deliberately because it moves the prompt-cache boundary. When these new documents are promoted into the injection set, update:

- `prompts/11-valuation-pipeline.md` — the `{{...}}` injection markers and the version banner (currently Master v3.3 / Section 1B v3.5.1 / FTTCP v1.2), and the `framework_versions` YAML field, to add FTTCP v2.0, Master v3.4, Section 1B v3.6, the Debt Capacity Assessment, the Market-Implied Assumptions block, and macro-sheet.md.
- `frameworks/README.txt` — the "copy these files here" list and the current-version note.
- `.claude/agents/stage-11-valuation.md` — the description line naming the framework versions.
- `VERSIONING.md` "rules right now" block and a new `fw-2026-08-18` bookmark after this branch merges to main.

These are pipeline-plumbing edits, not framework-document edits, and were left for the operator per the documents-only scope of this directive. The framework documents themselves are complete and internally consistent.
