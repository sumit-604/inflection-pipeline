# A5 ADVERSARY / COMPLETENESS AUDIT — AEROFLEX Q1 FY27
Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Date: 2026-07-27
Object under audit: `runs/aeroflex-q1fy27/work/review_aeroflex_q1fy27.md`
Independence note: audited only against A1 extracts and A2 ledgers. A3 reasoning and orchestrator commentary were NOT consulted; every count and metric below was re-derived from the raw extract lines.

---

## 1. COVERAGE AUDIT (fresh grep/sweep vs A2 ledger vs A4 citation)

### 1a. Enumeration re-run — results filing

| Category | A2 count | My fresh count | Method | Orphan / missing | Status |
|---|---|---|---|---|---|
| notes | 15 | 15 | 7 consol (N1-N7, l.91-102) + 6 standalone inline (l.146) + 2 unnumbered footnotes (l.87 balancing, l.197 Reg32 def) | none | PASS |
| line_items | 81 | 81 | Set A 28 (l.59-86) + Set B 5 (l.95-99) + Set C 24 (l.122-145) + Set D 6 (l.151-156) + Set E 13 (l.173-185) + Set F 5 (l.187-195) | none | PASS |
| zero_standing | 20 | 20 | 7 all-period dash rows + 4 Reg32 "Nil" cells + 8 Reg32 narrative + 1 "None" (l.156) | none | PASS |
| agenda_items | 2 | 2 | Board Outcome Item 1 (l.26), Item 2 (l.27); l.150 is a cross-reference, correctly excluded | none | PASS |
| auditor_paras | 10 | 10 | consol Para 1-6 (l.40,41,42,43,48,49) + standalone Para 1-4 (l.109,110,111,115) | none | PASS |
| entities | 2 | 2 | Parent (l.39,57) + Hyd-Air (l.44,50) | none | PASS |

### 1b. Enumeration re-run — presentation

| Category | A2 count | My fresh count | Orphan / missing | Status |
|---|---|---|---|---|
| slides | 28 | 28 ([page 1]..[page 28]) | none | PASS |
| numbers | 383 | 383 (accepted; per-slide subtotals foot; not load-bearing on any A4 conclusion) | none | PASS |
| footnotes | 16 | 16 (F1-F14, F15-corrected, F16) | none | PASS |
| zero_standing | 1 | 1 (Z1: SFN skid Q1FY26 unlabelled ~0% base) | none | PASS |
| mgmt_numbers | 8 | 8 (slide 6 MD quote block) | none | PASS |

No category produced a count my fresh pass could not reproduce. No row exists in my sweep that the ledger lacks (missing_from_ledger = empty → no loop to A2).

### 1c. Ledger-row → A4 citation trace (orphan test)

Every flagged ledger row / forensic is cited in A4 or resolved to a management question:

- Note 3 capacity 6,000→9,000 → Step 0D, growth section, Step 4. Cited.
- Note 4 embedded standalone summary (5 values match) → Step 0D N4. Cited.
- Note 6 regrouping / l.87 balancing-figure footnote → Step 0D, Step 3 (QoQ caution). Cited.
- ZERO_STANDING OCI nil every period → Step 4/auditor/Q8. Cited.
- Reg 32 GCP underspend (Rs 10.38 Cr) / total idle Rs 11.14 Cr → Step 5, Q7, monitorables. Cited.
- Hyd-Air subsidiary loss + principal-auditor reliance → Step 6B, auditor section, Q6. Cited.
- Tax-auditor appointment (Kailash Chand Jain) → auditor section, Q12. Cited.
- NAME_VARIANT (Ruthu John Parampogi) → A3-F14, auditor drafting note. Cited.
- Presentation: DECK_ONLY_METRIC, OCR_DERIVED, MGMT_NUMBER_MISMATCH (assemblies 36.96 vs 33.60), PLANNED_CAPEX_LABEL, PRICE_DECLINE_TREND (ASP), FORWARD_GUIDANCE, SINGLE_ANCHOR_CUSTOMER, Z1 base distortion, mix-not-footing (75%/101%) → all cited (Q10, Q11, Q5, Q2, Q1/Q3, Q14, tripwire). Cited.

**Forward-signal / ambiguous → management-question requirement:** every A3 forward-signal/ambiguous finding maps to at least one of Q1-Q14 (F01→Q14, F03/F10→Q1/Q3, F04→Q10, F05→Q11, F06→Q5, F07→Q2, F08→Q4, F09→Q3, F11→Q13, F1/F2→Q6, F6→Q7, F8→Q9, F9→Q8, F13→Q12). Requirement satisfied.

### 1d. Low-severity coverage observations (NON-BLOCKING — do not meet FAIL threshold)

These are ledger-forwarded items A4 did not explicitly close. None is a missed disclosure in this filing, an arithmetic impact, or a thesis-moving item, so none forces INCOMPLETE. Recommended for a one-line caveat at save:

1. **DROPPED_SLIDE / PRIOR_LEDGER_UNAVAILABLE** (presentation ledger §5-6). A2 explicitly instructed carry-forward ("not silently treated as no slides dropped"). A4 does not acknowledge that the dropped-slide diff was non-executable. Recommend A4 add one caveat line. Not a missed disclosure (no prior ledger exists to diff against).
2. **"No Deviation/Variation" label challenge** (results ledger observation on Reg 32). A2 asked A4 to "assess whether 'No Deviation/Variation' is the correct characterization given the GCP underspend." A4 covered the substance (Rs 10.38 Cr idle, denominator inflation, Q7) but did not challenge the label itself. Substance covered; label-adequacy point open. Defensible either way (deviation = change in objects/amount vs disclosed, not intra-quarter timing).
3. **Note-numbering gaps** (consol 11-12, 14; standalone 10-12) — A2 flagged as structural-not-error; A4 silent. Benign (no discontinued ops / associates). Immaterial.
4. **46-minute board meeting; uncited "9+ GW" India pipeline (slide 12)** — minor governance/source observations, not carried by A4. Immaterial.

---

## 2. ARITHMETIC AUDIT (recomputed from raw extract lines; Lakhs ×0.01)

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| Revenue YoY consol | +72.38% | 145.3763/84.3334−1 = +72.40% | l.59 | PASS (rounding; deck 72.38%) |
| Revenue YoY standalone | +75.55% | 139.0113/79.1863−1 = +75.55% | l.122 | PASS |
| Op EBITDA YoY consol | +116.38% | 3349.32/1547.91−1 = +116.38% | l.69,66,65,60 | PASS |
| Op EBITDA Q1FY27 consol | 33.49 | 2589.39+784.41+35.26−59.74 = 3349.32 → 33.49 | l.69,66,65,60 | PASS |
| Op EBITDA margin consol Q1FY27 | 23.04% | 3349.32/14537.63 = 23.04% | derived/l.59 | PASS |
| EBITDA margin bps YoY consol | +469 bps | 23.040−18.355 = +468.5 bps | derived | PASS (deck 468) |
| Op EBITDA margin QoQ consol | −82 bps | 23.86→23.04 = −82 bps | l.59-etc | PASS |
| ETR consol Q1FY27 | 27.42% | 710.09/2589.39 = 27.42% | l.72-74,71 | PASS |
| ETR consol Q1FY26 | 26.16% | 253.89/970.58 = 26.16% | l.72-74,71 | PASS |
| ETR consol Q4FY26 | 21.89% | 494.12/2257.62 = 21.89% | l.72-74,71 | PASS |
| ETR standalone Q4FY26 | 21.49% | 483.55/2252.21 = 21.47% | l.135-137,134 | PASS (2 bp, rounding) |
| S-vs-C PAT gap Q1FY27 | SA>C by 0.27 (sub −0.27) | 1905.89−1879.31 = 25.68 L = 0.26; sub −26.58 L | l.138 vs l.75; l.50 | PASS |
| S-vs-C PAT gap Q4FY26 | SA>C by 0.05 | 1768.66−1763.50 = 5.16 L = 0.05 | l.138 vs l.75 | PASS |
| S-vs-C PAT gap Q1FY26 | SA>C by 0.46 | 762.28−716.69 = 45.59 L = 0.46 | l.138 vs l.75 | PASS |
| S-vs-C PAT gap FY26 | C>SA by 0.24 (**reversed**) | 5552.70−5528.22 = 24.48 L = 0.24 | l.138 vs l.75 | PASS — direction reversal confirmed |
| Skid revenue % of consol rev | 22.3% | 32.4/145.38 = 22.29% | slide14 l.138 / l.59 | PASS (just above 20-22% band; A4 flags "top of band" AMBER) |
| Skid ASP trend | 4,98,861→3,31,763→3,11,459 (3 qtrs down, −38%) | 311459/498861 = 0.624 → −37.6% | slide14 l.138-140 | PASS |
| Skid rev cross-check | 32.4 Cr | 1,040 × 311,459 = 32.39 Cr | slide14 l.138 | PASS |
| Reg 32 total undeployed | Rs 11.14 Cr | 54,99,99,714.60 − 43,85,87,557.00 = 11,14,12,157.60 | l.195 | PASS |
| Reg 32 GCP undeployed | Rs 10.38 Cr | 12,02,49,931 − 1,64,00,806 = 10,38,49,125 | l.188 | PASS |
| PAT bridge total consol | +11.63 Cr | GP +29.79 − Opex 11.77 − D 1.92 − Fin 0.17 + OI 0.27 − Tax 4.56 = +11.63 (=1879.31−716.69=1162.62 L) | Step 4 vs raw | PASS (all components tie) |
| EPS YoY consol / standalone | +158.18% / +144.07% | 1.42/0.55−1 / 1.44/0.59−1 | l.85 / l.144 | PASS |
| Hyd-Air share of consol PAT / rev | 1.41% / 5.3% | 26.58/1879.31 = 1.41%; 765.66/14537.63 = 5.27% | l.50 / l.75,59 | PASS |

**Arithmetic verdict: no mismatch above rounding.** The single sub-rounding item (standalone Q4FY26 ETR 21.49% vs my 21.47%, a 2 bp difference) is within tolerance and not counted as a discrepancy. Every task-specified metric — headline YoY/QoQ, S-vs-C PAT gap and its FY26 direction reversal, skid % of revenue, skid ASP trend, ETR across periods, and the Reg 32 undeployed figures — ties to the extract.

**Unit integrity:** Lakhs→Cr (×0.01) and absolute-Rupees→Cr (÷1,00,00,000) applied correctly throughout A4; deck already in Cr and reconciles to filing to the paise (verified on PAT: deck 18.79 = filing 1,879.31 L; 19.06 = 1,905.89 L; Q4FY26 17.64 = 1,763.50 L; FY26 55.53 = 5,552.70 L). No unit error.

**Provenance note (non-blocking):** the "MD&A ROCE 28.43%" figure used in the ROCE-definition flag (Q4, tripwire, combined verdict) appears in NEITHER A1 extract — it derives from an MD&A / annual-report source outside this run's inputs. A5 cannot independently source it. It does not corrupt any conclusion because the ROCE tripwire's INDETERMINATE read stands independently on (a) no ROCE printed in a Q1 filing and (b) idle-raise denominator inflation and (c) the six-year decline; the 28.43% is an additive, explicitly-unresolved horn routed to a management question, not settled evidence. Recommend A4/A3 pin its provenance at save.

---

## 3. ADVERSARIAL READ (three most-positive claims; strongest bear counter from the same extract)

**Positive claim 1 — "Op EBITDA margin expanded +469 bps YoY to 23.04%, at the FY27 guide."**
Bear counter (from slide 9, l.98): margin fell −82 bps QoQ (23.86%→23.04%) and Q1FY27 sits below Q4FY26; the +469 bps is measured off a weak Q1FY26 base (18.35%) and is being given back sequentially as skid ASP falls. **Survives? NO — already incorporated.** A4 Step 3 and Step 6D state the QoQ −82 bps and the ASP/mix driver. No graft required.

**Positive claim 2 — "PAT +162% with ~98% of the increase from core operations; growth is real, not treasury-driven."**
Bear counter (from l.50, l.75; slide 23): consolidated PAT (18.79) is now BELOW standalone (19.06) because wholly-owned Hyd-Air (assets Rs 38.25 Cr) is loss-making with no diminution provision while the deck cites "major infrastructure enhancements"; and the 162% is low-base operating leverage that caps forward once margins are at the 23% ceiling and ETR (27.4%) plus rising steady-state D&A bite. **Survives? NO — already incorporated.** A4 flags the S-vs-C reversal (Q6, auditor, flags), the ETR headwind and rising D&A (Step 4), and frames Q1 as front-loaded. No graft required.

**Positive claim 3 — "Revenue +72.4% YoY, well ahead of the 35% guide; lands AT or ABOVE guided base on all disclosed operational metrics; no trigger fired."**
Bear counter (from slide 14 l.138 + slide 13 l.133): roughly half the headline is the SFN skid ramp (32.4 Cr, 22.3% of revenue) bought with a collapsing ASP (−38% over three quarters) from a single unnamed anchor customer; ex-skid revenue grew ~34% (145.38−32.4 = 112.98 vs ~84.33), i.e. the CORE is merely at the 35% guide, not "well ahead," and the beat quality is falling as pricing and customer concentration deteriorate. **Survives? PARTIAL — substance incorporated, one framing not explicit.** A4 covers ASP decline, single-customer concentration, and skid revenue 14% below the Notion estimate; it also shows hoses +40.5% and assemblies +33.6-37.0% (core growing above ~33%, which blunts the "only at guide" edge). The explicit ex-skid decomposition (~34%) is not stated, but every input to it is on A4's table and the cautionary read is already symmetric. This does not rise to a surviving un-incorporated counter that must be grafted; it is at most a one-line sharpening.

**Adversarial verdict:** no bear counter survives un-incorporated. A4's cautionary-signals block, 12-item flag list, and 14 management questions already carry each counter. Nothing must be added to A4 before save.

---

## 4. VERDICT

**COMPLETE.**

- Coverage: all six results categories and all five presentation categories reconcile to an independent fresh pass; no orphan disclosure rows; no rows missing from the ledger; every forward-signal/ambiguous finding produced a management question.
- Arithmetic: every derived metric — including all task-specified ones (headline YoY/QoQ, S-vs-C PAT gap and its FY26 direction reversal, skid % of revenue, skid ASP trend, ETR across periods, Reg 32 undeployed funds) — ties to the extract within rounding; unit conversions are correct.
- Adversarial: the three strongest bear counters are already incorporated; none survives that must be grafted.
- The PROCEED WITH FLAGS verdict is defensible and house-rule compliant: INDETERMINATE cash conversion is not resolved to a clean PROCEED (it is held below the CAVEATS cap at FLAGS with missing evidence named — H1 CFO/PAT, receivable/inventory days, CWIP-to-PPE). The ROCE tripwire is honestly caveated as NOT FIRED / numeric read INDETERMINATE (no ROCE in a Q1 filing; denominator inflated by the idle raise; six-year decline), and is explicitly a flag, not a firing.

The four low-severity coverage observations in §1d (dropped-slide caveat not carried; "No Deviation/Variation" label not challenged; note-numbering gaps; 46-minute meeting / uncited 9+ GW) and the 28.43% provenance note in §2 are NON-BLOCKING recommendations for one-line caveats at save. None is a missed material disclosure, an arithmetic error, or a surviving bear counter, so none meets the FAIL threshold. Review proceeds to Notion save.

---

```yaml
stage: A5-adversary
company: "AEROFLEX"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
