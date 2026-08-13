# A5 ADVERSARY / COMPLETENESS AUDIT — Amagi Media Labs Ltd (AMAGI)
## Q1 FY27 (three months ended 30 June 2026)

Independence note: re-derived from `extract_results_amagi_q1fy27.txt` (804 lines) and
`ledger_results_amagi_q1fy27.md` only. A4's and A3's cites were checked, not trusted.
Unit convention: filing in Rs Millions; Rs Cr = Mn x0.1 (confirmed captions L197 standalone,
L452 consolidated). Every recompute below starts from raw Mn figures in the extract.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

The A4 review carries a `PLAIN-LANGUAGE BRIEF (MANDATORY)` block (review L396-417) with all four
labelled parts present and carrying real content:

| Brief part | Location | Present? | Non-empty / real content? |
|---|---|---|---|
| (1) Summary narrative | L398-399 | YES | ~20-line narrative, numbers-anchored; not a placeholder |
| (2) Sector intelligence | L401-405 | YES | CTV/FAST sector, provenance-tagged, filing vs Notion split |
| (3) Business-model intelligence | L407-411 | YES | asset-light SaaS, profit-locus in foreign subs, model-drift |
| (4) Competition intelligence | L413-417 | YES | peer frame, win/loss, US-concentration risk, undisclosed tests |

**Gate result: PASS.** All four parts present and substantive.

---

## AUDIT 1 — COVERAGE (fresh enumeration vs A2 ledger)

Fresh grep pass over the extract, diffed against the A2 COUNT TEST:

| Category | A2 count | My fresh count | Method / evidence | Orphan rows | Status |
|---|---|---|---|---|---|
| notes | 16 | 16 | 8 standalone (L246-296) + 8 consolidated (L541-594), topics 1-8 both statements | none | PASS |
| line_items | 52 | 52 | 22 standalone (L205-240) + 30 consolidated (L460-524) per documented sweep | none | PASS |
| zero_standing | 7 | 7 | SA: current tax, deferred tax, total tax, OCI tax-effect (L219-227) = 4; CONS: current tax-India, 2x OCI tax-effect (L476/485/489) = 3 | none | PASS |
| agenda_items | 4 | 4 | grep `^\s*[0-9]+\.` L33/40/48/76 → exactly 4 board resolutions | none | PASS |
| auditor_paras | 13 | 13 | SA report L134(I)/140/148/158/165 = 5; CONS report L326/333/340/353/382/391/411/425 = 8 | none | PASS |
| entities | 11 | 11 | grep roman markers L356-372 → (i)-(xi), 1 holding + 5 subs + 4 step-down + 1 trust | none | PASS |
| turns | 0 | 0 | results filing, no transcript | n/a | PASS |
| questions | 0 | 0 | n/a | n/a | PASS |
| mgmt_numbers | 0 | 0 | n/a | n/a | PASS |
| slides | 0 | 0 | no deck in doctype | n/a | PASS |

**No row my fresh pass found is missing from the ledger; no ledger count differs from mine.**

Ledger-row → A4-citation trace (every substantive row must be cited or "reviewed, no finding"):
- 16 notes → A4 Step 0D table (L38-48) + preamble L12. Cited.
- 52 line items / 7 zero-standing → A4 preamble L12 ("52 line items, 7 zero-standing rows … reviewed"); populate Step 1 tables. Cited.
- 4 agenda items → item 1 (results) = whole review; item 2 (MD re-appointment) L354/388/457; item 3 (MOA reclass) Tripwire 4 L266/387; item 4 (BMP secretarial auditor) L392/461. All 4 cited.
- 13 auditor paras → clean-opinion + Other-Matters treatment L48, F4 entity gap. Cited.
- 11 entities → entity-coverage-gap (F4-02, Q8 L338). Cited.
- Ledger `ENTITY_COVERAGE_GAP` flag → A4 F4-02 / Q8. Cited.
- Ledger `TEXT_ANOMALY` (consol Note 7 "standalone" copy-paste, L590) → A4 F14-01 (L45, incorporated list L14). Cited.
- Ledger `ZERO_STANDING` x7 → A4 preamble L12; nil-tax standalone treated at Step 1/Note 7. Cited.
- Ledger OCR caveats (consol FY26 EPS garble L516-534) → A4 L100 marks FY26 consol EPS `ND (OCR-garbled, A2 flag)`. Cited.

Minor, non-orphan: the ledger Section-2 note that the CS digitally signed 10:35:38, 38 seconds
after the stated meeting close (10:35 A.M.), is NOT surfaced in A4. The ledger itself resolved it
as "after, not before — no SIGNATURE_BEFORE flag," i.e. reviewed-with-no-finding, and signature
blocks are not one of the enumeration-gate COUNT-TEST categories. Benign; **not an orphan, not a FAIL.**

**COVERAGE AUDIT: PASS. No orphan rows (→ A3 clear). No rows missing from ledger (→ A2 clear).**

---

## AUDIT 2 — ARITHMETIC (recomputed from raw Mn, x0.1)

Sampled and recomputed every derived cell in Steps 1-4. Representative checks (all Rs Cr):

**STANDALONE derived (A4 L74-82):**
| Metric | A4 value | Recomputed | Source lines | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 (PBT+D+FC−OI) | 2.80 | 22.97+3.70+0.60−24.47 = 2.80 | L217/213/212/206 | OK |
| Op EBITDA Q1FY26 | (16.36) | −5.53+3.52+0.79−15.14 = −16.36 | same | OK |
| Op EBITDA margin Q1FY27 | 1.02% | 2.80/275.64 = 1.016% | L205 | OK |
| Op EBITDA margin Q1FY26 | (7.92%) | −16.36/206.53 = −7.92% | L205 | OK |
| Core PBT ex-OI Q1FY27 | (1.50) | 22.97−24.47 = −1.50 | L217/206 | OK |
| OI/PBT Q1FY27 | 106.5% | 24.47/22.97 = 106.5% | L206/217 | OK |
| PAT margin Q1FY27 | 8.33% | 22.97/275.64 = 8.33% | L222/205 | OK |
| ETR (all periods) | 0% | tax = nil (L219-221) | L221 | OK |

**CONSOLIDATED derived (A4 L104-112):**
| Metric | A4 value | Recomputed | Source lines | Status |
|---|---|---|---|---|
| Op EBITDA Q1FY27 (PBT+D+FC−OI) | 29.85 | 40.41+5.89+1.14−17.59 = 29.85 | L473/469/468/461 | OK |
| Op EBITDA Q1FY26 | (1.18) | 6.59+4.97+1.53−14.27 = −1.18 | same | OK |
| Op EBITDA margin Q1FY27 | 6.83% | 29.85/436.88 = 6.83% | L460 | OK |
| Op EBITDA margin Q1FY26 | (0.36%) | −1.18/330.06 = −0.357% | L460 | OK |
| Core PBT ex-OI Q1FY27 | 22.82 | 40.41−17.59 = 22.82 | L473/461 | OK |
| Core PBT ex-OI Q1FY26 | (7.68) | 6.59−14.27 = −7.68 | same | OK |
| ETR Q1FY27 | 16.1% | 6.50/40.41 = 16.09% | L479/473 | OK |
| ETR Q1FY26 | 40.2% | 2.65/6.59 = 40.2% | L479/473 | OK |
| ETR FY26 | 17.9% | 15.58/87.26 = 17.85% | L479/473 | OK |
| PAT margin Q1FY27 | 7.76% | 33.91/436.88 = 7.76% | L480/460 | OK |
| OI/PBT Q1FY26 → Q1FY27 | 216.5% → 43.5% | 14.27/6.59=216.5%; 17.59/40.41=43.5% | L461/473 | OK |

**STEP 2 YoY (A4 L123-153):**
| Metric | A4 value | Recomputed | Status |
|---|---|---|---|
| Consol revenue YoY | +32.4% | (436.88−330.06)/330.06 = 32.36% | OK |
| Standalone revenue YoY | +33.5% | 69.11/206.53 = 33.46% | OK |
| Consol Op EBITDA margin | +719 bps | 6.83−(−0.36) = 7.19pp | OK |
| Standalone Op EBITDA margin | +894 bps | 1.02−(−7.92) = 8.94pp | OK |
| Consol D&A YoY | +18.5% | 0.92/4.97 = 18.5% | OK |
| Consol finance YoY | (25.5%) | −0.39/1.53 = −25.5% | OK |
| Consol OI YoY | +23.3% | 3.32/14.27 = 23.3% | OK |
| Consol core PBT swing | +30.50 | 22.82−(−7.68) = 30.50 | OK |
| Consol reported PBT YoY | +513% | 33.82/6.59 = 513.2% | OK |
| Consol PAT YoY | +760% | 29.97/3.94 = 760.7% | OK |
| Consol EPS YoY | (56.7%) | −1.95/3.44 = −56.7% (flagged non-comparable) | OK |

**STEP 3 QoQ (A4 L163-175):**
| Metric | A4 value | Recomputed | Status |
|---|---|---|---|
| Consol revenue QoQ (Q4→Q1FY27) | +10.1% | 39.91/396.97 = 10.05% | OK |
| Consol core PBT QoQ | +40% | 6.52/16.30 = 40.0% | OK |
| Consol reported PBT QoQ | −0.3% | −0.13/40.54 = −0.32% | OK |
| Consol Op EBITDA QoQ | +25% | 5.98/23.87 = 25.05% | OK |
| Consol OI QoQ | −27.5% | −6.65/24.24 = **−27.4%** | rounding (0.1pp; NOT a FAIL) |

**STEP 4 PAT BRIDGE (A4 L185-193):** consol PAT +Rs 29.97 Cr YoY (33.91−3.94).
Op EBITDA +31.03 (29.85−(−1.18)); D&A −0.92 (5.89−4.97); finance +0.39 (1.53−1.14);
OI +3.32 (17.59−14.27); tax −3.85 (6.50−2.65). Sum = 31.03−0.92+0.39+3.32−3.85 = **+29.97**.
Bridge reconciles exactly. "~104% operating-led" = 31.03/29.97 = 103.5% (op-EBITDA share of PAT
change); "OI ~11%" = 3.32/29.97 = 11.1%. Both defensible characterizations. OK.

**Cross-checks on narrative numbers used in verdict/PLB:**
- Subsidiary PAT contribution: Q4FY26 = 34.26−19.70 = 14.56; Q1FY27 = 33.91−22.97 = 10.94 (10.93 from raw Mn 339.05−229.71=109.34). QoQ = −24.9% ≈ −25%. OK (10.93/10.94 = rounding-method artifact, immaterial).
- FX/OCI translation Q1FY27 = 91.24 Mn = Rs 9.12 Cr (L487). OK.
- Actuarial OCI loss = 29.86 Mn = Rs 2.99 Cr (L484); vs FY26 +7.21 Mn = +0.72 Cr. OK.
- FY26 deferred-tax credit = 150.70 Mn = Rs 15.07 Cr (L478). OK.
- Foreign taxes Q1FY27 = 58.50 Mn = Rs 5.85 Cr (L477). OK.
- Net-worth proxy = 1,081.70 + 16,486.39 = 17,568.09 Mn = Rs 1,756.8 Cr (L509/511). OK.
- Other-matters reliance: revenue 1,166.33/4,368.78 = 26.7% (OK); PAT 66.00/339.05 = 19.5% (A4/ledger cite ~19.4% — rounding, 0.1pp, NOT a FAIL).
- MOA headroom: authorised 49,45,02,731 − issued 21.634 cr = ~27.8 cr shares (L733/L232). OK.
- Statutory-ETR gap: 25.17% − 16.1% = ~907 bps ≈ "~900 bps" (L199). OK.
- Share base: 1,081.70/5 = 216.34 Mn sh vs 170.81/5 = 34.16 Mn sh = 6.33x ≈ "~6x" (L232/509). OK.

**ARITHMETIC AUDIT: PASS.** Two sub-rounding items only (consol OI QoQ −27.4% vs A4 −27.5%;
other-auditor PAT share 19.5% vs cited 19.4%). Both ≤0.1pp, within rounding — no FAIL. No metric
mismatch above rounding. (→ A4 clear on arithmetic.)

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims + strongest bear from same text)

**Positive claim 1 (Section C L372; PLB L399):** "a genuinely operating-led PAT of Rs 33.91 Cr …
the strongest quality-of-earnings print the thesis has seen."
- **Strongest bear from the extract:** the entire YoY "swing" is measured against a Q1FY26 base that
the auditor expressly did NOT review or audit — "compiled by the Management" (standalone review para 5,
L165-167; consolidated review para 8, L425-427; Note 2, L261-262/557-558). The flagship quality claim
therefore rests on an unassured comparator, and Q1FY26 PBT of Rs 6.59 Cr is small enough to make every
YoY % explosive.
- **Survives?** NO — already incorporated. A4 raises the unreviewed-base caveat at Step 0D (L40:
"Q1FY26 comparative was neither audited nor reviewed … weight QoQ and YoY accordingly") and diagnostic 1
(L148). The point is present in the review body; not a new, unincorporated counter.

**Positive claim 2 (Section C L372; Step 2 L148):** consol revenue "+32.4% YoY … real 30% grower …
above the 20% constant-currency tripwire floor."
- **Strongest bear from the extract:** the +32.4% is a REPORTED number. The operating engine is the
foreign (US-heavy) subsidiaries, and FX translation added Rs 9.12 Cr to OCI this quarter (L487) — a
material INR-depreciation tailwind. With Note 8 single-segment reporting (L295/593) disclosing no
constant-currency figure, a chunk of the "32%" could be currency, so "real 30% grower" is unproven and
possibly flattered.
- **Survives?** NO — already incorporated. A4 explicitly marks CC as `ND`, tags the revenue read AMBER
(L253), and repeatedly qualifies "on a reported basis; CC growth not disclosed" (L124, L148, L242).

**Positive claim 3 (Step 2 L132/150):** consol core operating PBT ex-OI "swung to +Rs 22.82 Cr …
the headline growth is real at group level."
- **Strongest bear from the extract:** the group's operating profit lives entirely in the foreign subs,
whose PAT contribution FELL −25% QoQ (Rs 14.56 → 10.94 Cr, derived L480/222), while the taxable Indian
parent's core is still −Rs 1.50 Cr ex-treasury (L143). The "real turn" is thus (a) already decelerating
at the exact entity that produces it, and (b) partly a nil-tax artifact of the Note 7 Indian shield.
- **Survives?** NO — already incorporated. A4 surfaces the −25% QoQ subsidiary softness (Q3 L333, PLB
competition L416), the standalone −Rs 1.50 Cr core (L143/150, flag), and the forward-ETR-normalisation
drag from the Note 7 shield exhausting (L199, F1/F8 flag).

**Adversarial result:** all three strongest bear counters are already grafted into A4 (body, flags,
questions, and verdict). **No surviving counter requires addition. (→ A4 clear.)**

---

## VERDICT

- Deliverable-completeness gate: **PASS** (all four brief parts present, substantive).
- Coverage audit: **PASS** (fresh counts match ledger exactly; no orphan rows; no rows missing from ledger).
- Arithmetic audit: **PASS** (all derived metrics reconcile; two ≤0.1pp sub-rounding items, no FAIL).
- Adversarial read: **PASS** (three strongest bear counters already incorporated; none survive as new).

**VERDICT: COMPLETE.** No loop-back. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "AMAGI"
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
