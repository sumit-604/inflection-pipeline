# A5 ADVERSARY / COMPLETENESS AUDIT — GAUDIUMIVF Q1 FY27 (merged: results + monitoring + presentation)

Auditor: A5 (fresh context). Inputs seen: A4 merged review, three A1 extracts, three A2 ledgers. A3 reasoning NOT seen — every number below is re-derived from the raw extracts, not deferred to A4/A3 cites. Units: filing + deck in Rs Lakhs, monitoring in Rs Crore; all figures reconciled to Rs Crore (1 Cr = 100 L).

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS GATE (run first)

The A4 review carries a MANDATORY PLAIN-LANGUAGE BRIEF as Section F, all four labelled parts present and carrying real content:

| Part | Heading in review | Present? | Content check |
|---|---|---|---|
| (1) Summary narrative | F1 (lines 446-452) | PRESENT | ~15 lines; numbers-anchored; states verdict PROCEED WITH FLAGS |
| (2) Sector intelligence | F2 (lines 454-456) | PRESENT | IVF TAM, penetration, ART Act, self-pay dynamics — non-placeholder |
| (3) Business-model intelligence | F3 (lines 458-460) | PRESENT | hub-spoke, ARPU/OPU, subsidiary drug-trading arm, IPO recap |
| (4) Competition intelligence | F4 (lines 462-464) | PRESENT | Indira/Nova/Birla peers, execution-pace battleground, provenance flagged |

**Gate 0: PASS.** All four parts present and non-empty.

---

## AUDIT 1 — COVERAGE (fresh grep pass vs A2 ledgers; then ledger→A4)

### 1a. Independent enumeration vs ledger counts

| Category | A2 count | My fresh count | Method | Orphan/missing | Status |
|---|---|---|---|---|---|
| Presentation slides | 36 | 36 | `grep -c "^\[page "` = 36 | none | MATCH |
| Deck Adjusted-EBITDA callouts | 2 | 2 | `grep "Adjusted EBITDA is"` → L710 (507.75/37.12%), L737 (532.75/27.49%) | none | MATCH |
| Consolidation entities | 3 | 3 | grep entities L447/451/452 (Holding + Gaudium International + EKK Global) | none | MATCH |
| Results standalone P&L rows | 24 | 24 | full read L217-264 | none | MATCH |
| Results consolidated P&L rows | 25 | 25 | full read L503-576 | none | MATCH |
| IPO utilisation rows (x2 stmts) | 12 | 12 | read L316-337 / L638-659 | none | MATCH |
| Note-7 (>10% expenditure) rows | 6 | 6 | read L340-356 / L661-677 | none | MATCH |
| Monitoring object rows (4 tables) | 14 | 14 | read Sec 4(i)/4(ii)/4(iv)/5 | none | MATCH |
| Monitoring fund-utilization rows | 39 | 39 | read; 9 arithmetic cross-checks re-tied (below) | none | MATCH |
| Lucknow GCP advance | 1 | 1 | `grep "5.76"` → L495/504/708/723/732 | none | MATCH |
| Board-agenda items | 5 | 5 | read L42-78 | none | MATCH |

No category produced a count my fresh pass found but the ledger lacks (→ no A2 FAIL). No orphan enumeration.

### 1b. Every ledger row cited in A4 or reviewed-no-finding

Preamble (review L15-26) makes the contractual "all rows reviewed, no estimation" statement and lists A3/FND findings incorporated. I checked every FLAGGED ledger row (the only rows that can hide an orphan) against A4:

- Results: EKK stale entity → Step 0D + B5 + Q11 (A3-F15); Legal-fees identical 140.27 SA/consol → Q12 (A3-F14); discontinued-op line → Step 0D/PAT-bridge (A3-F1a); Q4FY26 prior-year tax (37.65) → Step 3/4 (A3-F8); Annexure-D Note-1 reallocation 192.63 → Step 0D (A3-F6c); UDIN_ILLEGIBLE → Step 0. **All addressed.**
- Monitoring: EVIDENCE_GAP 0.30 Cr vendor quotations → C1 + Q7 (FND-1); RECLASSIFICATION Lucknow-via-GCP → C1 + Q5 (FND-7); DELAY/deferment → Step 6D + C1 (FND-5); ZERO_STANDING/DUPLICATE_NOTE benign. **All addressed.**
- Presentation: CONSOLIDATED_BASIS_UNLABELED → B1/FND-06; ADJUSTED_EBITDA_GAP + CONSISTENT_ADJUSTMENT_AMOUNT → B2/C2/FND-05; CONTINUING_OPS_LABEL → B5/Q14; MISSING_DIN → FND-03/Q13; ODD_TEMPLATE_TEXT → B4/FND-04; PERIOD_UNSTATED → B4/C3. **All addressed.**

Two benign ledger flags left without a dedicated A4 sentence, both self-resolving and NON-gating:
- `results` ledger note (L198-201): consolidated EPS > standalone EPS every period. Trivially expected — consolidated PAT (177.59) > standalone (166.35) on identical share count → higher EPS; not an anomaly. Covered by implication in the subsidiary discussion (C2/FND-01).
- `presentation` slide-17 `ARITHMETIC_CHECK_NEEDED` (state hub/spoke sums). My independent sum: spokes 2+3+2+2+1+6+6+5+1 = 28; hubs 1+1+3+1+1+1 = 8 → the state figures DO reconcile to the stated 8 hubs / 28 spokes. Flag can be closed as PASS; review labels the whole KPI block unaudited, which is adequate.

**Audit 1: PASS.** No orphan rows (→ no A3 loop-back), no missing enumeration (→ no A2 loop-back).

---

## AUDIT 2 — ARITHMETIC (recomputed from raw Lakhs; every derived metric)

Recomputed independently from filing raw lines. Representative full set (all A4 tables checked; all tie within rounding):

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| SA Operating EBITDA Q1FY27 | 2.17 | 229.96+67.54+32.26−112.36 = 217.40 L = 2.174 | res L236/233/232/223 | TIE |
| SA Op-EBITDA margin Q1FY27 | 15.89% | 217.40/1367.73 | res L222 | TIE |
| SA Op-EBITDA margin Q1FY26 | 33.86% | 415.55/1227.32 | res L222 | TIE |
| SA Op-EBITDA YoY | −47.7% | 217.40/415.55−1 = −47.68% | — | TIE |
| SA margin YoY | −1,797 bps | 15.89−33.86 | deck L696 (−1797) | TIE |
| SA Core PBT ex-OI Q1FY27 | 1.18 | 229.96−112.36 = 117.60 | res L236/223 | TIE |
| SA Core PBT ex-OI YoY | −61.8% | 117.60/307.84−1 = −61.80% | — | TIE |
| SA ETR Q1FY27 | 27.66% | 63.61/229.96 | res L244/236 | TIE |
| SA PAT margin Q1FY27 | 12.16% | 166.35/1367.73 | res L245 | TIE |
| SA PAT bridge ΔPAT | −0.69 | 166.35−235.08 = −68.73 L | res L245 | TIE |
| — bridge sum | −0.69 | −1.98+1.12−0.10+0.17+0.09 = −0.70 | — | TIE (rounding) |
| SA S&M step-up | −2.23 | 382.96−159.72 = 223.24 L | res L348-349 | TIE |
| Consol Op EBITDA Q1FY27 | 2.42 | 244.98+72.17+37.62−112.36 = 242.41 | res L537/531/529/514 | TIE |
| Consol Op-EBITDA margin | 12.51% | 242.41/1937.66 | res L512 | TIE |
| Consol margin YoY | −1,651 bps | 12.51−29.02 | deck L723 (−1651) | TIE |
| Consol Core PBT ex-OI YoY | −67.2% | 132.62/404.78−1 = −67.24% | — | TIE |
| Consol PAT YoY | −42.3% | 177.59/307.62−1 = −42.27% | res L549 | TIE |
| Consol PAT bridge ΔPAT | −1.30 | 177.59−307.62 = −130.03 L | — | TIE |
| Consol S&M step-up | −2.42 | 404.33−162.72 = 241.61 L | res L670 | TIE |
| Revenue YoY SA / Consol | +11.4% / +9.1% | 11.44% / 9.13% | res L222/512 | TIE |
| ETR SA/consol vs 25.17% | 27.66% / 27.51% (above) | 63.61/229.96; 67.39/244.98 | — | TIE |

**Standalone-vs-consolidated (subsidiary) gap math — independently rebuilt:**

| Item | A4 | My recompute | Status |
|---|---|---|---|
| Subsidiary PAT contribution Q1FY27 | 6.8% of SA PAT | (177.59−166.35)=11.24; /166.35 = 6.76% | TIE |
| Subsidiary PAT contribution Q1FY26 | 30.9% | (307.62−235.08)=72.54; /235.08 = 30.86% | TIE |
| Q4FY26 / FY26 | 8.1% / 9.9% | 62.60/773.14=8.10%; 220.08/2228.77=9.87% | TIE (matches YAML sc_gap) |
| Subsidiary net margin | ~13% → ~2% | 72.54/548.27=13.2% → 11.24/569.93=1.97% | TIE |
| Subsidiary revenue (flat) | ~5.5-5.7 Cr | 548.27 L → 569.93 L | TIE |

**Adjusted-EBITDA add-back (Rs 2.90 Cr) — independent adjudication:**
- Standalone add-back = 507.75 − 217.40 = **290.35 L**; consolidated = 532.75 − 242.40 = **290.35 L**. Identical absolute confirmed (deck L710/737). Recast margins 37.12% / 27.49% both recompute exactly.
- Over-scoping: 290.35 − 223.24 (SA S&M rise) = 67.11 L = **30.1% larger** than the entire standalone S&M step-up. A4's "~67 L / ~30%" is correct.
- Cross-base incoherence: consolidated incremental S&M (241.61 L) exceeds standalone (223.24 L) by 18.37 L, yet the add-back is identical 290.35 L at both bases. A genuine group re-computation would differ across bases; a fixed number that tracks neither S&M rise is a plug. **A4's adjudication (AMBIGUOUS leaning confirmatory-negative; framing device; do not rely) is SOUND and fully supported by the extract — I reach the same conclusion independently.**

**Audit 2: PASS on all derived tables.** One narrative labelling imprecision found (NON-gating, advisory to A4) — see below.

### Advisory (does not fail the gate)
1. **FD-interest share-of-PBT mislabel.** Flag L517 and Q8 (L413) say "Rs 1.02 Cr FD interest ... (49% of SA PBT)." Precisely: FD interest 102.24 / PBT 229.96 = **44.5%** of PBT; the 48.9% figure is *total other income* / PBT (112.36/229.96), and FD interest is **61.5%** of PAT (102.24/166.35). The load-bearing claims (Rs 1.02 Cr FD interest; ~61% of PAT; OI 48.9% of PBT in Step-2 diagnostic 6) are all individually correct; only the shorthand conflates "FD interest" with the 49% OI/PBT ratio. Recommend A4 relabel to "other income 48.9% of PBT / FD interest 61% of PAT." Derived tables are unaffected.
2. **GCP "largely consumed" (Q6).** GCP utilised 7.21 of 12.28 Cr (59%), unutilised 5.07 Cr, plus the +1.93 Cr repayment-tranche reallocation raises headroom — "largely consumed" slightly overstates; directionally fine for a management question. NON-gating.

---

## AUDIT 3 — CROSS-DOCUMENT & SPECIAL CHECKS

**Lucknow-via-GCP reconciliation (independently verified):** Monitoring Note 2 (L480-504) + Section 5 (L708-732): Rs 5.76 Cr advance for Gaudium Women Hospital Lucknow (30-yr lease, 15-yr lock-in, 10% monthly net revenue + Rs 3.00 Cr refundable deposit, Board 28 May 2026) funded under GCP head, expressly NOT from the earmarked New-IVF-Centres object, under certified "Deviation: Nil." GCP during-quarter = 5.76 + 0.42 TDS + 0.06 IPO commission = **6.24 Cr** = monitoring Sec 4(ii) GCP "during quarter" (L438) — reconciles exactly. Meanwhile the New-IVF-Centres object shows 1.03 Cr utilised / 48.97 Cr idle (98%), confirmed identically in filing IPO table (102.95 L) and monitoring. **A4's C1/C2 reconciliation is correct:** growth capex is deferred/back-loaded, not structurally stalled; the one moving asset runs off-object via GCP; the "Nil deviation" certificate coexists with a substance-over-form question (a leased hospital funded from GCP). Fully supported.

**INDETERMINATE cash-conversion cap:** correctly applied. No Q1 CFO/balance sheet is mandated under Reg 33 until Q2 half-yearly; Step 5 marks CFO/CFO-PAT/WC-days ND, names the missing evidence, and caps the verdict below plain PROCEED per house rule. Compliant with CLAUDE.md.

**No exit PE / valuation introduced:** confirmed. Step 7 records forward inputs only ("No destination PE on record"), Step 8 pushes the workup to Section 1B v3.3, and the deck's market cap Rs 822.13 Cr / price Rs 112.95 are cited only as market data, never used to derive a multiple or target. Compliant with the CLAUDE.md NEVER rule (Section 1B is sole valuation authority; Role 4/5 introduces none).

**Questions-for-Management coverage:** every AMBIGUOUS / FORWARD-SIGNAL finding across all three docs generates a row — add-back (Q1/FND-05), S&M conversion (Q2/A3-F1b), subsidiary margin (Q3/A3-F2·FND-01), FY27 deployment (Q4/FND-2), Lucknow-GCP substance (Q5/FND-7), GCP headroom (Q6/FND-3), vendor-quotation invoices (Q7/FND-1), FD-interest run-rate (Q8/FND-06), AR/AGM disclosure (Q9-10), EKK exit (Q11/F15), legal-fee copy-across (Q12/F14), DINs (Q13/FND-03), deck basis (Q14/FND-06), hub-vs-centre reconciliation (Q15/FND-02). No orphan forward-signal finding.

---

## AUDIT 4 — ADVERSARIAL READ (three most-positive claims, strongest bear from same extract)

| # | A4 positive claim | Strongest bear counter (from extract) | Survives & must be grafted? |
|---|---|---|---|
| 1 | "Strip the S&M step-up and standalone margin is ~32%, roughly prior-year — parent intact, front-loaded expansion not deterioration." (C2/F1) | Revenue grew only 11.4% on a 140% S&M jump — marketing efficiency collapsed; S&M was already elevated in Q4FY26 (233.70 L), so the higher level may be a permanent run-rate, not a one-quarter blip, invalidating "add it back and it's fine." | NO — already incorporated: bridge labels S&M "Recurring", 8C sets the bear threshold "spend without conversion", Q2 asks exactly this. |
| 2 | "Debt fully repaid; near net cash with ~Rs 56 Cr FDs; finance costs −35% — genuine positive." (Step 2/5/F1) | The ~Rs 56 Cr is restricted, earmarked IPO money (48.97 capex + 5.07 GCP), committed to a Rs 26.31 Cr FY27 programme — not free flexibility; and a new long-dated fixed obligation (Lucknow 30-yr lease, 10% of monthly net revenue) was just created. | NO — already incorporated: Step 5 flags FDs as unspent IPO cash; B5 flags the Lucknow lease as an undisclosed fixed obligation. |
| 3 | "Growth capex not structurally stalled — certified FY27 plan Rs 26.31 Cr / 10 centres, Rs 5.76 Cr already flowing." (C1) | Only Rs 1.03 Cr (3.9%) deployed in Q1, of which 29.14% is vendor-quotation-only → ~Rs 0.73 Cr invoiced against a Rs 26.31 Cr plan; the "plan" is a post-deferment management projection, and the sole moving asset is off-object (leased hospital via GCP). | NO — already incorporated: C1 calls the ~Rs 25 Cr-in-9-months "ambitious", flags the 29.14% quotation gap and the GCP object-substance question. |

The A4 review is unusually bear-symmetric (it leads with the −1,797 bps margin collapse as "the headline of the quarter" and prints core-PBT-ex-OI declines of −62%/−67%). Every strongest bear counter I could construct from the extract is already present with a specific location. **No surviving bear counter is absent → nothing to graft into A4.**

---

## VERDICT

**COMPLETE.** All four audits pass. Deliverable gate PASS (all four brief parts present). Coverage PASS (no orphan ledger rows → no A3 loop-back; no missing enumeration → no A2 loop-back). Arithmetic PASS (every derived metric — Operating EBITDA, margins, ETR, YoY/QoQ, both PAT bridges, standalone-vs-consolidated subsidiary gap, and the Rs 290.35 L add-back — recomputed from raw Lakhs and ties within rounding). Adversarial PASS (three strongest bear counters all already incorporated). Rs 2.90 Cr add-back adjudication and Lucknow-via-GCP reconciliation independently confirmed sound. INDETERMINATE cash-conversion cap correctly applied; no exit PE / valuation introduced. Two NON-gating narrative imprecisions handed to A4 as advisory (FD-interest "49% of PBT" mislabel; GCP "largely consumed"); neither changes any number or verdict, so the run proceeds.

```yaml
stage: A5-adversary
company: "GAUDIUMIVF"
quarter: "q1fy27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
advisory_non_gating:
  - "A4 flag L517/Q8 label FD interest as '49% of PBT'; precisely other income=48.9% of PBT, FD interest=44.5% of PBT / 61% of PAT — relabel recommended, no number affected"
  - "A4 Q6 'GCP largely consumed': 7.21 of 12.28 Cr utilised (59%), plus +1.93 Cr reallocation headroom — mild overstatement, non-gating"
  - "presentation slide-17 ARITHMETIC_CHECK_NEEDED closes as PASS: state figures sum to 8 hubs / 28 spokes on independent recompute"
```
