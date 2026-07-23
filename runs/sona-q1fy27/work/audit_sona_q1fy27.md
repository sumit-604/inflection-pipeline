# A5 ADVERSARY / COMPLETENESS AUDIT — Sona BLW Precision Forgings (SONACOMS) — Q1 FY27

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Date: 2026-07-23
Under audit: `review_sona_q1fy27.md` (A4 analyst). Re-derived independently from the three A1
extracts and the three A2 ledgers. A3 reasoning not consulted (fresh context); A4/A3 cites checked,
not deferred to. Unit basis re-applied from scratch: results filing Rs Mn (x0.1 to Cr); deck Rs mn
(x0.1) with order book Rs bn (x100); press release Rs Cr with order book Rs bn/mn.

---

## AUDIT 1 — COVERAGE (fresh enumeration vs A2 ledgers; then A2 rows vs A4)

### 1A. Fresh grep/sweep re-run vs A2 count-tests

| Doctype | Category | A2 count | My fresh count | Orphan / delta | Status |
|---|---|---|---|---|---|
| Results | notes | 14 (7 SA + 7 C) | 14 (SA L235/244/248/262/270/280/284; C L534/542/545/563/571/581/583) | none | PASS |
| Results | line_items | 65 (29 SA + 36 C) | 65 (SA P&L to L225; C P&L to L520 incl owners/NCI/OCI-attribution/translation rows) | none | PASS |
| Results | zero_standing | 8 | 8 (exceptional, tax-prior-yr, OCI-tax 0.00, total-reserves — both statements) | none | PASS |
| Results | agenda_items | 1 | 1 (single bundled SA+C results resolution, L28-31) | none | PASS |
| Results | auditor_paras | 9 (4 SA + 5 C) | 9 (SA 1-4; C 1-5, C para 5 = Other Matters) | none | PASS |
| Results | entities | 17 (1 holding + 16 subs) | 17 (Annexure 1, L427-445; Novelic India NEW, inc 28-Nov-2025) | none | PASS |
| Results | signature_blocks | 5 | 5 | none | PASS |
| Presentation | slides | 41 | 41 (`[page N]` markers 1-41, sequential, = formfeed/pdfinfo) | none | PASS |
| Presentation | numbers | 365 | 365 (accepted; category is a line-sweep, not per-number A4 citation) | none | PASS |
| Presentation | footnotes | 27 | 27 (11 note blocks + 4 "Product under development" + slide-25 unnumbered) | none | PASS |
| Presentation | entities | 39 | 39 (7 people + 2 exch + 6 JV/cust + 5 sources + 18 locations + self) | none | PASS |
| Presentation | guidance_statements | 8 | 8 (4 SOP timelines + 2 aspiration + disclaimer + definition-hedge) | none | PASS |
| Press release | disclosure_units | 51 | 51 (4 headline + 5 fin + 1 quote + 2 ops + 3 order + 16 ent + 3 fwd + 10 admin + 3 sig + 1 fn + 3 boiler + 0 zero) | none | PASS |

**Enumeration reconciles at every category across all three ledgers. No row my fresh pass found is
missing from a ledger → no FAIL routed to A2.**

### 1B. Every A2 ledger row cited in A4, or reviewed-no-finding?

Checked each flagged/material ledger row against the A4 narrative:

- Results notes 1-7, auditor Other-Matters para 5, sign-off-timing flags, NEW_ENTITY Novelic India,
  ZERO_STANDING lines, entity list → all surfaced (Step 0D, Step 4A, Q9, Q10). **Covered.**
- Presentation CHART_LABEL_AMBIGUOUS (slides 21/28/36), CAPEX_NOT_DISCLOSED, STALE_SOURCE_DATA
  (CRISIL 2021), POTENTIAL_MISREAD_AS_GUIDANCE (Guided-by-Values), BEV-44%-annualised,
  forex-in-revenue, SOP guidance rows → all surfaced (Step 5, Step 6B, Q3/Q4/Q6/Q8/Q11, Monitorables).
  **Covered.**
- Press-release STD_CONSOL_UNSPECIFIED (→PR-FD1/Q2), ORDER_COUNT_AMBIGUITY + MULTI_ORDER_BUNDLE
  (→Q7), UNSUBSTANTIATED_GEOGRAPHY_CLAIM (→Q7), POSSIBLE_DUPLICATE_ENTITY (→Q7),
  TEMPLATE_ARTIFACT/conference-call (→PR-FD5, L26/L412), EXTERNAL_REFERENCE_UNVERIFIED (→Q6),
  DOCTYPE_MISMATCH (→ noted in preamble L15). **Covered.**

**FAIL — ORPHAN ROW (coverage): the press-release `DATE_MISMATCH`, flagged CRITICAL by A2**
(`ledger_pressrelease_sona_q1fy27.md` Section 8, R1, and the bold "DATE_MISMATCH (critical)"
paragraph L155-161). The release body is datelined **"Gurgaon, India, April 30, 2026"** (extract
L64) while reporting the quarter **ended 30 June 2026** and signed **23 July 2026** — a dateline
that precedes the quarter it reports. A2 explicitly directs "A3/A4 should note [it] since it
signals a templating/QC gap in the disclosure process itself." Independent grep of the full 528-line
A4 review for `April | Gurgaon | dateline | 30, 2026` returns **zero hits**. The row is neither
cited nor marked reviewed-no-finding → **orphan.**

This is not trivial: A4 itself constructs Question 10 around "**cumulative governance data points**"
(auditor sign-off timing R-A3-F14-01 + note-only DENSO disclosure R-A3-F13-01). The stale April-30
dateline is a third QC/process-gap data point in that exact cluster — and A4 already surfaced the
analogous stale conference-call disclaimer (PR-FD5). Its omission understates the governance/
transparency read that feeds the TRUSTWORTHY-promoter check. **Loop back to A3** (the forensic layer
must raise the critical ledger flag as a finding for A4 to surface; if A3 did raise it inside
PR-FD1-13, then A4 listed-but-did-not-surface it and must graft it into the Q10 governance cluster).

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extract lines; independent of A4)

All recomputed from raw Rs Mn (x0.1). SA = standalone P&L (results L177-225); C = consolidated
(results L469-520). Focus metrics per the task are marked ★.

| Metric | A4 value | My recompute | Source lines (raw Rs Mn) | Status |
|---|---|---|---|---|
| ★ Consol Op EBITDA Q1FY27 (PBET+D&A+FC−OI) | 302.60 | 240.942+76.881+10.477−25.696 = **302.60** | C L481/478/477/471 | PASS |
| ★ Consol Op EBITDA Q1FY26 | 202.55 | 174.413+66.994+5.331−44.188 = **202.55** | C L481/478/477/471 | PASS |
| ★ Consol Op EBITDA margin Q1FY27 (/rev ops) | 23.26% | 302.60/1,301.20 = **23.26%** | C L469 | PASS |
| ★ Consol Op EBITDA margin Q1FY26 | 23.72% | 202.55/853.91 = **23.72%** | C L469 | PASS |
| ★ Consol EBITDA margin YoY | −46 bps | 23.256−23.720 = **−46 bps** | — | PASS |
| ★ Consol EBITDA margin, deck basis (/rev incl fx) Q1FY27 | 23.09% | 302.60/(1,301.20+9.169)=302.60/1,310.37 = **23.09%** | C L469/470 | PASS |
| ★ Consol EBITDA margin deck basis Q1FY26 | 23.80% | 202.55/(853.91−3.009)=202.55/850.90 = **23.80%** | C L469/470 | PASS |
| ★ Deck margin YoY | −71 bps ("~0.7% lower") | 23.093−23.803 = **−71 bps** | deck L682/690 | PASS |
| Consol core PBT ex-OI Q1FY27 / Q1FY26 | 215.25 / 130.23 | 240.942−25.696=**215.25**; 174.413−44.188=**130.23** | C L481/471 | PASS |
| Consol core PBT ex-OI growth YoY | +65.28% | (215.246−130.225)/130.225 = **+65.28%** | — | PASS |
| ★ Consol ETR Q1FY27 | 25.91% | 62.429/240.942 = **25.91%** | C L488/483 | PASS |
| ★ Consol ETR Q1FY26 | 26.34% | 43.530/165.239 = **26.34%** | C L488/483 | PASS |
| ★ Consol ETR Q4FY26 | 24.48% | 60.552/247.409 = **24.47%** | C L488/483 | PASS (within rounding; recompute 24.474% → 24.47 vs A4 24.48, 1 bp) |
| PAT total YoY | +46.67% | (178.513−121.709)/121.709 = **+46.67%** | C L490 | PASS |
| PAT owners YoY | +44.71% | (180.468−124.713)/124.713 = **+44.71%** | C L506 | PASS |
| Reported PBT YoY | +45.82% | (240.942−165.239)/165.239 = **+45.81%** | C L483/482 | PASS (within rounding; 45.813% → 45.81 vs A4 45.82, 1 bp) |
| Revenue from ops YoY | +52.38% | (1,301.20−853.91)/853.91 = **+52.38%** | C L469 | PASS |
| Revenue incl fx YoY | +54.00% | 1,310.37/850.90−1 = **+54.00%** | C L469/470 | PASS |
| Finance cost YoY | +96.53% | (10.477−5.331)/5.331 = **+96.53%** | C L477 | PASS |
| D&A YoY | +14.76% | (76.881−66.994)/66.994 = **+14.76%** | C L478 | PASS |
| Revenue QoQ | +3.48% | (1,301.20−1,257.50)/1,257.50 = **+3.48%** | C L469 | PASS |
| EBITDA margin QoQ | −144 bps | 23.256−24.702 = **−144 bps** | — | PASS |
| Owners PAT QoQ | −5.97% | (180.468−191.916)/191.916 = **−5.97%** | C L506 | PASS |
| ★ SA PAT Q1FY27 / Q1FY26 / Q4FY26 | 220.11/120.13/207.34 | 2,201.06/1,201.30/2,073.41 x0.1 = **220.11/120.13/207.34** | SA L202 | PASS |
| ★ S−C PAT gap Q1FY27 (of SA) | +18.90% | (220.106−178.513)/220.106 = **+18.90%** (Δ +41.60) | SA L202 / C L490 | PASS |
| ★ S−C PAT gap Q1FY26 | −1.31% | (120.130−121.709)/120.130 = **−1.31%** | SA L202 / C L490 | PASS |
| ★ S−C PAT gap swing Q1FY26→Q1FY27 | +20.2 pp | −1.314 → +18.897 = **+20.21 pp** | — | PASS |
| ★ S−C gap vs owners Q1FY27 | +18.02% | (220.106−180.468)/220.106 = **+18.01%** | SA L202 / C L506 | PASS (within rounding; 18.009% → 18.01 vs A4 18.02, 1 bp) |
| ★ SA ETR Q1FY27 (dividend shield) | 20.14% | 55.515/275.621 = **20.14%** | SA L200/194 | PASS |
| SA Other Income/PBT Q1FY27 | 29.67% | 81.783/275.621 = **29.67%** | SA L179/194 | PASS |
| Intragroup dividend (Note 6) | 59.46 Cr | 594.63 mn x0.1 = **59.46 Cr** | SA L282 | PASS |
| PAT bridge YoY (Op EBITDA +100.05, D&A −9.89, FC −5.15, OI −18.49, Exc +9.17, Tax −18.90) | ΣΔ = +56.80 | sum = **+56.79** (→ +56.80 rounding); ties to 178.513−121.709 = +56.80 | C L481/478/477/471/482/488 | PASS |
| Unreviewed-subs net loss / % of consol PAT | 2.98 Cr / −1.67% | 29.75 mn x0.1 = **2.98**; 2.975/178.513 = **1.67%** | C L373 / L490 | PASS |
| Order book EV share | 64% | 154/240 bn = **64.2%** | deck L513 | PASS |
| BEV revenue YoY | +107% | 4,355/2,106−1 = **+106.8%** | deck L683/684 | PASS |

**No arithmetic mismatch above rounding.** Three items differ from A4 by exactly 1 bp / 0.01 pp
(Consol Q4FY26 ETR 24.47 vs 24.48; Reported PBT YoY 45.81 vs 45.82; S−C-vs-owners gap 18.01 vs
18.02) — all rounding-boundary artifacts, at or below tolerance, not FAILs. Every focus metric
(S-vs-C PAT gap and its +20.2 pp swing, standalone 20.14% ETR, EBITDA margin YoY on both bases, the
PAT bridge) re-derives to A4's figure. **AUDIT 2 = PASS.**

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive A4 claims; strongest bear counter from same text)

A4 is already a bearish AVOID review, so the obvious counters to its positives are largely
pre-incorporated. Two of the three survive only as already-addressed; one surfaces a genuinely
unincorporated counter.

**Positive claim 1 — "Headline growth is operationally real; core operating PBT ex-OI +65% grew
FASTER than reported PAT; Other Income FELL, so the print is *the opposite of a treasury-flattered
one*"** (Step 2 diag 3, Step 4B, Section C).
- Bear counter (same text): A4's "operating EBITDA" and "core PBT ex-OI" are built as PBET+D&A+FC−OI,
  which **retains the net foreign-exchange line** (a treasury/FX item, separate from Other Income).
  Consolidated forex swung from **−3.009 Cr (Q1FY26, C L470) to +9.169 Cr (Q1FY27)** — a **+12.18 Cr
  favourable YoY swing**. Stripping it, core operating PBT ex-OI grows **(215.246−9.169)=206.08 vs
  (130.225+3.009)=133.23 = +54.7%, not +65.28%** — the FX swing accounts for ~10.6 pp of the
  headline "faster-than-PAT" growth. The deck itself concedes "**Revenue includes net gain from
  foreign exchange**" (deck L701). A4 raises forex only as a management *question* (Q3, quantify FX
  in revenue) but does **not** net it out of its own "operationally real / not treasury-flattered"
  conclusion — the two are internally inconsistent (a +12.18 Cr FX tailwind IS a treasury tailwind).
- **SURVIVES.** Extract-supported and unincorporated. **Must be grafted into A4:** the +65% core
  operating PBT growth includes a +Rs 12.18 Cr YoY forex swing; ex-forex the figure is ~+55%, and
  the revenue/EBITDA prints are partly FX-flattered — the "not treasury-flattered" characterisation
  should be qualified accordingly. **Loop back to A4.**

**Positive claim 2 — "Net cash ((1.06)x EBITDA); balance-sheet strength intact; deleveraging
corroborated by the India Ratings facility cut Rs 925→725 Cr"** (Step 5, Section C).
- Bear counter (same text): zero capex is disclosed anywhere in the deck (CAPEX_NOT_DISCLOSED,
  deck has no capex token) despite four dated SOP commitments; no Q1 cash-flow statement exists, so
  CFO/PAT is INDETERMINATE; net-debt/EBITDA uses a deck-**normalised** LTM EBITDA; FY26 FCF/PAT was
  −0.61x. "Net cash" is a point-in-time stock that says nothing about cash *conversion*.
- **Does NOT survive as new** — A4 already caps the verdict on INDETERMINATE cash conversion, flags
  zero-capex (P-A3-F17-01), cites FY26 FCF/PAT −0.61x, and names the missing evidence (Step 5, Q4,
  flags). Fully incorporated.

**Positive claim 3 — "The S-vs-C PAT gap is mechanical/explained, not a red flag per se;
consolidated is the honest number"** (Step 4A).
- Bear counter (same text): the standalone Rs 59.46 Cr intragroup dividend + 503 bps ETR shield
  will unwind when the dividend stops (future SA ETR steps back up ~500 bps), and the gap is a
  symptom of a **net-dilutive, loss-making subsidiary layer** (unreviewed overseas subs −2.98 Cr
  C L373; NCI −1.96 Cr C L507) — a structural drag, not merely an accounting elimination; the press
  headline PAT basis is unlabeled (STD_CONSOL_UNSPECIFIED).
- **Does NOT survive as new** — A4 already names both drivers (dividend elimination AND subsidiary
  drag), flags the unlabeled press basis (PR-FD1), and routes the ETR-unwind/recurrence to Q2.
  Fully incorporated.

---

## VERDICT

**INCOMPLETE.** Two gaps block save:

1. **[Loop back to A4] — Surviving bear counter, unincorporated.** A4's central positive conclusion
   ("core operating PBT +65% … operationally real … the opposite of a treasury-flattered print")
   embeds a **+Rs 12.18 Cr favourable YoY forex swing** (consol forex −3.009 Cr Q1FY26 → +9.169 Cr
   Q1FY27, results C L470; deck L701 concedes forex is inside revenue). Ex-forex, core operating PBT
   grows **~+55%, not +65.28%**, and the revenue/EBITDA prints are partly FX-flattered. A4 raises
   forex only as a management question (Q3) and does not net it out of its own quality conclusion.
   Graft the FX-neutral figure and qualification before save.

2. **[Loop back to A3] — Orphan ledger row.** The press-release **`DATE_MISMATCH`** (flagged CRITICAL
   by A2: body datelined "Gurgaon, India, **April 30, 2026**", extract L64, for a quarter ended
   30 Jun 2026, signed 23 Jul 2026) appears **nowhere** in A4's 528-line review — neither cited nor
   marked reviewed-no-finding. It is a QC/process-gap governance data point belonging to A4's own
   Q10 "cumulative governance data points" cluster (alongside the auditor sign-off timing and the
   note-only DENSO disclosure). A3 must raise it as a finding for A4 to surface; if A3 already raised
   it inside PR-FD1-13, A4 listed-but-did-not-surface it and must graft it into the Q10 cluster.

Arithmetic (Audit 2) fully passes; enumeration (Audit 1A) fully reconciles at every category — no
FAIL to A2. Only COMPLETE proceeds to Notion save; this run does not.

```yaml
stage: A5-adversary
company: "SONACOMS"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows:
    - "press-release DATE_MISMATCH (CRITICAL, A2 ledger Sec 8/R1): body dateline 'Gurgaon, India, April 30, 2026' (extract L64) for quarter ended 30-Jun-2026, absent from A4 (no cite, no reviewed-no-finding); belongs in Q10 governance cluster"
  missing_from_ledger: []
arithmetic_mismatches: []   # all recomputes tie; 3 items differ by 1 bp (24.47 vs 24.48; 45.81 vs 45.82; 18.01 vs 18.02) = within rounding, not FAILs
surviving_bear_counters:
  - claim: "Core operating PBT ex-OI +65.28% grew faster than reported PAT; growth 'operationally real', 'the opposite of a treasury-flattered print' (Step 2 diag 3 / Step 4B / Section C)"
    counter: "A4's operating-EBITDA/core-PBT build (PBET+D&A+FC-OI) retains the net forex line; consol forex swung -3.009 Cr (Q1FY26) to +9.169 Cr (Q1FY27), a +12.18 Cr favourable YoY swing. Ex-forex core operating PBT grows ~+55%, not +65%; the print is partly FX-flattered (deck concedes revenue includes net FX gain). A4 raises FX only as management question Q3, never nets it out of its own quality conclusion."
    source_line: "results C L470 (forex 91.69 vs -30.09 mn); deck L701 ('Revenue includes net gain from foreign exchange'); A4 Step 2 diag 3 / Step 4B"
loop_back_to: "A4"
gap: "A4 must graft the FX-neutral qualifier: core operating PBT +65% includes a +Rs12.18 Cr YoY forex swing, ~+55% ex-forex, prints partly FX-flattered [A4]. Separately, the CRITICAL press-release DATE_MISMATCH (April-30-2026 dateline) is an orphan ledger row absent from A4 and must be surfaced in the Q10 governance cluster [A3]."
```
