# B12c — VERIFIER C: FRAMEWORK ADHERENCE (Phase 1 scope)
Company: Gaudium IVF and Women Health Ltd (GAUDIUMIVF) | Run date: 2026-07-16
Model: claude-opus-4-8 | Emits: B12c

SCOPE NOTE: This is the PHASE 1 pass. Only Gate 0 (B01) and Emerging Moat
(B07) framework-adherence checks were run. The valuation-adherence audit
(B10/B11) is DEFERRED to PHASE 3 — those reports do not exist yet, so the
valuation section below is `pending-phase-3` and is excluded from the
acceptance-rate arithmetic. `framework_adherence` is computed from the
Gate 0 + Emerging Moat rule set only.

I audited RULE APPLICATION, not company quality and not raw source-number
accuracy (Verifier A owns numbers). Where I re-derived a figure it was
only to confirm the correct scoring BAND / multiplier was selected.

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE
═══════════════════════════════════════════════════════════════════

Framework: prompts/01-gate-0-pipeline.md. Data window declared: 4 years
FY23–FY26, consolidated. Opening line format honoured ("Data available:
4 years (FY2023 to FY2026)... Scoring adapted to 4-year history"). PASS.

### Block A — Return on Capital
| Rule | Maker value | Band applied | Re-derivation | Verdict |
|---|---|---|---|---|
| A1 Median RoCE | median{20.11,38.74,39.37,54.40}=39.06% | ≥25→5 | (38.74+39.37)/2=39.055 ✓ | PASS |
| A2 Min single-yr RoCE | 20.11% | ≥15→5 | ✓ | PASS |
| A3 Median RoE | median{16.08,38.23,41.31,59.51}=39.77% | ≥20→5 | (38.23+41.31)/2=39.77 ✓ | PASS |
| A4 RoCE trend | FY26 20.11 vs FY23 54.40 = −34.29pp | >5pp decline→0 | ✓; denominator-effect noted but NOT used to override score | PASS |
Block A = 5+5+5+0 = 15/20. PASS.

BASIS NOTE (MINOR): RoCE/RoE use the RHP's own KPI definitions (RoCE
denominator = NW+Borrowings+Lease+DTL; RoE = PAT÷closing NW) rather than
the framework's default formulas (RoCE = EBIT÷(Total Assets−Current
Liab.); RoE = PAT÷**average** net worth). The framework permits using a
source's own ratio when screener is unpopulated ("use the source's
figure"), and the screener CSVs were exported empty — so the substitution
is source-permitted and transparently disclosed. It does not change any
band: A3 remains 5 on either basis (average NW is lower than closing for a
growing book, pushing RoE higher, still ≥20). Logged as MINOR advisory,
not a scoring fail.

### Block B — Cash Generation Quality
| Rule | Maker value | Band | Re-derivation | Verdict |
|---|---|---|---|---|
| B1 CFO/PAT | 4325.88/6745.82=64.1% | 0.50–0.69→1 | 0.6412 ✓ | PASS |
| B2 FCF-positive yrs | 3/4=75% (FY25 −16.08 neg) | 75–99→4 | ✓ | PASS |
| B3 Cum FCF/PAT | 961.83/6745.82=14.3% | <0.20→0 | 0.1426 ✓ | PASS |
| B4 ΔWC days | 11.32→156.33 = +145.0 | >15↑→0 | ✓ | PASS |
Block B = 1+4+0+0 = 5/20. Deal-breaker #2 (Block B<8→max GOOD) correctly
triggered. PASS.

### Block C — Growth
| Rule | Maker value | Band | Re-derivation | Verdict |
|---|---|---|---|---|
| C1 Rev CAGR 3yr | (2.3591)^⅓−1=33.12% | ≥20→5 | 33.13% ✓ (rounding) | PASS |
| C2 PAT CAGR 3yr | (1.8106)^⅓−1=21.89% | ≥20→5 | 21.88% ✓ | PASS |
| C3 Positive YoY yrs | 3/3=100% | →5 | ✓ | PASS |
| C4 PAT−Rev CAGR | 21.89−33.12=−11.23pp | <−8pp→0 | ✓ | PASS |
Block C = 5+5+5+0 = 15/20. PASS. CAGR edge rules: no negative/zero
endpoints, no loss-to-profit swing — correctly recorded as none in
data_notes. PASS.

### Block D — Balance Sheet Strength
| Rule | Maker value | Band | Re-derivation | Verdict |
|---|---|---|---|---|
| D1 NetDebt/EBITDA | (2307.48−878.57)/3770.39=0.379x | 0–1.0x→4 | ✓; near-cash NOT credited to force net-cash (conservative, correct) | PASS |
| D2 Int coverage | 3568.72/349.16=10.22x | ≥10→5 | ✓ | PASS |
| D3 Debt/Equity | (2307.48+149.54)/15230.21=0.161x | 0.1–0.5→4 | borrowings-only 0.151x, same band ✓ | PASS |
| D4 Current ratio | 7330.20/3852.73=1.90x | 1.5–1.99→4 | ✓ | PASS |
Block D = 4+5+4+4 = 17/20. PASS.

### Block E — Shareholder Alignment
| Rule | Maker value | Band | Re-derivation | Verdict |
|---|---|---|---|---|
| E1 Promoter holding | 71.30% (RHP post-offer indic.) | ≥60→5 | ✓; no post-listing Reg.31 filing — flagged input gap, proxy disclosed | PASS |
| E2 Holding change | 99.98%→71.30% = −28.68pp | dec >3%→0 | ✓ literal formula; IPO-artifact noted but NOT used to override | PASS |
| E3 Pledge | 0% | 0%→5 | ✓ | PASS |
| E4 ContLiab/NW | 3141.78/15230.21=20.63% | 15–30→1 | 0.2063 ✓ | PASS |
Block E = 5+0+5+1 = 11/20. PASS.

CORE = 15+5+15+17+11 = 63. ✓

### Block F — Quantitative Moat (12 tests)
| Test | Score | Band logic | Verdict |
|---|---|---|---|
| M1 Pricing power | 0 | margin −9.23pp exceeds −2/−5 band → else 0 | PASS |
| M2 Cost adv. | 5 | 40.25% vs peer median 16.34% (=median{6.05,26.63}) → +23.9pp ≥5pp | PASS |
| M3 Cap. efficiency | 5 | FAT 13.98x>3x AND RoCE 20.11%>20% (boundary, literally >20) | PASS |
| M4 Cust. stickiness | 0 | 0 decline yrs but receivables unstable; lower bands require decline yrs → conservative 0 | PASS |
| M5 Scale/dominance | 0 | PEER DATA NEEDED (no Indian listed peer) — correct per rule | PASS |
| M6 Tech/R&D | 0 | no R&D/Rev disclosed; not estimated | PASS |
| M7 Regulatory | 1 | regulated but >10 players | PASS |
| M8 Distribution | 3 | network growing AND rev CAGR ≥15; rev/outlet not computable so not 5 | PASS |
| M9 Brand | 0 | PEER DATA NEEDED (no comparable GM peer) | PASS |
| M10 Switching costs | 0 | grew every yr but receivables +179d ≫10; else 0 | PASS |
| M11 Network effects | 1 | <6yr, conservative; CAGR>15 but selling% not clearly declining | PASS |
| M12 Neg WC/float | 0 | 3/4 yrs >45d → >45 band | PASS |
Moat score = 0+5+5+0+0+0+1+3+0+0+1+0 = 15/60. ✓
Moats present ≥3: M2,M3,M8 = 3. Classification 2–3 → MODERATE. PASS.

CONSISTENCY NOTE (MINOR, not a fail): M2 credits a foreign-peer EBITDA
comparison (score 5) while M5/M9 mark PEER DATA NEEDED for
scale/gross-margin. This is defensible — the RHP peer table supplies an
EBITDA-margin datapoint (so M2 has provided data), whereas Indian
market-share and like-for-like gross-margin peers genuinely do not exist.
The differential treatment follows the "score 0 only if peer data is NOT
provided" rule. PASS with note.

### Classification chain
- Grand total 63+15 = 78 ✓
- Base matrix: Core 63 (60–79) + MODERATE → "Core 60–79 + else = GOOD" ✓
- Deal-breakers: #2 triggered (max GOOD); all others correctly ruled
  not-triggered; #9 (history<3) correctly not triggered at 4 yrs ✓
- Data confidence: 4 yrs → "3–4 LIMITED, downgrade one tier" → GOOD→AVERAGE ✓
- Final: AVERAGE; history_downgrade: true ✓
- No exit PE, no round-number default, no Section 1B multiple leaked at
  this stage — confirmed ABSENT (correct; none should exist pre-valuation) ✓

GATE 0 VERDICT: fully compliant. 39 rules checked, 0 scoring fails.
Two MINOR advisories logged (RoCE/RoE source-basis substitution; M2/M5/M9
peer-data asymmetry) — neither changes a score, band, or the AVERAGE
classification. Recomputed classification CONCURS: AVERAGE.

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE
═══════════════════════════════════════════════════════════════════

Framework: prompts/07-emerging-moat-pipeline.md.

| Rule | Check | Verdict |
|---|---|---|
| All 21 categories addressed or NO EVIDENCE | A1–A4,B1–B3,C1–C2,D1–D2,E1–E2,F1–F2,G1–G2,H1–H3 (20) + R1 in §4 = 21, all present in summary table | PASS |
| Evidence taxonomy 📄/🎙️/🔍 applied per item | Applied granularly (e.g. IVF 2.0 launch 📄 vs +8-9% outcome 🎙️; IPO-note items labelled 📄 "within RHP chain" with explicit caveat) | PASS |
| Evidence multipliers 📄1.0/🎙️0.7/🔍0.5 | A2 1×0.7=0.7; A3 2×0.7=1.4; E1 1×0.7=0.7; E2 2×0.7=1.4; G1 4×1.0=4.0; H1 1×0.5=0.5; H2 3×0.85(blended)=2.55; R1 2×0.7=1.4 | PASS |
| Raw L×I matrix values | LL=1,MM=2,LM=1,HH=4,HM=3 all correct | PASS |
| Adjusted total arithmetic | 0.7+1.4+0.7+1.4+4.0+0.5+2.55+1.4 = 12.65 → 13 | PASS |
| Classification band | 12–24 → MODEST MOAT DEVELOPMENT ✓ | PASS |
| Completionist recount performed & stated | "📄 recount performed: 4 documented items across 3 categories" present | PASS |
| Active categories within 3–6 base rate, not inflated | 3 active (G1,H2,R1); Weak-Moderate rows (A3,E2,H1) conservatively EXCLUDED from active count | PASS |
| No 🎙️-only category scored as 📄 | Only G1 gets 1.0x (genuine 📄 audited BS); H2 blended has real 📄 leg; R1 weighted 0.7 | PASS |
| One-improvement-one-mechanism (no double credit) | GAAT scored once under A2; D1 explicitly folded to A2; IVF 2.0 AI scored under H2 not D1 | PASS |
| 2C capex-embedded-growth arithmetic shown | ₹25cr × 14.0x = ₹350cr ≈ +335% (350/104.36); correctly flagged not-decision-useful, hub-count proxy +271% offered | PASS |
| Optionality register present (0/🎙️/🔍 items, watched not scored) | 8-row table with converting-evidence + first-appears + window | PASS |
| 6D combined classification reasoning | AVERAGE; HIGH-POTENTIAL/TURNAROUND transition logic explicitly reasoned and correctly declined (no EXPANSION-level forward) | PASS |
| **Closing YAML block emitted** | **ABSENT — report ends at the "Input gaps carried forward" line with NO fenced `stage: B07-emoat` block** | **FAIL (MAJOR)** |

FINDING (MAJOR) — B07 missing required YAML block. The framework OUTPUT
spec mandates the report "end with exactly this fenced YAML block," and
CLAUDE.md defines a stage as "done" only when "full report written AND
valid YAML block emitted." The block is the machine-readable handoff that
feeds downstream Pillar 3 inputs (em_score, active_categories,
evidence_mix, catalysts_12m, capex_embedded_growth_pct,
optionality_register, combined_assessment). All of this content exists in
the prose, so the analysis itself is intact and no destination value is
altered — but the structured handoff a downstream stage would ingest is
missing. Rated MAJOR (broken deliverable / handoff), not CRITICAL (no
decision or number changes) and not MINOR (more than cosmetic).

EMERGING MOAT VERDICT: analytically compliant and unusually disciplined on
evidence tiering (no claim inflated to documented; active count of 3 sits
honestly at the low end of the 3–6 base rate; double-crediting explicitly
guarded). One MAJOR structural fail: the closing YAML block is absent.
13 rules checked, 1 fail.

═══════════════════════════════════════════════════════════════════
## PART 3 — VALUATION (B10/B11)
═══════════════════════════════════════════════════════════════════

DEFERRED to PHASE 3. B10 and B11 do not exist yet. Section 1B v3.3 is the
sole exit-multiple authority and is NOT applied in this pass. No Pillar
formula, UA multiplier, Hurdle Ratio, dual-track, or destination-PE audit
was performed. `valuation: pending-phase-3`.

═══════════════════════════════════════════════════════════════════
## SUMMARY
═══════════════════════════════════════════════════════════════════

- Gate 0 (B01): 39 rules checked, 0 scoring fails. Recomputed
  classification CONCURS — AVERAGE, moat MODERATE, core 63, grand total
  78. No exit multiple / round-number leak. 2 MINOR advisories.
- Emerging Moat (B07): 13 rules checked, 1 MAJOR fail (missing closing
  YAML block). Evidence discipline and completionist guard fully honoured;
  active categories not inflated. Recomputed EM classification CONCURS —
  MODEST (13/80).
- Valuation: pending Phase 3.
- framework_adherence (Gate0 + EM only) = 52 passed / 53 checked = 98%.
- No CRITICAL. The single MAJOR is structural (deliverable completeness),
  does not change any score or the AVERAGE / MODEST destinations, and is
  well above the 60% REWORK floor.

```yaml
stage: B12c
company: "GAUDIUMIVF"
run_date: "2026-07-16"
model: claude-opus-4-8
status: complete
gate0: {rules_checked: 39, fails: []}
emoat:
  rules_checked: 13
  fails:
    - "B07 closing YAML block (stage: B07-emoat) NOT emitted; report ends at 'Input gaps carried forward'. Required by framework OUTPUT spec and CLAUDE.md 'done' definition; breaks machine-readable Pillar-3 handoff (em_score, active_categories, catalysts_12m, capex_embedded_growth_pct, optionality_register). Content present in prose; no value changed. MAJOR."
valuation: pending-phase-3
framework_adherence: 98            # gate0 + EM only; 52 passed / 53 checked
recomputed_destination_pe: ""      # concur (valuation deferred to phase 3)
recomputed_decision: ""            # concur: Gate0 AVERAGE, EM MODEST both stand
findings:
  - {severity: "MAJOR", location: "B07 §OUTPUT / end of report", claim: "B07-emoat closing YAML block required by framework", finding: "block absent; downstream structured EM handoff missing", recompute: "none — prose content intact, no score/decision change"}
  - {severity: "MINOR", location: "B01 Block A", claim: "RoCE/RoE per stated framework formulas", finding: "RHP KPI definitions used (RoCE denom NW+Borrow+Lease+DTL; RoE closing NW) instead of framework defaults; source-permitted as screener CSVs empty; A3 band unchanged", recompute: "A3=5 on either basis"}
  - {severity: "MINOR", location: "B01 Block F M2/M5/M9", claim: "peer-dependent moat tests", finding: "M2 credits foreign-peer EBITDA (score 5) while M5/M9 mark PEER DATA NEEDED; defensible under 'score 0 only if peer data not provided' but asymmetric", recompute: "no change; moat count stays 3"}
critical_count: 0
major_count: 1
minor_count: 2
acceptance_rate: 98                # rules passed / rules checked, gate0+EM only
coverage_note: "Phase 1 scope: Gate 0 (B01) + Emerging Moat (B07) only. Valuation (B10/B11) deferred to Phase 3, excluded from acceptance_rate. Audited rule application, not raw-number accuracy (Verifier A) nor company quality."
```
