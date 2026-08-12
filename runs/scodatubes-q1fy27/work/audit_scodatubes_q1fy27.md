# A5 ADVERSARY / COMPLETENESS AUDIT — Scoda Tubes Limited (SCODATUBES), Q1 FY27

**Re-audit (loop 1) of the revised A4 review.** Fresh context: I saw only the A4 review, the A1 extract, and the A2 ledger. Every number below is re-derived independently from the raw CORRECTED extract body (L81-L112, Millions x 0.1 = Rs Crore); I did not defer to A4's or A3's cites.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

PLAIN-LANGUAGE BRIEF is present (review L430-442) with all four labelled parts, each non-empty and carrying real content:

| Part | Location | Present? | Real content? |
|---|---|---|---|
| 1. SUMMARY NARRATIVE | L432-433 | YES | Full narrative, ~1 dense paragraph covering revenue, the two-effect margin/PAT split, cash INDETERMINATE, AVOID stance. Meets 10-20 line substance. |
| 2. SECTOR INTELLIGENCE | L435-436 | YES | Import-substitution / anti-dumping, energy-cost watch, hot-pierced vs hot-extruded, tender silence. |
| 3. BUSINESS-MODEL INTELLIGENCE | L438-439 | YES | Capex-heavy model, backward integration, above/below-EBITDA stress, deferred-tax shield, cash-conversion Achilles heel. |
| 4. COMPETITION INTELLIGENCE | L441-442 | YES | Peer scale/margin/working-capital comparison (Venus, Ratnamani, Welspun), disclosure-cadence lag, promoter strength. |

**Gate 0: PASS.**

---

## AUDIT 1 — COVERAGE (independent re-enumeration vs A2 ledger)

Fresh grep/sweep of the extract body (L15-204). Zero-standing rows (L93, L97, L111) are counted inside the 25 line-items, consistent with the ledger.

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| Notes | 7 (L115,118,120,122,123,125,127) | 7 | none — all 7 extracted in A4 Step 0D | PASS |
| Line-items (value-bearing) | 25 (L81-L112 minus 7 header rows) | 25 | none — all in A4 Step 1 table | PASS |
| Zero-standing | 3 (L93,L97,L111) | 3 | none — all confirmed blank x4 periods in A4 | PASS |
| Agenda items | 1 (L38-39) | 1 | none — cited A4 preamble + Monitorables | PASS |
| Auditor paras | 4 (L158-161,162-167,169-178,179-185) | 4 | none — all cited A4 Step 0D + ledger recon | PASS |
| Entities | 1 (Note 5, L123-124) | 1 | none — Step 4A | PASS |
| Signatories | 3 (DIN L53, DIN L143, UDIN L197) | 3 | none — cited A4 preamble L51-53/L141-143/L188-197 | PASS |

Header-row exclusions (L80,84,95,100,101,108,109) re-verified as non-value category rows. Stray `*` at L145 re-confirmed as OCR seal artifact, not a note. L112 (EPS continued+discontinued) is an exact duplicate of L110 and is reviewed via L110. No orphan rows; no row my fresh pass found that the ledger lacks.

**Coverage: PASS.** No loop-back to A2 or A3.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extract, Millions; Cr = x0.1)

### 2a. Footing — all four columns on the five identities (independently recomputed)

| Column | Total Income | Total Expenses | PBT | PAT | TCI |
|---|---|---|---|---|---|
| Q1FY27 | 1243.45+16.30=**1259.75** ✓ | 1001.65−156.14+24.62+64.81+41.31+213.53=**1189.78** ✓ | 1259.75−1189.78=**69.97** ✓ | 69.97−6.25−11.22=**52.50** ✓ | 52.50+1.71−0.43=**53.78** ✓ |
| Q4FY26 | 1235.69+44.03=**1279.72** ✓ | 1007.73−183.41+26.34+81.39+36.12+217.98=**1186.15** ✓ | =**93.57** ✓ | 93.57−25.72−4.66=**63.19** ✓ | 63.19−1.47+0.37=**62.09** ✓ |
| Q1FY26 | 974.17+17.61=**991.78** ✓ | 742.49−52.47+24.20+51.04+15.72+118.05=**899.03** ✓ | =**92.75** ✓ | 92.75−18.90−3.02=**70.83** ✓ | 70.83+1.47−0.37=**71.93** ✓ |
| FY26 | 5186.50+105.71=**5292.21** ✓ | 4143.75−611.44+104.54+248.66+92.17+787.21=**4764.89** ✓ | =**527.32** ✓ | 527.32−116.33−22.56=**388.43** ✓ | 388.43+1.18−0.30=**389.31** ✓ |

**20/20 footing checks reproduce.** Exceptional items nil all periods (L93). The corrected grid stands.

### 2b. Derived metrics in A4

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 (PBT+D+Fin−OI) | 15.979 | (69.97+41.31+64.81−16.30)/10=15.979 | L94,89,88,82 | PASS |
| Op EBITDA Q1FY26 | 14.190 | (92.75+15.72+51.04−17.61)/10=14.190 | L94,89,88,82 | PASS |
| Op EBITDA margin Q1FY27 | 12.85% | 159.79/1243.45=12.851% | L81 | PASS |
| Op EBITDA margin Q1FY26 | 14.57% | 141.90/974.17=14.566% | L81 | PASS |
| Reported EBITDA Q1FY27 / margin | 17.609 / 14.16% | 176.09 / 176.09÷1243.45=14.162% | L94,89,88,81 | PASS |
| Core PBT ex-OI (all cols) | 5.367/4.954/7.514/42.161 | 53.67/49.54/75.14/421.61 Mn | L94,82 | PASS |
| Other Income / PBT | 23.3/47.1/19.0/20.0% | 23.30/47.05/18.99/20.05% | L82,94 | PASS |
| Effective tax rate | 24.97/32.47/23.63/26.34% | 17.47/30.38/21.92/138.89 ÷ PBT | L96,98,94 | PASS |
| Current-tax share of PBT | 8.93/27.49/20.38/22.06% | 6.25/25.72/18.90/116.33 ÷ PBT | L96,94 | PASS |
| PAT margin | 4.22/5.11/7.27/7.49% | 52.50/63.19/70.83/388.43 ÷ Rev | L99,81 | PASS |
| Revenue YoY | +27.64% | 1243.45/974.17−1=27.641% | L81 | PASS |
| Op EBITDA YoY | +12.61% | 159.79/141.90−1=12.607% | derived | PASS |
| Op EBITDA margin YoY | −172 bps | 14.566−12.851=−1.715 pp | L81 | PASS |
| Depreciation YoY | +162.8% | 41.31/15.72−1=162.85% | L89 | PASS |
| Finance YoY | +26.98% | 64.81/51.04−1=26.98% | L88 | PASS |
| EBIT (OpEBITDA−D) YoY | −6.10% | 118.48/126.18−1=−6.10% | derived | PASS |
| Core PBT ex-OI YoY | −28.57% | 53.67/75.14−1=−28.57% | L94,82 | PASS |
| Reported PBT YoY | −24.56% | 69.97/92.75−1=−24.56% | L94 | PASS |
| PAT YoY | −25.88% | 52.50/70.83−1=−25.88% | L99 | PASS |
| EPS YoY | −38.89% | 0.88/1.44−1=−38.89% | L110 | PASS |
| Other Expenses YoY | +80.9% | 213.53/118.05−1=80.88% | L90 | PASS |
| **Margin decomp — net material** | 70.83%→68.00%, −283 bps | 690.02/974.17=70.83%; 845.51/1243.45=68.00% | L85,86,81 | PASS |
| **Margin decomp — employee** | 2.484%→1.980%, −50 bps | 24.20/974.17; 24.62/1243.45 | L87,81 | PASS |
| **Margin decomp — other exp** | 12.117%→17.173%, +505 bps | 118.05/974.17; 213.53/1243.45 | L90,81 | PASS |
| Decomp reconciliation | +283+50−505=−172 bps | reconciles exactly | — | PASS |
| Revenue QoQ | +0.63% | 1243.45/1235.69−1=0.628% | L81 | PASS |
| PAT QoQ | −16.92% | 52.50/63.19−1=−16.92% | L99 | PASS |
| Δinv build YoY | +198% | 156.14/52.47−1=197.6% | L86 | PASS |
| PAT bridge (all legs) | see below | reproduced leg-by-leg | L81-99 | PASS |

**PAT bridge recomputed leg-by-leg:** gross profit +11.379 (39.794 vs 28.415), employee −0.042, other expenses −9.548 → Op EBITDA change +1.789; depreciation −2.559; finance −1.377; other income −0.131 → PBT change −2.278; current tax +1.265; deferred tax −0.820 → total tax +0.445; exceptional 0.000 → **PAT change −1.833** (5.250−7.083). Every leg reproduces.

**Arithmetic result: no mismatch above rounding in any derived metric, any table, or the bridge.**

**One minor non-gating imprecision (noted, not a gate failure):** Step 4 (review L229) states the Q1FY27 deferred-tax charge is "16.0% of PBT, ~1,624 bps." The governing figure 16.0% is correct (11.22/69.97 = 16.04%), but 16.04% = ~1,603 bps, not 1,624. This is a parenthetical restatement of a correct number, affects no table cell, no verdict, and no downstream figure. Flagged for A4 to tidy while it makes the graft below; it does not itself fail the gate.

---

## AUDIT 3 — ADVERSARIAL READ

### Prior-loop counter (Other Expenses driver) — VERIFICATION

The prior A5 loop's surviving counter was that the −172 bps operating-EBITDA margin miss was mis-diagnosed as a below-EBITDA (depreciation/finance) event, when it is an above-EBITDA event driven by **Other Expenses +80.9% YoY (L90)**. I independently reproduce the decomposition: **net material +283 bps, employee +50 bps, other expenses −505 bps = −172 bps** (exact). I confirm A4 has now incorporated it in full:
- Step 2 decomposition table (L143-148) and corrected read (L155, L161).
- Summary-narrative attribution corrected to the Other-Expenses driver (L433).
- Management question **Q9** added (L385).
- Monitorable "Other Expenses / revenue ratio normalising <~13%" added (L415).
- Flags updated (L490-491), verdict paragraph corrected (L426).

**This counter is RESOLVED.** No further loop-back on it.

### Three most positive A4 claims, strongest bear counter for each

**Claim 1 (positive): Revenue +27.6% YoY — "the one genuinely good number," lands at/above base (L154, L127).**
Counter (from extract): revenue is essentially FLAT sequentially, +0.63% QoQ vs Q4FY26 (1243.45 vs 1235.69, L81), while depreciation +162.8% (L89) proves the new plant is already capitalised. A commissioned plant that does not lift the run-rate above the pre-commissioning quarter is the named capex red-flag; the YoY figure is lapping a soft Q1FY26 base, not evidence of live acceleration.
**Status: DOES NOT SURVIVE as unaddressed** — A4 already grafts this (Step 3 plateau/red-flag L182, monitorables, growth-trigger "DELAYED"). No action.

**Claim 2 (positive): Absolute Operating EBITDA still GREW +12.6% / +Rs1.789 Cr on volume (L212, L155).**
Counter: (a) the +1.789 Cr gain is more than consumed below EBITDA by depreciation −2.559 + finance −1.377 = −3.936 Cr, producing PAT −25.9% — A4 fully incorporates this (Step 4 bridge). (b) Part of the absolute EBITDA growth is a **cost-deferral artifact of the inventory build** (see Claim 3) — NOT incorporated.
**Status: PARTIALLY SURVIVES → merges into Claim 3.**

**Claim 3 (positive): "Genuinely favourable +283 bps gross-material improvement" (net material 70.83%→68.00%); the cost problem is confined to Other Expenses, "not a raw-material disadvantage, since Scoda's material ratio actually improved" (L145, L150, L154, Step 4 "recurring" L209/L211, Competition intel L442).**

Counter (SURVIVING, extract-supported, L81/L85/L86):
The +283 bps "net material" improvement is **not a unit-economics gain — it is entirely an inventory-build (cost-deferral) artifact.** Net material cost = raw material consumed (L85) + changes in FG/WIP inventories (L86). Decomposing the two components as a % of revenue:
- **Raw material actually CONSUMED / revenue ROSE +433 bps**: Q1FY26 742.49/974.17 = 76.22% → Q1FY27 1001.65/1243.45 = 80.55%.
- The **FG/WIP inventory-build credit tripled, from 5.39% to 12.56% of revenue (+717 bps favourable)**: Q1FY26 52.47/974.17 → Q1FY27 156.14/1243.45.
- Net: +433 − 717 = **−283 bps** (reconciles exactly to A4's figure).

So the "favourable material economics" is production outrunning sales: Rs15.6 Cr of FG/WIP was built (L86), deferring conversion cost onto the balance sheet and flattering current-period gross margin and absolute EBITDA. Underlying raw-material efficiency per rupee of revenue **deteriorated**. Critically, **this is the SAME inventory build A4 flags as the negative cash-conversion signal** (Step 5, L245/L258, "+198% YoY inventory build, pointing the wrong way for CFO"). A4 treats it as a virtue in Step 2/Step 4/Competition and as a vice in Step 5 without reconciling the two — they are one event.

Why it is material (not cosmetic): three A4 conclusions rest on the material improvement being genuine — (i) Step 2's "genuinely favourable +283 bps" framing (L150/L154); (ii) Step 4's classification of the +11.379 Cr gross-profit gain as "Recurring" (L209/L211); (iii) the Competition-intelligence claim that the peer-gap widening "is not a raw-material disadvantage since Scoda's material ratio actually improved" (L442). All three are undercut once the improvement is shown to be an inventory-capitalisation artifact tied to the cash-conversion red flag.

**Status: SURVIVES. Must be grafted into A4 before save. Loop back to A4.**

Required graft: in Step 2, Step 4B, and the Competition-intelligence brief, qualify the +283 bps net-material improvement as substantially an FG/WIP inventory-build (cost-deferral) effect — raw material consumed per revenue rupee rose +433 bps, the build credit rose +717 bps (5.4%→12.6% of revenue), net −283 bps — and note it is the same Rs15.6 Cr build (L86) flagged as the negative cash-conversion proxy; reclassify the gross-profit gain from unqualified "Recurring" to "recurring-but-inventory-inflated (verify at H1 when the balance sheet/CFO arrive)"; and add/extend a management question and monitorable on FG/WIP inventory build vs dispatch (does gross margin hold once production and sales re-align).

### New independent scan beyond the three claims
No further surviving counter found. The deferred-tax shield (F8-1), single-segment non-disclosure (trigger 8), EPS/share-base non-reconciliation (F10-1), and INDETERMINATE cash are all already surfaced as flags/questions. The inventory-build-vs-material-margin counter above is the one genuinely new, unincorporated, extract-supported bear point.

---

## VERDICT

**INCOMPLETE.** Deliverable gate PASS, coverage PASS, arithmetic PASS (one non-gating parenthetical bps imprecision noted). The adversarial read surfaces one NEW surviving bear counter that A4 has not incorporated: A4's "genuinely favourable +283 bps gross-material improvement" (relied on in Step 2, Step 4B, and the Competition brief) is substantially an FG/WIP inventory-build cost-deferral artifact — raw material consumed per revenue rupee actually rose +433 bps, and the −283 bps net gain is created entirely by the tripled inventory build (5.4%→12.6% of revenue, L86), which is the same build A4 flags as the negative cash-conversion signal. This must be grafted before save.

**Loop back to: A4.**

```yaml
stage: A5-adversary
company: "SCODATUBES"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE             # COMPLETE | INCOMPLETE
plain_language_brief:           # hard gate — all four present
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: []               # none — every ledger row cited in A4
  missing_from_ledger: []       # none — fresh enumeration matched A2 exactly
arithmetic_mismatches: []       # no derived-metric mismatch above rounding; footing 20/20 reproduced
                                # (note: Step 4 "~1,624 bps" is an imprecise restatement of the correct 16.0% of PBT (~1,603 bps) — non-gating parenthetical, tidy during graft)
surviving_bear_counters:
  - claim: "Genuinely favourable +283 bps gross-material improvement; cost problem confined to Other Expenses, 'not a raw-material disadvantage since Scoda's material ratio actually improved' (Step 2 L145/L150/L154, Step 4B 'Recurring' L209/L211, Competition brief L442)"
    counter: "The +283 bps net-material gain is an FG/WIP inventory-build cost-deferral artifact, not a unit-economics improvement. Raw material CONSUMED per rupee of revenue ROSE +433 bps (76.22%->80.55%); the net gain comes entirely from the tripled FG/WIP build credit rising +717 bps (5.39%->12.56% of revenue). Production outran sales, deferring conversion cost onto the balance sheet and flattering current-period gross margin and absolute EBITDA. This is the same Rs15.6 Cr build A4 flags as the negative cash-conversion proxy (Step 5) — one event scored as both a virtue and a vice without reconciliation. Undercuts the 'genuinely favourable' framing, the 'Recurring' gross-profit label, and the Competition claim that the peer-gap widening is not a raw-material issue."
    source_line: "L85 (RM consumed), L86 (change in FG/WIP inventories), L81 (revenue)"
loop_back_to: "A4"
gap: "Graft the inventory-build (cost-deferral) qualification of the +283 bps net-material improvement into Step 2, Step 4B, and the Competition-intelligence brief: state that RM consumed/revenue rose +433 bps while the FG/WIP build credit rose +717 bps (5.4%->12.6% of revenue, L86) for a net -283 bps; note it is the SAME Rs15.6 Cr build flagged as the negative cash-conversion proxy (Step 5); reclassify the +11.379 Cr gross-profit gain from unqualified 'Recurring' to inventory-inflated pending H1 CFO/balance-sheet; add a management question + monitorable on FG/WIP build vs dispatch and whether gross margin holds once production and sales re-align. Also tidy the '~1,624 bps' parenthetical to ~1,603 bps (16.0% of PBT)."
```
