# A5 ADVERSARY / COMPLETENESS AUDIT — KRN Heat Exchanger (KRN) — Q1 FY27

Doctype: results (Q1 FY27 unaudited). Role 5 (concall/presentation) legitimately N.A.; confirmed
no concall content fabricated (review states Role 5 N.A. at lines 24-27, 3; no utilisation/customer
number is presented as concall-sourced — all such items carried as UNKNOWN/monitorable).

Fresh context. I re-derived every number from the A1 extract (Lakhs x0.01 = Rs Cr) and re-ran the
enumeration independently against the A2 ledger. I did not defer to A4's or A3's cites.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

| Brief part | Location | Present? | Content check |
|---|---|---|---|
| (1) Summary narrative | 5A, L588-616 | present | ~26 lines, numbers-first, symmetric bull/bear; real content |
| (2) SECTOR intelligence | 5B, L618-636 | present | industry, input exposure, export cycle, payer mix, non-disclosures |
| (3) BUSINESS-MODEL intelligence | 5C, L638-658 | present | revenue model, unit economics, model drift, balance-sheet, non-disclosures |
| (4) COMPETITION intelligence | 5D, L660-679 | present | wins, structural risks, peers (Notion-provenanced), DC risk |

Gate 0: PASS. All four labelled parts present and non-empty.

---

## AUDIT 1 — COVERAGE (fresh enumeration vs A2 ledger)

Fresh grep + manual sweep of the 13-page extract, diffed against the A2 count test.

| Category | A2 count | My fresh count | Orphan / delta | Status |
|---|---|---|---|---|
| Numbered notes | 18 | 18 (9 consol L180-243 + 9 SA L472-532) | none | match |
| Board agenda items | 3 | 3 (results, cost auditor, internal auditor; L39-64) | none | match |
| P&L line items | 63 | 63 (35 consol C + 28 SA D) | none | match |
| Zero-standing rows | 51 | 51 (C9,D6,H1-9,I1-9,F2-4,F3-4,F5-4,F6-4,M1-1,M2-1) | none | match |
| Segment rows | 36 | 36 (18 consol H1 + 18 SA I1) | none | match |
| Export-country rows | 22 | 22 (14 consol H2 + 8 SA I2) | none | match |
| Auditor paragraphs | 16 | 16 (10 consol J + 6 SA K) | none | match |
| Consolidated entities | 2 | 2 (KRN HVAC Products; Thermotech Research Lab; L367-368) | none | match |
| Annexure-II sub-rows | 8 | 8 (2 blocks x 4; L657-730) | none | match |
| Signature blocks | 5 | 5 (CS + 2 auditor + 2 unnamed board placeholders) | none | match |

**Enumeration counts reconcile exactly. No row my fresh pass found is missing from the ledger
(no A2 loop-back).** Standalone AND consolidated both present in the review (Steps 1A/1B consol,
1C/1D standalone). Zero-value lines preserved (NCI rows, Other Equity, Inter-Segment, Overseas
segment result — all carried, none dropped). Auditor Other-Matters paragraph treated verbatim
(F4, L379-390 -> review L81-84). Board Outcome agenda items 2 and 3 assessed (F13; review L71-74,
Q10, monitorable 7). Every forward-signal/ambiguous finding became a management question
(F1->Q1, F6->Q2, F4->Q3, F2->Q4/Q5, F12->Q6, F8->Q7/Q8, F9->Q9, F13->Q10, F14->Q13).

### COVERAGE FAIL — one orphan finding (loop back to A3)

A2 flagged **FIGURE_MISMATCH x4** and expressly left them "for A3/A4 reconciliation — not resolved
by A2" (ledger L318-320, L407-411). The four are:
- (i) consol PAT 3,289.56 (L150/L160) vs Profit-for-period 3,269.56 (L139)
- (ii) standalone Prior-Period/Exceptional sign vs consolidated FY sign
- (iii) standalone Income-Tax short/excess sign (-302.65) vs consolidated (+302.65)
- (iv) **standalone SEGMENT "Profit Before Exceptional Items & Tax" FY26 = 9,191.08 Lakhs (L564)
  vs standalone P&L "Profit Before Prior Period and Exceptional Item" FY26 = 9,111.66 Lakhs (L434)
  — a Rs 0.79 Cr (79.42 Lakh) discrepancy.**

A4 asserts (L20) "FIGURE_MISMATCH x4 (all resolved into F14/F8)" and (L134, L539) that there are
"**three** internal arithmetic inconsistencies." Mismatches (i)/(ii)/(iii) are genuinely resolved
into F14/F8 and confirmed by my recompute below. **Mismatch (iv) is not addressed anywhere in the
review** — the figure 9,191.08 never appears (grep-confirmed), F14 is scoped to exactly three items,
and no "reviewed, no finding" disposition is given. Both figures foot to the same true PBT
(9,151.37 Lakh: P&L 9,111.66 + 39.71; segment 9,191.08 − 39.71), so it is the *same* exceptional-item
handling inconsistency surfacing inside the standalone entity — which makes it a FOURTH instance of
the very drafting-control weakness F14 is built to flag, and therefore material to that finding, not
ignorable. A4's "x4 all resolved" and "three inconsistencies" claims are internally contradictory and
one flagged row is orphaned.

This is a missed forensic disposition -> **loop back to A3** to disposition FIGURE_MISMATCH (iv)
(then A4 to correct the "three inconsistencies"/"x4 resolved" wording and, if desired, add it to Q13).

---

## AUDIT 2 — ARITHMETIC (independent recompute from raw Lakhs)

Every derived cell in Steps 1B/1D/1.5/2/4 recomputed from the extract. Representative results:

| Metric | A4 value | My recompute (source) | Status |
|---|---|---|---|
| Consol PAT Q1FY27 (true) | 32.90 | 4,233.08 − 943.52 = 3,289.56 -> 32.90 (L133/L138); EPS 5.20 x 632.6L = 3,289.5 cross-check | CONFIRM |
| Line-139 PAT typo | 32.70 is typo, 32.90 true | L139 prints 3,269.56; reconciles only at 3,289.56 (L150/L160) | CONFIRM (typo real) |
| Q1FY26 consol total tax | 5.87 true vs printed 5.67 | 537.61+49.21 = 586.82; PBT 1,828.90 − PAT 1,242.08 = 586.82 -> 5.87; L138 prints 566.82 | CONFIRM (typo real) |
| FY26 consol short/excess sign | must be −3.03 (credit) | 2,382.39+69.09−302.65 = 2,148.83 -> PBT 9,795.57 − PAT 7,646.74 = 2,148.83; +302.65 would not foot | CONFIRM (sign error real) |
| Consol Op EBITDA Q1FY27 | 49.06 | 42.33+6.47+3.04−2.78 = 49.06 (L133/128/127/118) | CONFIRM |
| Consol Op EBITDA margin Q1FY27 | 19.44% | 49.06/252.32 | CONFIRM |
| Consol ETR Q1FY27 | 22.30% | 9.44/42.33 = 22.30% | CONFIRM |
| Consol ETR Q1FY26 (reconciled) | 32.09% | 5.87/18.29 = 32.09% (uses true 5.87, not misprinted 5.67) | CONFIRM |
| Consol PAT margin Q1FY27 | 13.04% | 32.90/252.32 | CONFIRM |
| Consol revenue YoY | +118.9% | (252.32−115.28)/115.28 = 118.9% | CONFIRM |
| Consol core-PBT YoY | +168.9% | (39.55−14.71)/14.71 = 168.8% | CONFIRM |
| Consol PAT YoY | +164.9% | (32.90−12.42)/12.42 = 164.9% | CONFIRM |
| SA Op EBITDA margin Q1FY27 | 13.56% | (25.04+0.72+1.33−2.42)/181.97 = 24.67/181.97 | CONFIRM |
| SA Op EBITDA margin YoY | −374 bps | 13.56% − 17.30% | CONFIRM |
| SA revenue YoY | +59.1% | (181.97−114.40)/114.40 = 59.1% | CONFIRM |
| SA ETR Q1FY27 | 25.48% | 6.38/25.04 (current 641.75 + def −4.23 = 637.52) | CONFIRM |
| SA PAT YoY | +19.0% | (18.67−15.69)/15.69 = 19.0% | CONFIRM |
| Revenue gap Q1FY27 (C−SA)/SA | +38.66% | (252.32−181.97)/181.97 | CONFIRM |
| Revenue-gap swing | +49.8pp | 38.66 − (−11.18) | CONFIRM |
| PAT gap Q1FY27 (C−SA)/SA | +76.2% | (32.90−18.67)/18.67 = 76.2% | CONFIRM |
| Subsidiary PAT / consol PAT | 43.2% | 14.23/32.90 (L383: 1,422.72) | CONFIRM |
| Subsidiary income / consol income | 65.5% | 167.19/255.09 (L382) | CONFIRM |
| Consol PAT bridge residual | < 0.01 | +31.47−4.28−2.35−0.80−3.57 = 20.47 = 32.90−12.42 | CONFIRM |
| SA PAT bridge residual | ~0.00 | +4.88+0.22−0.70−0.32−1.10 = 2.98 = 18.67−15.69 | CONFIRM |
| Export mix consol | 20.8% | 5,237.70/25,231.70 | CONFIRM |
| Export mix standalone | 15.0% | 2,733.51/18,197.15 | CONFIRM |

**No arithmetic error found in A4. All derived metrics, both entities, all four columns, reconcile
within rounding.** The three keying-error typos A4 claims (line-139 consol PAT; Q1 FY26 consol tax
component sum; FY26 consol income-tax sign) are each independently CONFIRMED real, and A4's treatment
(use true 32.90; reconcile ETR on true 5.87; treat FY26 short/excess as a credit) is correct.

Minor note (not a fail): the FY26 consol total-tax line prints 2,148.63 Lakh while the reconciled
value is 2,148.83 Lakh (0.20 Lakh = Rs 0.002 Cr); rounds to 21.49 Cr either way, immaterial, and
A4 uses 21.49 correctly.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims, strongest bear counter each)

| # | A4 positive claim | Strongest bear counter from the SAME extract | Survives? | Already in A4? |
|---|---|---|---|---|
| 1 | Consol revenue +118.9% YoY is "real operating growth, not treasury" (OI fell) | ~Rs 24.5 Cr is intra-group trading (SA stock-in-trade 33.75 > consol 9.21, L425/L122) and 65.5% of group income sits in unaudited, management-furnished subsidiary numbers (auditor Other-Matters L379-388) — headline growth quality is not independently verifiable | YES | YES — F1/F4, Steps 1.5/2C, Q1/Q3/Q4 |
| 2 | Consol Op-EBITDA margin +417 bps to 19.44% = genuine expansion | Standalone (the only auditor-reviewable operating entity) margin CONTRACTED −374 bps to 13.56% (L420-441); the group margin gain is entirely subsidiary-attributed and the subsidiary is unaudited | YES | YES — Step 2B item 2, 6D row 4 |
| 3 | Subsidiary flipped to +14.23 Cr PAT (43.2% of group); growth trigger ON TRACK | The 14.23 Cr is management-furnished/unaudited (L383, L386-388); no cash-flow confirms conversion (CFO ND, INDETERMINATE); and Rs 143.18 Cr of the subsidiary-directed QIP cash sits idle in FDs/Bonds (L234-236), inconsistent with a working-capital-constrained ramp | YES | YES — F4/F6, Step 4, Step 8C, Q2/Q3 |

**All three strongest bear counters are already grafted into A4's review.** No NEW surviving bear
counter needs incorporation. The review is adversarially symmetric. No A4 loop-back on this axis.

Independence / provenance checks (all PASS): INDETERMINATE cash conversion is NOT resolved to a clean
PROCEED — capped at PROCEED WITH FLAGS with the missing evidence (no Q1 CFO) named (L358-363, 5A).
Notion prior-period figures (Q3 FY26 rev 153.23; ~Rs 200 Cr net cash; 24-Jul Rs 43.11 Cr order) are
each explicitly marked "provenance: Notion, not this filing" and never asserted as this-quarter fact.
Verdict PROCEED WITH FLAGS is consistent with the evidence.

---

## VERDICT

**INCOMPLETE.**

- loop_back_to: **A3**
- gap: A2 FIGURE_MISMATCH (iv) is orphaned. Standalone SEGMENT "Profit Before Exceptional Items &
  Tax" FY26 = 9,191.08 Lakh (extract L564) vs standalone P&L "Profit Before Prior Period and
  Exceptional Item" FY26 = 9,111.66 Lakh (extract L434) — a Rs 0.79 Cr discrepancy A2 explicitly left
  for A3/A4 reconciliation (ledger L318-320, L407-411). A4 asserts "FIGURE_MISMATCH x4 (all resolved
  into F14/F8)" (review L20) and "three internal arithmetic inconsistencies" (review L134, L539), but
  only three are dispositioned; the fourth is never cited or resolved (9,191.08 appears nowhere).
  A3 must disposition (iv) as a finding — it is a fourth instance of the F14 drafting-control weakness,
  so F14's "three" undercounts — after which A4 corrects the "three/x4" wording and may fold it into
  Q13. Everything else (deliverable gate, full enumeration, all arithmetic both entities, adversarial
  symmetry, cash-INDETERMINATE handling, Notion provenance) PASSES.

```yaml
stage: A5-adversary
company: "KRN"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows:
    - "FIGURE_MISMATCH(iv): SA segment PBExcep&Tax FY26 9,191.08L (L564) vs SA P&L 9,111.66L (L434), Rs 0.79 Cr; A2-flagged, never dispositioned by A3/A4"
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: "A3"
gap: "A2 FIGURE_MISMATCH (iv) orphaned: standalone segment-note Profit Before Exceptional Items & Tax FY26 = 9,191.08 Lakh (L564) vs standalone P&L Profit Before Prior Period and Exceptional Item FY26 = 9,111.66 Lakh (L434), a Rs 0.79 Cr gap left by A2 for reconciliation. A4 claims all four FIGURE_MISMATCHes resolved into F14/F8 and cites only 'three' arithmetic inconsistencies; the fourth is never addressed (9,191.08 absent). A3 must disposition it as a fourth instance of the F14 drafting-control weakness."
```
