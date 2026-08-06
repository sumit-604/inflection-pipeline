# A5 ADVERSARY / COMPLETENESS AUDIT — The Anup Engineering Limited (ANUP) — Q1 FY27 (RE-AUDIT)

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Fresh context: A4 review + A1 extracts + A2 ledgers only.
Re-audit after A4 applied two surgical fixes flagged by the prior A5 pass. Every number below re-derived
independently from the raw Lakhs extracts (×0.01 → Rs Cr). I do not defer to A4's or A3's cites.

---

## PRIOR-GAP RE-VERIFICATION (the two fixes under test)

**Prior gap 1 — standalone Q4 FY26 gross margin must read 47.85%.** RE-DERIVED FROM RAW:
(19,480.07 − 9,277.15 − 881.69) / 19,480.07 = 9,321.23 / 19,480.07 = **0.47850 = 47.85%**
(results L158 / L164 / L165, 31.03.2026 column). A4 now prints 47.85% in BOTH the derived-metrics
table (review L95) and the explanatory note (review L97). **RESOLVED.** (Prior value had been the
erroneous carry from the Q1 column; the Q4-column re-derivation is now correct and internally consistent.)

**Prior gap 2 — finding A3-16 (drafting inconsistencies, NEUTRAL-FACT) must be cited/accounted in the
review body.** A3-16 now appears in three places: the incorporation roster (review L24), an explicit
paragraph in Section C — Combined Verdict that names each sub-item ("Air-Cooled" vs "Air-Cool",
"Desai Lay"/"Lay Desai" signatory flip, the "Comparison on a YoY basis" header with no comparative
column) and pairs it with F14-01 as a single cumulative NEUTRAL-FACT drafting/governance data point
(review L439), and the flags block (review L549). **RESOLVED.**

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

PLAIN-LANGUAGE BRIEF present at review L466-486, all four labelled parts present and carrying real content:

| Part | Heading | Location | Content check | Status |
|---|---|---|---|---|
| 1 | Summary narrative | L468-474 | 3 substantive paragraphs; revenue/margin/PAT collapse, trigger logic, wait-for-Q2 | PRESENT |
| 2 | Sector intelligence | L476-478 | static process equipment; demand air-pocket; capex-cycle framing; steel-input risk | PRESENT |
| 3 | Business-model intelligence | L480-482 | engineer-to-order; utilisation + WC economics; capacity/debt-ahead-of-volume | PRESENT |
| 4 | Competition intelligence | L484-486 | code/metallurgy/single-piece moat; KRN peer deferred; WC-discipline weakness | PRESENT |

**Gate: PASS.** No placeholder, no empty section.

---

## AUDIT 1 — COVERAGE (fresh independent enumeration vs A2 ledgers)

Fresh grep/sweep pass over each A1 extract, diffed against the A2 count-tests:

| Category | A2 count | My fresh count | Method | Orphan rows | Status |
|---|---|---|---|---|---|
| Results — numbered notes | 13 | 13 (6 std L227-256 + 7 consol L436-471) | structural read | none | OK |
| Results — line items | 71 | 71 (33 std + 33 consol + 5 Note-6 subtable) | table read L157-200/L365-408/L457-465 | none | OK |
| Results — auditor paras | 11 | 11 (5 std L88-138 + 6 consol L295-350) | numbered-para read | none | OK |
| Results — entities | 2 | 2 (Anup parent L323 + Mabel L324) | para-4 read | none | OK |
| Results — signatures | 5 | 5 | signatory read | none | OK |
| Results — agenda items | 1 | 1 (sole board resolution) | cover-letter read | none | OK |
| PR — bulleted claims | 20 | 20 (`grep -c "•"` = 20) | fresh grep | none | OK |
| PR — section headers | 5 | 5 (fresh keyword grep, L49/67/84/121/135) | fresh grep | none | OK |
| PR — forward-looking | 13 | 13 (8 Outlook bullets ∪ 5 keyword-flagged) | union read | none | OK |
| PR — business numbers | 14 | 14 | table read | none | OK |
| Deck — slides | 26 | 26 (`^\[page N\]` grep = 26, pages 1-26) | fresh grep | none | OK |
| Deck — numbers | 217 | 217 (reconciliation trail accepted; OCR 8/8 no new tokens) | ledger method verified | none | OK |
| Deck — footnotes | 6 | 6 | table read | none | OK |

A4's LEDGER-RECONCILIATION PREAMBLE (review L13-27) reconciles against every ledger row 100% and
incorporates every A3 finding ID (Results F2-1/F6-1/F7-1/F8-1/F9-1/F11-1; PR A3-01…A3-19;
deck F16-01…F16-08/F6-01/F7-01/F14-01). Administrative/identifier numbers (BSE/NSE PINs, CIN, phone/fax,
UDIN) are non-material and reviewed-no-finding by construction. **No orphan ledger row (in ledger, absent
from A4). No row my fresh pass found that the ledger lacks.** Coverage: PASS.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw Lakhs ×0.01 → Rs Cr)

| Metric | A4 value | My recompute | Source lines (raw Lakhs) | Status |
|---|---|---|---|---|
| Std gross margin Q4 FY26 | 47.85% | 47.85% (=9,321.23/19,480.07) | L158/L164/L165 | **OK (prior gap 1 fixed)** |
| Std gross margin Q1 FY27 | 48.82% | 48.82% (=5,755.25/11,789.29) | L158/L164/L165 | OK |
| Std gross margin Q1 FY26 | 51.64% | 51.64% (=8,748.57/16,942.21) | L158/L164/L165 | OK |
| Std gross margin FY26 | 51.47% | 51.49% (=40,649.55/78,943.70) | L158/L164/L165 | OK (0.02pp, rounding) |
| Std Op EBITDA Q1 FY27 | 9.42 | 9.42 (1.2093+7.2714+1.4335−0.4974) | L173/L168/L167/L159 | OK |
| Std Op EBITDA margin Q1 FY27 | 7.99% | 7.99% (9.4168/117.8929) | derived | OK |
| Std Op EBITDA margin Q1 FY26 | 23.24% | 23.24% | derived | OK |
| Std Op EBITDA margin Q4 FY26 | 18.51% | 18.51% | derived | OK |
| Std Reported EBITDA margin Q1 FY27 | 8.41% | 8.41% (9.9142/117.8929) | derived | OK |
| Std ETR Q1 FY27 | 8.4% | 8.37% (10.12/120.93) | L180/L175 | OK |
| Consol ETR Q1 FY27 | 39.0% | 38.98% (36.42/93.44) | L388/L383 | OK |
| Std ETR Q1 FY26 / Q4 FY26 / FY26 | 25.9%/5.7%/20.6% | 25.9%/5.7%/20.6% | L180/L175 | OK |
| Std revenue YoY | −30.4% | −30.42% (117.89/169.42) | L158 | OK |
| Std Op EBITDA YoY | −76.1% | −76.1% | derived | OK |
| Std Op EBITDA margin YoY | −1,525 bps | −1,525 bps (7.99−23.24) | derived | OK |
| Std finance-cost YoY | +69.1% | +69.1% (143.35/84.78) | L167 | OK |
| Std depreciation YoY | +14.3% | +14.3% (727.14/636.15) | L168 | OK |
| Std other-income YoY | −78.2% | −78.2% (49.74/228.34) | L159 | OK |
| Std core PBT ex-OI Q1 FY27 | 0.71 | 0.71 (120.93−49.74) | L175/L159 | OK |
| Std core PBT ex-OI YoY | −97.8% | −97.8% | derived | OK |
| Consol revenue YoY | −28.5% | −28.52% (125.25/175.23) | L366 | OK |
| Consol Op EBITDA margin YoY | −1,547 bps | −1,547 bps | derived | OK |
| Consol PAT YoY | −97.8% | −97.83% (0.57/26.26) | L390 | OK |
| Std QoQ revenue off Q4 | −39.5% | −39.48% (117.89/194.80) | L158 | OK |
| PAT bridge closes to | −24.42 | −24.42 (110.81−2,553.14 lk) | L182 | OK (all bridge legs tie, see below) |
| Std-vs-consol PAT gap Q1 FY27 | −48.5% | −48.5% (57.02/110.81) | L390/L182 | OK |
| Mabel Q1 FY27 (consol−std) PAT / revenue | ~−0.54 loss / ~7.4 | −0.54 (0.57−1.11) / 7.36 (125.25−117.89) | L390/L182, L366/L158 | OK |
| Net worth tie (consol) | 691.01 | 691.01 (670.98 + 20.03) | L405/L404 | OK |
| Share base | 2.003 Cr | 2.003 Cr (2,003.15 lk / ₹10) | L196/L404 | OK |
| Consol core PBT ex-OI FY26 | 137.62 (bex) | 137.62 (140.75−3.13, bex) | L381/L367 | OK |

**PAT bridge leg-by-leg (std YoY, review Step 4):** gross profit −29.94 (A4 −29.93); employee drag −0.79;
other-expense credit +0.76; → Op EBITDA −29.96; depreciation drag −0.91; finance drag −0.59; other-income
drag −1.79 (A4 −1.78); → PBT −33.24; tax credit +8.82; exceptional 0.00; → PAT −24.42. All legs tie within
rounding; the bridge sums exactly to the reported −24.42.

**Two documented non-gating observations (shown for transparency; neither reaches the FAIL threshold):**

1. **Std FY26 core PBT ex-OI carries a stray "(bex)" tag but is computed on the reported base.** A4 prints
   132.40 (review L91), which equals reported PBT 135.70 − OI 3.30 (i.e. matches the row's literal formula
   "PBT − OI"). A before-exceptional read would be 137.00 − 3.30 = 133.70. The consolidated table uses the
   before-exceptional base (137.62). So the two tables tag "(bex)" but use different bases. The standalone
   number is correct against its own stated formula; the discrepancy is a 1.30 Cr labelling inconsistency on a
   FY26 comparative context figure that feeds no trigger, no verdict, no YoY-collapse line and no brief.
   Non-material; does NOT gate. A4 may optionally relabel or align the two bases for hygiene.

2. **PR-vs-deck EBITDA figure inconsistency (₹9.2 Cr vs ₹9.5 Cr).** Press release L68 states consolidated
   EBITDA "₹9.2 Cr"; the deck states "9.5" (slide 8 L195; slide 10 L242, misspelled "EBIDTA"). My recomputed
   consolidated operating EBITDA is 9.47 Cr, i.e. the deck's 9.5 is right and the PR's 9.2 is the ~₹0.3 Cr
   outlier. A4 surfaced BOTH figures side-by-side (R5 Step 1 claim #1, review L363) and uses the correct 9.47/9.5
   throughout its own tables, so the analysis is not corrupted and neither ledger row is orphaned. A4 did not,
   however, explicitly flag the PR-vs-deck delta as an inconsistency. It is materially trivial on a collapsed
   quarter and is of the same genus as the already-flagged drafting-inconsistency cluster (A3-16 / F14-01).
   Recommendation (optional, non-gating): fold the 9.2-vs-9.5 delta into the existing A3-16/F14-01 note.

No arithmetic mismatch above rounding on any decision-relevant metric. Audit 2: PASS.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims, strongest bear counter from the same extract)

The review is overwhelmingly bearish; the "positive" claims are the residual reassurances. For each I built the
strongest bear counter from the extracted text and checked whether it already lives in A4.

**Claim 1 — "Highest ever order booking … pending order book (incl. LOI) ₹985 Cr" (PR L74/L89; deck slide 14).**
Bear counter (from same text): the ₹985 Cr is LOI-blended, ~₹240 Cr is booked for FY28 (PR L89 / deck L332), so
FY27-executable is ~₹745 Cr — below the ₹800 Cr green line — and the discrete LOI value is not broken out, so the
"LOI<20%, OB>₹800 Cr" gate is uncomputable; the inquiry pipeline also fell ₹1,200→₹1,100 Cr (deck L334).
Counter SURVIVES — and is already grafted into A4 (checklist item 5 AMBER L248; QFM #4 L329; flags L546).
**No new graft required.**

**Claim 2 — Auditor conclusion UNMODIFIED (clean) on both standalone and consolidated (Notes 2; auditor paras 4/5).**
Bear counter (from same text): it is a review under SRE 2410 (moderate assurance, "not an audit", explicitly no
audit opinion — L111/L319), and neither report states whether Mabel's figures were independently reviewed vs
management-certified (consol report paras 1-6 silent; results ledger §7). Counter SURVIVES — already carried in A4
as the interpretive-gap flag (review L53) and QFM #6 (Mabel). **No new graft required.**

**Claim 3 — "Gross margin remains intact" / "net debt free" / capacity in place (PR L50, L116; deck L365).**
Bear counter (from same text): fuller standalone gross margin is 48.82% vs 51.64% = −282 bps (L158-165), so
"intact" holds only materials-only; "net debt free" (deck, no figure) sits against finance cost +69% YoY (L167);
Kheda is "fully operational" yet drove under-absorption, not run-rate lift. Counter SURVIVES — already grafted
(review L417-419 narrative-vs-numbers table; QFM #2/#14; flags L547). **No new graft required.**

**Adversarial result: every surviving bear counter is already incorporated in A4.** No new surviving counter must
be added before save.

---

## VERDICT

**COMPLETE.**

- Deliverable-completeness gate: PASS (all four brief parts present, real content).
- Coverage: PASS (fresh enumeration matches A2 on every category; zero orphan rows; nothing my pass found is
  missing from the ledgers).
- Arithmetic: PASS (every decision-relevant metric re-derived from raw Lakhs ×0.01 ties within rounding; PAT
  bridge closes exactly to −24.42).
- Adversarial: PASS (three strongest positive claims each carry a surviving bear counter, and all three are
  already incorporated in A4).
- Prior gap 1 (Q4 FY26 gross margin 47.85%): RESOLVED and independently re-derived.
- Prior gap 2 (A3-16 cited/accounted in review body): RESOLVED.

Two minor, non-gating observations are logged for optional A4 hygiene (stray "(bex)" tag on the standalone FY26
core-PBT-ex-OI figure; the PR ₹9.2 Cr vs deck ₹9.5 Cr EBITDA drafting delta). Neither corrupts any decision
metric, verdict, trigger, or brief, and neither meets the FAIL threshold. This review proceeds to Notion save.

```yaml
stage: A5-adversary
company: "ANUP"
quarter: "Q1 FY27"
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
```
