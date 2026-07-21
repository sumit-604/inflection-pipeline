# A5 ADVERSARY / COMPLETENESS AUDIT — E2E Networks Limited (E2E / E2ENETWORKS), Q1 FY27

**Agent:** A5 ADVERSARY | **Model:** claude-opus-4-8 | **Date:** 2026-07-21
**Under audit:** `review_e2e_q1fy27.md` (A4 ANALYST)
**Inputs re-derived from:** A1 results extract, A1 presentation extract, A2 results ledger, A2 presentation ledger.
**Independence note:** every number below is recomputed from the A1 extracts (Lakhs x0.01; Millions x0.1). A4's and A3's cites were checked, not trusted. Run scope confirmed: results filing + press release only, **NO concall transcript** — Role 5 N/A is a legitimate scope fact, audited below.

---

## 1. COVERAGE AUDIT

Fresh enumeration re-run independently (manual sweep of both extracts + confirming greps).
Grep evidence: notes opener regex = **18**; zero-standing dash rows at lines 94/99 (consolidated) + 179/183 (standalone) = **4**; signature grep = 6 line-hits collapsing to **5** blocks.

### 1A. Results filing ledger

| Category | A2 count | My fresh count | Orphan / missing | Status |
|---|---|---|---|---|
| notes | 18 | 18 (9 consol L125-142 + 9 standalone L208-228) | none | PASS |
| line_items | 60 | 60 (30 per table x2) | none | PASS |
| zero_standing | 4 | 4 (Exceptional C+S L94/179; Current tax C+S L99/183; all four period-columns dash) | none | PASS |
| agenda_items | 1 | 1 (results approval L38-41) | none | PASS |
| auditor_paras | 10 | 10 (standalone 1-4; consolidated 1-5 + unnumbered Master-Circular para L359) | none | PASS |
| entities | 1 | 1 (Sovcloud Technologies Ltd) | none | PASS |
| signature_blocks | 5 | 5 (CS digital sig; 2 director sigs; 2 auditor sigs) | none | PASS |

### 1B. Press-release ledger

| Category | A2 count | My fresh count | Orphan / missing | Status |
|---|---|---|---|---|
| slides/pages | 2 | 2 | none | PASS |
| kpi_metrics | 42 | 42 | none | PASS |
| admin_identifiers | 14 | 14 | none | PASS |
| highlight_bullets | 12 | 12 (6 KFH + 6 OH) | none | PASS |
| narrative_statements | 12 | 12 | none | PASS |
| about_boilerplate | 2 | 2 | none | PASS |
| footnotes_disclaimers | 3 | 3 | none | PASS |
| entities | 2 | 2 (E2E + Sovcloud) | none | PASS |
| signature_units | 3 | 3 | none | PASS |

**No count mismatch in either ledger — no row loops back to A2.**

### 1C. Every FLAGGED ledger row reflected in A4?

| Flagged ledger row | A4 disposition | Status |
|---|---|---|
| ZERO_STANDING Exceptional items (C+S) | Step 4 bridge "Exceptional 0.00 nil both periods" (L166) | Cited |
| ZERO_STANDING Current tax (C+S) | A3-F1/F8, Step 4, Q4, verdict flag; "nil current tax" throughout | Cited |
| Tax pertaining to earlier years (sparse, FY26 only) | Step 1 ND(nil)/FY26 (0.41) (L77) | Cited |
| ENTITY_CHANGE Sovcloud | Note 9 table, para-4 other-matters, A3-F6/F15, Q8, monitorable 1 | Cited |
| SINGLE_AGENDA_ITEM | Preamble L17 | Cited |
| Note 2 "year ended" misstatement | A3-F14 (L306) | Cited |
| Consol Note 9 subsidiary unnamed vs standalone names it | A3-F14 | Cited |
| OCR-garbled FY26 deferred/total tax ("52V IO"/"56.l.36") | Step 1 memo L88 (flagged, not estimated) | Cited |
| Auditor unmodified opinion + para 4 Sovcloud reviewed 20-Jul | Step 0D L56 | Cited |
| Unnumbered Master-Circular consolidated para (L359) | Not individually named | Reviewed, no finding (procedural Reg 33(8) scope statement; immaterial) |
| NUMERIC_INCONSISTENCY +1,450 vs +1,446 bps | P-F14, Step 3 L148, flag | Cited |
| NOT_FOUND FY26 full-year EBITDA absolute base | Resolved from filing (126.26 Cr); ratio 93.4% reconciled L105 | Cited |
| FORWARD_LOOKING NCCL/MFU + capacity expansion | P-F6, Q9/Q11, monitorables 4/6 | Cited |
| UNATTRIBUTED_QUOTE | P-F14, Role 5 section L294 | Cited |
| UNAUDITED_FIGURES / limited-review-only | P-F7 (L311) | Cited |
| ~5,100 GPUs | Q9 ("from ~5,100 today") | Cited |
| Two qualitative OH bullets (org-capability; full-stack optimisation) | Not individually cited | Reviewed, no finding (qualitative, no metric; A3 raised no finding) |

**Result: every ledger row carrying a flag or finding is reflected in A4's review or is a defensible "reviewed, no finding." No orphan row → no loop-back to A3.** The two minor "reviewed, no finding" items (unnumbered Master-Circular para; two purely-qualitative OH bullets) carry no financial or forensic content and are correctly non-cited under A4's blanket 100%-reviewed confirmation (L25).

### 1D. A3 forward/ambiguous findings carried

A4's body cites A3-F1, F2 (S-vs-C gap, L318), F6, F8, F9, F10, F11 (net-worth tie-out, L86), F14, F15; and P-F6, F7, F8, F10, F14, F15, F16. The preamble "incorporated" list (L23) omits F2 and F11, but both appear in the body — a cosmetic list gap, not a coverage gap. Every A3 FORWARD-SIGNAL and AMBIGUOUS finding maps to ≥1 Question-for-Management (Q1-Q12) or monitorable. **No unincorporated A3 finding.** (Note: the A3 findings file is outside my injected inputs by design; A3 findings were audited via the A2 ledgers and A4's own cites, both of which reconcile.)

---

## 2. ARITHMETIC AUDIT

All recomputed from raw Lakhs (results) / Millions (press release). Source lines are the A1 results extract unless noted.

| Metric | A4 value | My recompute | Source line(s) | Status |
|---|---|---|---|---|
| Revenue Q1FY27 | 156.76 | 15,675.99 x0.01 = 156.76 | L79/164 | PASS |
| Revenue YoY | +334.1% | (156.76-36.11)/36.11 = +334.1% | L79/L164 vs 3,611.02 | PASS |
| Revenue QoQ | +63.9% | (156.76-95.64)/95.64 = +63.9% | vs 9,564.27 | PASS |
| Op EBITDA Q1FY27 (PBT+D+Fin-OI) | 117.90 | 58.6264+60.6444+10.0515-11.4201 = 117.90 | L87/88/93/80 | PASS |
| Op EBITDA Q4FY26 | 58.10 | 8.5582+51.3464+3.6804-5.4828 = 58.10 | same, Mar col | PASS |
| Op EBITDA Q1FY26 | **10.52** | -3.7535+27.4330+1.8305-14.9956 = **10.5144 → 10.51** | Jun-25 col | **NOTE — 0.01 rounding slip (within rounding)** |
| Op EBITDA FY26 | 126.26 | -21.1995+169.2269+12.2413-34.0064 = 126.26 | FY26 col | PASS |
| Op EBITDA Margin Q1FY27 | 75.21% | 117.90/156.76 = 75.21% | derived | PASS |
| Op EBITDA Margin Q1FY26 | 29.13% | 10.5144/36.11 = 29.12% | derived | NOTE — 29.12% (propagated from 10.52 slip) |
| Reported EBITDA margin Q1FY27 | 82.50% | 129.32/156.76 = 82.50% | derived | PASS |
| Core PBT ex-OI Q1FY27 | 47.21 | 58.63-11.42 = 47.21 | L93-L80 | PASS |
| Core PBT ex-OI Q1FY26 | (18.75) | -3.75-15.00 = (18.75) | derived | PASS |
| Core-PBT swing YoY | +65.96 | 47.21-(-18.75) = 65.96 | derived | PASS |
| Other Income / PBT Q1FY27 | 19.48% | 11.42/58.63 = 19.48% | derived | PASS |
| Other Income / PBT Q4FY26 | 64.02% | 5.48/8.56 = 64.02% | derived | PASS |
| Effective tax rate Q1FY27 | 25.14% | 14.7443/58.6264 = 25.14% | L101/L93 | PASS |
| Finance cost YoY | +449.2% | (10.05-1.83)/1.83 = +449.2% | L88 | PASS |
| Finance cost QoQ | +173% | (10.0515-3.6804)/3.6804 = +173.1% | L88 | PASS |
| Depreciation YoY | +121.1% | (60.64-27.43)/27.43 = +121.1% | L87 | PASS |
| Op EBITDA margin QoQ (the +1,446 bps claim) | +1,446 bps | 75.211% - 60.748% = +14.46pp = +1,446 bps | derived | PASS (confirms +1,450 press-box is the error) |
| Op EBITDA margin YoY | +4,608 bps | 75.211% - 29.117% = +46.09pp = **+4,609 bps** | derived | NOTE — +4,609 bps (press release L103 states +4,609; A4 Step 2 +4,608, 1-bp base rounding) |
| S-vs-C PAT gap (all periods) | 0.00 pp | Standalone L164-204 line-for-line identical to consolidated L79-121 | both tables | PASS |
| EPS basic-vs-diluted spread Q1FY27 | ~1.9% (0.04) | 2.14-2.10 = 0.04; 0.04/2.14 = 1.87%; prior periods 0.32/0.32, (0.14)/(0.14) = 0 | L120-121 | PASS |
| PAT bridge sum | +46.72 | 107.37-33.21-8.22-3.58-15.65 = 46.71; actual PAT YoY 43.88-(-2.84) = **46.72** | Step 4 | PASS (0.01 component-rounding; ties to true 46.72) |
| Net worth (FY26 memo) | 1,685.05 | (2,055.65+166,449.53) x0.01 = 1,685.05 | L116-117 | PASS |
| Annualised run-rate | ~627 | 156.76 x4 = 627.04 | derived | PASS |
| Q1 EBITDA / FY26 EBITDA ("93%") | 93.4% | 117.90/126.26 = 93.38% | derived | PASS |
| Depreciation +₹93 Mn QoQ (release) | ₹93 Mn | 606.44-513.46 = 92.98 Mn | L109 rel / L87 filing | PASS |
| Press-release headline reconciliation | exact | 1,568/1,179/586/439/606 Mn x0.1 = 156.8/117.9/58.6/43.9/60.6 Cr | rel L82-109 | PASS |

**Arithmetic verdict: no discrepancy above rounding.** One 0.01-Cr slip — A4 carried Q1 FY26 Operating EBITDA as 10.52 where the raw figure is 10.5144 (rounds to 10.51). It propagates trivially into three derived cells (Op EBITDA margin 29.13% vs true 29.12%; EBIT −16.91 vs −16.92; Dep/Op-EBITDA 260.7% vs 260.9%; Op-EBITDA YoY 1,020.7% vs ~1,021.4%). Every propagation is ≤0.2pp on the affected metric and **none is decision-relevant** (the 11.2x / "turned positive" reading is unchanged). Separately, A4's Step 2 "+4,608 bps YoY" is 1 bp below the more precise +4,609 bps (which the press release itself states). Both are within-rounding artifacts, **not FAILs**; noted for the record. No loop-back to A4 forced on arithmetic.

---

## 3. ADVERSARIAL READ — three most positive claims, strongest bear counter from the same extract

**Claim 1 (L128): "Core operating PBT ex-OI turned from Rs(18.75) to +Rs47.21 Cr — headline growth is real, not treasury-driven; the single strongest signal in the filing."**
Bear counter (same extract): the entire revenue step is credited to a *single* B200 cluster go-live (release L97-98, L102), Exit MRR and the recurring-vs-one-off split are undisclosed (P-F16), and the QoQ base Q4 FY26 is itself a Note 3 *balancing figure* (derived, not independently reported). So the "real operating profit" could be a one-quarter provisioning/go-live burst, not durable recurring earnings.
**Survives? Already incorporated.** A4 caveats durability throughout (Step 3 diag; L126, L150; Q1; verdict point 2). No new graft required.

**Claim 2 (L115/L127/L250): "Op EBITDA margin 75.21%, +4,609 bps YoY — structural margin step-up; margin proof FIRED, clears 64% guide."**
Bear counter (same extract): the margin is struck in a quarter where depreciation is still catching up (Dep/Op-EBITDA fell to 51.4%) and finance costs jumped +173% QoQ / +449% YoY — both of which A4 itself calls NOT steady-state (L172). As B200/Blackwell capex commissions, D&A + interest step up and compress the margin back toward the ~64% guide; 75.21% is a utilisation-peak / under-depreciated-quarter figure, not proven "structural."
**Survives? Already incorporated.** A4 asks exactly this in Q11 and states it in Step 4 (L172). The Step-2 label "structural" is arguably strong versus A4's own Q11 caveat, but the caveat is present in the review. No new graft required.

**Claim 3 (L56/L105/L372): "Every press-release headline reconciles exactly to the filing; auditor opinion unmodified; 0% of consolidated PAT rests on unaudited/management-furnished numbers."**
Bear counter (same extract): every reconciled figure is expressly "unaudited and subject to limited review" (release L124-125) and the auditor twice states "we do not express an audit opinion" (L280-281, L357) — moderate assurance only. The release reconciles on the lines it *chooses* to show while omitting the unfavourable ones the filing carries: finance costs +173% QoQ, other income ~19% of PBT, and nil current tax. "Everything reconciles" therefore overstates disclosure quality.
**Survives? Already incorporated.** A4 flags selective disclosure (P-F16, verdict flag) and limited-review-only status (P-F7). No new graft required.

**Adversarial conclusion:** all three strongest bull claims have a genuine bear counter, and in every case A4 has ALREADY grafted that counter into the review (durability/one-off, margin-not-steady-state, selective-disclosure/limited-review). **No surviving un-incorporated bear counter → no loop-back to A4 on completeness.** This is a marker of a thorough A4, not a gap.

---

## 4. TARGETED CHECKS REQUESTED

- **Role 5 N/A handling:** correct. No transcript in scope; A4 marked Role 5 N/A with a one-line reason (L292), folded all forward/guidance statements from the release into Role 4 and the Questions/monitorables lists, and logged the UNATTRIBUTED_QUOTE to carry into the first concall. Turns reviewed = 0 is a true scope fact, not a missed enumeration. PASS.
- **Zero-standing lines:** both (Exceptional items, Current tax) addressed; the sparse "earlier-years tax" row correctly *not* treated as zero-standing. No missed zero-standing line. PASS.
- **Auditor-paragraph nuance:** unmodified on both reports; consolidated para 4 (Sovcloud reviewed unmodified, dated 20-Jul-2026, one day before the board meeting) captured; no EoM / Going Concern present; standalone report correctly carries no Other-Matters para. Only the unnumbered Master-Circular procedural para is uncited (immaterial). PASS.
- **Omitted press-release metric:** every release KPI (incl. ~5,100 GPUs, +₹93 Mn depreciation, 93% ratio, 4.3x, both bps figures) is reflected. PASS.
- **INDETERMINATE cash-conversion handling:** correct and house-rule compliant. No CFO/balance sheet at Q1 (Reg 33 half-yearly); A4 classified cash conversion INDETERMINATE, named the missing evidence (CFO/PAT, capex split, net debt, WC), and did NOT resolve it silently to PROCEED. Per CLAUDE.md the INDETERMINATE cap is PROCEED WITH CAVEATS; A4 landed one notch more cautious at PROCEED WITH FLAGS (selective-disclosure flags propagate past a caveat). That honours both "may not resolve silently to PROCEED" and the cap. PASS.
- **Verdict defensibility / escalation:** PROCEED WITH FLAGS is defensible. Arithmetic sound, both ledgers reconcile, auditor unmodified, no thesis-broken trigger fired, no mechanical failure — so no escalation to REWORK/INSUFFICIENT EVIDENCE is warranted; and the INDETERMINATE cap + propagating flags correctly bar a plain PROCEED. No single flag rises to a halt condition (flags propagate; only mechanical failures halt). Position DO-NOT-ADD is arithmetically supported (CMP ~Rs2,448 is 30-43% above the Rs1,400-1,700 entry). No flag needs to escalate. PASS.

---

## VERDICT

**COMPLETE.**

All three audits pass. Coverage: both A2 ledgers reconcile to a fresh independent enumeration (18 notes, 60 line items, 4 zero-standing, 10 auditor paras, 1 entity, 1 agenda, 5 signature blocks; presentation 2/42/14/12/12/2/3/2/3) with zero orphan rows and every flagged row reflected in A4. Arithmetic: every headline, delta, margin, tax, EPS-spread and bridge figure recomputes to A4's value within rounding; the lone 0.01-Cr slip on Q1 FY26 Operating EBITDA (10.52 vs 10.51) and the 1-bp YoY-bps difference are sub-rounding and decision-irrelevant. Adversarial: the three strongest bull claims each have a real bear counter, but all are already grafted into A4 — no surviving un-incorporated counter. Role 5 N/A, INDETERMINATE cash conversion, zero-standing lines, auditor nuance, and the PROCEED WITH FLAGS verdict are all correctly handled. Nothing loops back to A2, A3, or A4. Proceed to Notion save.

```yaml
stage: A5-adversary
company: "E2E"
quarter: "q1fy27"
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
