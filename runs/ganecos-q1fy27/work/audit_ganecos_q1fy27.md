# A5 ADVERSARY / COMPLETENESS AUDIT — Ganesha Ecosphere Limited (GANECOS) — Q1 FY27

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Re-audit loop 1 of max 2.
Inputs seen: A4 revised review, A1 results extract, A1 boardoutcome extract, A2 results ledger, A2 boardoutcome ledger. Nothing else. All figures independently re-derived from the raw Lakh cells (x0.01 to Rs Cr); A4/A3 cites checked, not trusted.

Trigger for this loop: prior A5 returned INCOMPLETE on one cell — consolidated Reported EBITDA Q4 FY26 stated 62.84, should be 56.84 (PBT 30.88 + Dep 17.16 + Fin 8.79). This re-audit (a) confirms that specific cell and (b) re-runs the entire coverage + arithmetic + adversarial audit from scratch.

---

## AUDIT 1 — COVERAGE (fresh enumeration vs A2 ledgers)

Fresh grep/sweep over both extracts, diffed against both A2 ledgers.

| Category | Doc | A2 count | My fresh count | Orphan / missing | Status |
|---|---|---|---|---|---|
| Notes | results | 14 | 14 (std 7: L101-113; consol 6 numbered L249-260 + 1 unnumbered ESOP bullet L261-264) | none | PASS |
| Line items | results | 64 | 64 (std 31 + consol 33; consol carries 2 extra rows — assoc-loss L217 + split PBT V/VII) | none | PASS |
| Zero-standing | results | 4 | 4 (std B(i) L83, B(ii) L86; consol B(i) L231, B(ii) L234) | none — retained | PASS |
| Auditor paras | results | 15 | 15 (std 4 unnumbered prose L144-174; consol 11 numbered L293-377, para1 OCR "I.", para11 "11.Our") | none | PASS |
| Entities | results | 6 | 6 (parent, Ecopet, Ecotech, Nepal Overseas, Welfare Trust, Recycling Chain assoc; L321-335) | none | PASS |
| Agenda items | results | 4 | 4 (Section-1 rows: results approval, encl 1, encl 2, meeting-time) | none | PASS |
| Turns / slides | results | 0 / 0 | 0 / 0 (no transcript, no deck) | none | PASS |
| Agenda items | boardoutcome | 1 | 1 (SVP re-appointment) | none | PASS |
| Annexure particulars | boardoutcome | 4 | 4 (reason, date/term, profile, relationship) | none | PASS |
| Related-party facts | boardoutcome | 2 | 2 (son of Exec VC; MD of Ganesha Ecoverse) | none | PASS |
| Regulatory refs | boardoutcome | 2 | 2 (Reg 30; SEBI Master Circular) | none | PASS |
| Signatory block | boardoutcome | 1 | 1 (Bharat Kumar Sajnani, CS) | none | PASS |
| Meeting-time facts | boardoutcome | 2 | 2 (commenced 5:15; concluded illegible) | none | PASS |
| Entities | boardoutcome | 1 | 1 (Ganesha Ecoverse group co) | none | PASS |

**Row-citation check (every ledger row cited in A4 OR marked reviewed-no-finding):**
- A4 preamble (L12-13) recites the Doc-1 inventory (14 notes / 64 line items / 15 auditor paras / 6 entities / 4 agenda / 4 zero-standing) verbatim to the A2 counts and states "All reviewed." That is a valid blanket reviewed-no-finding statement covering rows not individually cited (e.g. the OCI section and the 4 zero-standing B(i)/B(ii) rows, which A4's Step-1 P&L tables legitimately stop short of — they carry no forward signal and are nil / non-reclassified in all periods). **No orphan.**
- Doc-2: A4 preamble tallies only 5 of the 7 board-outcome categories (omits meeting_time_facts=2 and entities=1 from the count line). Both are nonetheless cited in the review body — meeting-time / signature-timestamp sequencing at L359; Ganesha Ecoverse entity at L336/L357/L382 and question Q6. **No orphan; presentational note only** (A4 could tighten the preamble tally, but every row is substantively addressed).
- All 14 findings (F-01…F-08; A3-F6-01, F13-01, F13-02, F14-01, F14-02, F14-03) map to Step tables, the governance section, or the 11 management questions.

**COVERAGE VERDICT: PASS. Zero orphan rows, zero rows my fresh pass found that the ledger lacks. Standalone and consolidated both first-class. Zero-standing rows retained.**

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw Lakh cells)

Raw-cell tie-out of Step-1 extraction tables (standalone L54-99, consolidated L199-247): every one of the 64 line-item cells in A4's two Step-1 tables matches the extract at x0.01. No transcription error.

### The corrected cell (prior-loop failure) — re-verified independently
| Metric | A4 value | My recompute (raw) | Source | Status |
|---|---|---|---|---|
| Consol Reported EBITDA Q4 FY26 (PBT+D+Fin) | **56.84** | (3088.13+1716.04+879.41)/100 = 5683.58/100 = **56.84** | L218, L210-211, L209 | **FIXED — PASS** |

Row consistency re-check across all four periods: 39.66 / 56.84 / 63.31 / 159.09 = (14.32+15.50+9.84) / (30.88+17.16+8.79) / (37.09+17.34+8.87) / (53.95+64.81+40.32). All four tie. No sibling cell disturbed by the correction.

### Standalone derived metrics
| Metric | A4 | Recomputed | Status |
|---|---|---|---|
| Op EBITDA (PBT+D+Fin−OI) Q1/Q4/Q1'/FY | 9.30 / 20.93 / 23.79 / 56.95 | 9.30 / 20.93 / 23.79 / 56.95 | PASS |
| Op EBITDA margin | 4.20 / 8.04 / 9.07 / 5.62% | 4.20 / 8.04 / 9.07 / 5.62% | PASS |
| Reported EBITDA (PBT+D+Fin) | 17.47 / 30.79 / 27.31 / 96.75 | 17.47 / 30.79 / 27.31 / 96.75 | PASS |
| Core PBT (PBT−OI) | 2.11 / 12.33 / 14.94 / 24.67 | 2.11 / 12.33 / 14.94 / 24.67 | PASS |
| Other Income / PBT | 79.5 / 44.4 / 19.1 / 61.7% | 79.5 / 44.4 / 19.1 / 61.7% | PASS |
| Effective tax rate | 25.5 / 26.1 / 25.5 / 25.8% | 25.5 / 26.1 / 25.5 / 25.8% | PASS |
| PAT margin (on rev) | 3.46 / 6.30 / 5.24 / 4.72% | 3.46 / 6.30 / 5.24 / 4.72% | PASS |

### Consolidated derived metrics
| Metric | A4 | Recomputed | Status |
|---|---|---|---|
| Op EBITDA (V+D+Fin−OI) | 36.31 / 52.35 / 59.78 / 141.71 | 36.31 / 52.35 / 59.78 (raw 59.7755) / 141.71 | PASS |
| Op EBITDA margin | 10.77 / 12.35 / 14.11 / 9.56% | 10.77 / 12.35 / 14.11 / 9.56% | PASS |
| Reported EBITDA (PBT+D+Fin) | 39.66 / 56.84 / 63.31 / 159.09 | 39.66 / 56.84 / 63.31 / 159.09 | PASS |
| Core PBT (PBT−OI) | 10.94 / 26.34 / 33.47 / 36.53 | 10.94 / 26.34 / 33.47 / 36.53 | PASS |
| Other Income / PBT | 23.6 / 14.7 / 9.8 / 32.3% | 23.6 / 14.7 / 9.8 / 32.3% | PASS |
| Effective tax rate | 24.9 / 24.8 / 21.7 / 29.2% | 24.9 / 24.8 / 21.7 / 29.2% | PASS |
| PAT margin (on rev) | 3.19 / 5.48 / 6.85 / 2.58% | 3.19 / 5.48 / 6.85 / 2.58% | PASS |

### Step-2 YoY (Q1 FY27 vs Q1 FY26)
| Metric | A4 | Recomputed (raw) | Status |
|---|---|---|---|
| Std revenue | +18.4% | 262.30/221.47−1 = +18.4% | PASS |
| Std Op EBITDA | +155.8% | +155.8% | PASS |
| Std margin | +487 bps | 9.07−4.20 = 487 bps | PASS |
| Std finance cost | +51.8% | 199.90/131.65−1 = +51.8% | PASS |
| Std EBIT (op) | +394.6% | 16.9375/3.4254−1 = +394.5% | PASS (0.1pp intermediate-rounding, within tolerance) |
| Std Other Income | −57.0% | 351.68/817.01−1 = −57.0% | PASS |
| Std Core PBT | +608.4% | 1493.85/210.89−1 = +608.4% | PASS |
| Std reported PBT | +79.5% | +79.5% | PASS |
| Std PAT | +79.4% | +79.4% | PASS |
| Std EPS basic | +70.4% | 5.13/3.01−1 = +70.4% | PASS |
| Consol revenue | +25.7% | 423.67/337.12−1 = +25.7% | PASS |
| Consol Op EBITDA | +64.6% | +64.6% | PASS |
| Consol margin | +334 bps | 14.11−10.77 = 334 bps | PASS |
| Consol finance cost | −9.8% | 887.26/984.13−1 = −9.8% | PASS |
| Consol EBIT (op) | +103.9% | 4243.30/2081.05−1 = +103.9% | PASS |
| Consol Other Income | +7.2% | 361.98/337.81−1 = +7.2% | PASS |
| Consol Core PBT | +206.0% | 3347.49/1094.03−1 = +206.0% | PASS |
| Consol reported PBT | +159.1% | +159.1% | PASS |
| Consol PAT | +170.0% | 2903.48/1075.36−1 = +170.0% | PASS |
| Consol EPS basic | +156.5% | 10.85/4.23−1 = +156.5% | PASS |

### Step-3 QoQ, Step-4 PAT bridge, Step-4A S-to-C gap
| Metric | A4 | Recomputed | Status |
|---|---|---|---|
| Consol rev QoQ | −0.06% | 423.67/423.94−1 = −0.06% | PASS |
| Consol margin QoQ | +176 bps | 14.11−12.35 = 176 bps | PASS |
| Consol core PBT QoQ | +27.1% | 33.47/26.34−1 = +27.1% | PASS |
| Std rev QoQ | +0.76% | 262.30/260.33−1 = +0.76% | PASS |
| Std PAT QoQ | −16.2% | 13.75/16.41−1 = −16.2% | PASS |
| Consol PAT YoY Δ | +18.28 | 29.03−10.75 = +18.28 | PASS |
| Bridge: rev contrib | +9.32 | 86.55 × 10.77% = +9.32 | PASS |
| Bridge: margin contrib | +14.15 | 3.34% × 423.67 = +14.15 | PASS |
| Bridge: Op EBITDA Δ | +23.46 | 59.7755−36.3145 = +23.46 | PASS |
| Bridge: D&A Δ | (1.84) | 17.34−15.50 = 1.84 | PASS |
| Bridge: finance Δ | +0.97 | 9.84−8.87 = 0.97 | PASS |
| Bridge: OI Δ | +0.24 | 3.62−3.38 = 0.24 | PASS |
| Bridge: assoc Δ | (0.06) | (8.55−2.89)/100 = 0.0566 → 0.06 | PASS |
| Bridge: PBT Δ | +22.77 (ties 22.78) | 3709.47−1431.84 = 22.78 | PASS |
| Bridge: tax Δ | (4.50) | 8.06−3.56 = 4.50 | PASS |
| Bridge: PAT Δ | +18.27 (ties 18.28) | 18.28 | PASS |
| Std PAT bridge close | +6.09 | 12.83−4.65−2.09 = +6.09 | PASS |
| S-to-C gap FY26 / Q1'26 / Q4'26 / Q1'27 | −9.62 / +3.09 / +6.80 / +15.29 | −9.62 / +3.09 / +6.80 / (2903.48−1374.95)/100=+15.29 | PASS |
| S-to-C gap % of std PAT Q1'27 | +111% | 15.29/13.75 = +111.2% | PASS |
| Gap decomposition residual | +0.61 | 15.29 − 15.04 + 0.27 + 0.09 = +0.61 | PASS |
| Share issuance | +1.339 Cr FV / +5.3% | 26.7960−25.4570 = 1.3390; /25.457 = 5.26% | PASS |
| EPS-behind-PAT (std) | ~9 pp | 79.4−70.4 = 9.0 pp | PASS |

### One approximate prose figure — recomputed and dispositioned (not a FAIL)
"~50.6% of consolidated PAT rests on component-auditor-reviewed subsidiaries" (L44, L396, flags). Component-auditor-reviewed net profit = para-7 domestic subs +15.04 and para-8 Nepal −0.27 = 14.77; 14.77/29.03 = **50.9%**. Domestic-subs-only = 15.04/29.03 = 51.8%. A4's "~50.6%" sits within the band of defensible denominator definitions (0.3pp from my primary recompute), is explicitly approximate ("~"), and is an audit-scope AMBER characterization, not a headline derived-valuation metric. The qualitative claim — roughly half of consolidated PAT rests on component-auditor-reviewed subs — is true and correctly flagged. **Recorded as a note, PASS within tolerance.** (Recommend A4 restate as "~51%" for precision, non-blocking.)

**ARITHMETIC VERDICT: PASS. The prior-loop cell (56.84) is corrected and internally consistent across the Reported-EBITDA row. Every other derived metric, margin, YoY/QoQ, PAT bridge, and ratio ties from the raw cells within rounding. No NOT-FOUND value estimated (FY26 basic EPS OCR-garble carried as flagged 18.12; missing Q2/Q3 FY26 and all balance-sheet/CFO rows held ND, not estimated).**

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims, strongest same-text bear counter)

**Claim 1 — "~100% of the +Rs 18.28 Cr YoY PAT rise is recurring core operations; genuinely high quality" (L217).**
Strongest bear (same extract): the +170% consolidated PAT leans on Rs 15.04 Cr from two subsidiaries reviewed only by component auditors (para 7, L347-348), off a recent loss base (within-FY26 Q2+Q3 S-to-C gaps sum to ~−19.5 Cr per A4's own FY26 reconciliation), and the group runs a sub-normal 21.7% ETR because the profitable subs pay ~nil current tax (tax shield, F-04). So "high quality / recurring" overstates durability and rests on a temporary tax level and lower-tier assurance.
**Survives? NO — already incorporated.** A4 flags component-auditor reliance (L44, L396), the ETR step-up risk (Step 4, L220; Q3), and the three durability caveats (Step 4A, L244). Nothing to graft.

**Claim 2 — "S-to-C PAT gap swung to +Rs 15.29 Cr (+111% of standalone PAT); decision-gate pre-condition (i) met" (Step 4A).**
Strongest bear (same extract): it is one quarter; the Rs 15.04 Cr is component-auditor-reviewed, not principal-audited; no utilisation/tonnage/product-mix disclosed to attribute the swing to structural volume vs one-off (grant / inventory revaluation / DTA drawdown); Warangal commissioning is silent and consol revenue is flat QoQ (no visible volume step-up).
**Survives? NO — already incorporated.** A4 states pre-condition (i) is "met on the reported number but not yet durable" with exactly these three caveats (L244), routes to Q1, and pushes the entry gate to the FY26 AR + one confirming quarter. Nothing to graft.

**Claim 3 — "Consolidated Op EBITDA margin +334 bps YoY / core PBT +206% YoY — genuine operating expansion" (Step 2, verdict).**
Strongest bear (same extract): Q4 FY26 is a Note-5 balancing figure so the sequential step is partly artefact; the +487/+334 bps could be feedstock/input-cost timing rather than structural pricing power with no tonnage or per-tonne data to confirm pass-through (tripwire 7); and a large Q1 inventory build (consol change-in-inventories −Rs 35.56 Cr vs −Rs 8.80 Cr PY) could be absorbing fixed cost and flattering the current-quarter margin — un-testable from a P&L-only filing.
**Survives? NO — already incorporated / non-determinable.** A4 carries the Note-5 balancing-figure caveat (L39, L178), the per-tonne mechanism gap (tripwire 7, Q11), and the inventory build under cash quality (L270) with cash conversion held INDETERMINATE and the missing evidence named. The over-production/absorption angle is not determinable from the extract (no cost breakout, no balance sheet), so per conservative bias it is a named-missing-evidence flag, which A4 already carries — not a proven surviving counter. Nothing to graft.

**ADVERSARIAL VERDICT: PASS. All three strongest bear counters are already present in A4's review; none survives as an unincorporated counter requiring graft.**

---

## DECISION-STATUS INTEGRITY CHECK
Decision Status = WATCHLIST, unchanged. No committed thesis-broken / growth trigger exists (pre-thesis name), so none fired; the change is correctly withheld absent a committed trigger. Cash conversion INDETERMINATE correctly caps off a clean PROCEED; verdict PROCEED WITH FLAGS is consistent with the flag load. Compliant.

---

## VERDICT

**COMPLETE.**

The one prior-loop arithmetic failure (consol Reported EBITDA Q4 FY26) is corrected to 56.84 and is internally consistent across all four periods of the Reported-EBITDA row, with no sibling cell disturbed. Independent re-run finds: coverage total (zero orphans, zero ledger gaps; standalone and consolidated both first-class; four zero-standing rows retained); every derived metric, margin, YoY/QoQ, PAT bridge and ratio ties from the raw Lakh cells within rounding; no NOT-FOUND value estimated; all three strongest bear counters already incorporated; Decision Status unchanged without a committed trigger. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "GANECOS"
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
