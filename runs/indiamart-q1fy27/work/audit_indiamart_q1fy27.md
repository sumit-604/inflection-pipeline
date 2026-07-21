# A5 ADVERSARY / COMPLETENESS AUDIT — IndiaMART InterMESH Limited (INDIAMART), Q1 FY27

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Date: 2026-07-21
Fresh context: I saw only the A4 review, the three A1 extracts, and the three A2 ledgers. Every number below re-derived independently from the A1 extracts at their line numbers; A4's cites checked, not trusted.
Unit discipline: results filing in INR **million** (x0.1 = Rs Cr); presentation and press release native **Rs Crore**.

---

## AUDIT 1 — COVERAGE

Fresh grep/manual enumeration re-run over each A1 extract, diffed against the A2 ledgers.

| Category | A2 count | My fresh count | Orphan / missing rows | Status |
|---|---|---|---|---|
| results — notes | 14 | 14 (5 consol numbered L415-437 + 6 standalone numbered L649-672 + 3 segment lettered fn L402-410) | none | PASS |
| results — line_items | 65 | 65 (21 consol L321-350 + 25 segment L367-400 + 19 standalone L618-643) | none | PASS |
| results — agenda_items | 2 | 2 (L17-25 results; L26-32 WOS) | none | PASS |
| results — auditor_paras | 16 | 16 (9 consol + 7 standalone, section-level; structure spot-verified) | none | PASS |
| results — entities | 13 | 13 (Annexure I L273-300; 5 subs + 8 assoc) | none | PASS |
| results — annexure_rows | 8 | 8 (Annexure B L693-726) | none | PASS |
| results — signature_blocks | 5 | 5 (Bagri L44; DCA consol L442; DCA std L677; Jones consol L244; Jones std L586) | none | PASS |
| results — zero_standing | 1 | 1 (inter-segment rev, accounting software, dash all periods L372) | none | PASS |
| presentation — slides | 69 | 69 (page markers L15→L2047) | none | PASS |
| presentation — numbers | 462 | 462 (methodology reconciled; spot-checked across slides 6-9, 34, 37-39, 43-47, 52, 67-68) | none | PASS |
| presentation — footnotes | 58 | 58 (52 numbered + 6 unnumbered; spot-checked) | none | PASS |
| pressrelease — headline_bullets | 3 | 3 (L70-72) | none | PASS |
| pressrelease — quantitative_claims | 26 anchors / 24 rows | 24 discrete rows / 26 anchors (rows 4,16 carry dual Rs anchors) — reconciled | none | PASS |
| pressrelease — line_items | 11 | 11 (T1-T11, L144-165) | none | PASS |
| pressrelease — mgmt_quotes | 1 | 1 (DCA, L112-117) | none | PASS |

**Orphan-row check (ledger rows absent from A4):** Every A2 SUMMARY FLAG is traceable into A4: SIGNATURE_BEFORE_MEETING_CONCLUDED → A4 flag 7 / Q16; ENTITY_UNAUDITED_MGMT_FURNISHED (MonotaRO stub) → flag 5 / Q11; ENTITY_CHANGE MonotaRO exit → flag 6 / Q1 / F15-01; NEW_ENTITY_PENDING (IndiaMART Finance) → flag 4 / Q2 / monitorable; ENTITY_AUDITED_BY_OTHERS (4 subs) → Step 0D; GOING_CONCERN_LANGUAGE boilerplate → Step 0D (A3 F5); presentation sign-convention/attrition-in-fine-print → F16-01/F16-02 / flag 10; Busy EBITDA-PAT divergence → Q7/Q8; CFO %-of-collections seasonal → Step 5 / Q18. The two immaterial template rows (ZERO_STANDING inter-segment revenue; ZERO_STANDING "proceeds from issue of shares" L1166) and the two cosmetic renames (Busy f/k/a Tolexo; Livekeeping f/k/a Finlite) plus the Fleetex w.e.f. 11-Apr-2025 addition are covered only by A4's blanket "no ledger row is unreviewed" preamble, not by a specific line — acceptable, as all are non-material and non-numeric. **No material orphan row. No row in my fresh pass that the ledger lacks.**

**COVERAGE STATUS: PASS.**

Two source-consistency observations (data quality, NOT count failures — logged for A3/A4, do not block save on their own):
- **OBS-C1 (deck-internal):** Unique Business Enquiries quarterly bars read 31→29→28→27→26 (L2030-2034), so Q1FY27 26 vs Q1FY26 31 = −16.1%, yet the same deck labels the YoY −11% (Operational Metrics table L1004; chart header L2024). The A2 KPI cross-ref caught the sign-convention issue but not this magnitude mismatch. A4 quoted the deck's −11% (did not recompute), so this is a source inconsistency for A3/A4 to reconcile, not an A4 computational error.
- **OBS-C2 (A4 specificity not in extract):** A4 monitoring item 2 asserts active buyers are in a "2nd consecutive decline (−3%→−5%)." The extract supports only the current Q1FY27 −5% YoY (L1002); the prior-quarter −3% YoY is not derivable from any supplied extract. Minor over-specification; A4 should cite its source or soften.

---

## AUDIT 2 — ARITHMETIC

Every A4 derived metric recomputed from raw extracted numbers.

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| Consol Op EBITDA Q1FY27 (PBTbefAssoc+D+FC−OI) | 146.5 | 246.3+6.4+0.5−106.7 = 146.5 | L332/328/327/322 | PASS |
| Consol Op EBITDA margin Q1FY27 | 35.4% | 146.5/414.4 = 35.35% | L321 | PASS |
| Std Op EBITDA Q1FY27 (PBT+D+FC−OI) | 149.3 | 234.3+2.6+0.5−88.1 = 149.3 | L628/625/624/619 | PASS |
| Std Op EBITDA margin Q1FY27 | 39.7% | 149.3/375.9 = 39.72% | L618 | PASS |
| Consol ETR Q1FY27 | 25.7% | 595/2317 = 25.68% | L339/334 | PASS |
| Std ETR Q1FY27 | 24.8% | 582/2343 = 24.84% | L632/628 | PASS |
| Consol ETR Q4FY26 | 36.0% | 282/784 = 35.97% | L339/334 | PASS |
| Consol Core PBT ex-OI Q1FY27 | 125.0 | 231.7−106.7 = 125.0 | L334/322 | PASS |
| Std Core PBT ex-OI Q1FY27 | 146.2 | 234.3−88.1 = 146.2 | L628/619 | PASS |
| Consol Core PBT ex-OI YoY | +12.1% | (125.0−111.5)/111.5 = 12.11% | L334/322 | PASS |
| Std Core PBT ex-OI YoY | +12.1% | (146.2−130.4)/130.4 = 12.11% | L628/619 | PASS |
| Consol Revenue YoY | +11.4% | (414.4−372.1)/372.1 = 11.37% | L321 | PASS |
| Std Revenue YoY | +8.5% | (375.9−346.3)/346.3 = 8.55% | L618 | PASS |
| Consol PAT YoY | +12.2% | (172.2−153.5)/153.5 = 12.18% | L341 | PASS |
| Std PAT YoY | +6.1% | (176.1−166.0)/166.0 = 6.08% | L633 | PASS |
| Std Op EBITDA margin ΔYoY | +80bps | 39.7−38.9 = +0.8pp | L618/628 | PASS |
| Consol Op EBITDA margin ΔYoY | −50bps | 35.4−35.9 = −0.5pp | L321/332 | PASS |
| Consol OI YoY | +15.5% | (106.7−92.4)/92.4 = 15.48% | L322 | PASS |
| Std OI YoY | +4.4% | (88.1−84.4)/84.4 = 4.38% | L619 | PASS |
| EPS diluted YoY consol / std | +11.9% / +5.8% | 3.04/25.52=11.9% ; 1.61/27.59=5.84% | L350/643 | PASS |
| Reported EBITDA consol Q1FY27 (incl OI) | 253.2 | 146.5+106.7 = 253.2 | L332/322 | PASS |
| S-vs-C PAT gap Q1FY26 / Q4FY26 / Q1FY27 / FY26 | 7.5 / 27.9 / 2.2 / 9.6% | 12.5/166.0=7.53; 19.4/69.6=27.87; 3.9/176.1=2.21; 50.5/525.2=9.61 | L341/633 | PASS |
| CFO/PAT single-q consol / std Q1FY27 | 0.95x / 0.87x | 163/172.2=0.947 ; 153/176.1=0.869 | deck L1160/1292; L341/633 | PASS |
| Rolling-12m CFO/PAT consol | ≈1.41x | (694−161+163)/(474.7−153.5+172.2)=696/493.4=1.410 | deck L1160/1107; L341 | PASS |
| Consol QoQ PAT / Std QoQ PAT | +243% / +153% | 172.2/50.2−1=243%; 176.1/69.6−1=153% | L341/633 | PASS |
| Deferred rev consol QoQ | +49 (1,965→2,014) | 2,014−1,965 = 49 | deck L1136 | PASS |
| Other Liabilities consol QoQ | +338 (169→507) | 507−169 = 338 | deck L1142 | PASS |

**All headline derived metrics reconcile within rounding.** One flagged discrepancy:

- **ARITH-1 (PAT bridge does not reconcile to its own stated total, Step 4A/4B).** The listed components do not sum to the stated ΔPAT on either basis:
  - Consol (Step 4A): +15.0 −2.1 +0.5 +0.5 +14.3 −0.5 −2.4 = **+25.3**, but the table's stated total is **+18.7** (a +6.6 Cr overstatement if read additively). Correct total is right (172.2−153.5 = 18.7 ✓).
  - Standalone (Step 4B): +13.3 +2.9 +0.9 +0.3 +3.7 −5.0 = **+16.1**, but stated total is **+10.1** (a +6.0 Cr overstatement). Correct total is right (176.1−166.0 = 10.1 ✓).
  - Cause: the bridge mixes a **pre-tax** gross-contribution line (revenue +42.3 × ~35% and a separate margin line) with a **rate-only** tax line (−2.4 / −5.0) instead of the full YoY tax delta (consol tax +9.1 Cr; std +9.4 Cr). A4 tags components "≈", and each individual estimate is internally defensible, but a reader treating the columns as additive is misled. This is a presentation/methodology defect, not a wrong headline number. **Loop to A4** to either reconcile the components to the total or state explicitly that the rows are non-additive rate-vs-base estimates. Not verdict-determinative on its own.

**ARITHMETIC STATUS: PASS on every headline derived metric; one non-additive-bridge defect (ARITH-1) for A4 to tidy.**

---

## AUDIT 3 — ADVERSARIAL READ

Three most positive claims in A4, each met with the strongest bear counter constructed from the SAME extracted text.

**Positive claim 1 — "Standalone operating EBITDA margin expanded to 40% / 39.7%, +80bps YoY, above the 30% thesis floor (monitoring item 5 GREEN)."**
Bear counter: the 40% headline is standalone-only (consol margin CONTRACTED −50bps to 35.4%), uses the more favourable of two coexisting deck figures (reported 40% vs "Adjusted EBITDA margin 41%", L1285), and does **not** yet absorb the unquantified remaining-state Labour Code employee-cost step-up (consol N5 / std N6, L428-437 / L663-672).
Survives? **NO — already incorporated.** A4 discloses the consol −50bps (Step 2A/diagnostic 2), flags the selective standalone framing (F16-a, Q6), and carries the Labour Codes cost as flag/Q12/monitorable (F6-02/F7-01). No graft required.

**Positive claim 2 — "Core operating PBT grew +12.1% on both bases, cleaner than headline PAT; the operating engine is genuinely strong."**
Bear counter: that +12.1% is realization-only growth on a **contracting** volume base — paying-supplier net −1,852 (L235), active buyers −5% (L1002), unique enquiries −11%/−16% (L1004 vs L2030-2034), Busy EBITDA margin 16%→9% (L1566); with the growth concentrated at the top (top-10% ARPU +10% vs blended +9%, L1016/L1014), this is late-cycle price compounding on an eroding base.
Survives? **NO — already incorporated, and it is A4's central thesis.** Step 6B (3 RED + 1 AMBER), Step 8C (single cleanest metric = net supplier adds), flag 2/3, and growth-trigger table all carry this. No graft required.

**Positive claim 3 — "Rolling CFO/PAT ≈1.41x elite / cash STRUCTURAL, and consol PAT +12.2% at/above base (record quarter)."**
Bear counter (SURVIVES): **the quality of the consolidated headline is materially overstated because the bulk of consolidated Other Income this quarter is UNREALIZED mark-to-market gain, and A4 leaves this un-quantified even though the deck discloses it.** From the deck's own Cash Generation table: realized non-operating income Q1FY27 = **Rs 16 Cr** (L1162, footnote 2 = realized treasury income + stake-sale gains), while the change in **unrealized** fair-value gain on treasury Q1FY27 = **Rs 96 Cr** (L1169). Consol Other Income was Rs 106.7 Cr (filing L322) — i.e. **~90% of consol Other Income (~Rs 96 Cr) is unrealized fair-value MTM**, equal to **~41% of consol PBT** (96 / 231.7) and, post-tax, ~Rs 71 Cr or ~41% of the Rs 172.2 Cr "record" consol PAT. Its reversibility is already demonstrated in the same series: Q4 FY26 consol Other Income printed **−Rs 33.9 Cr** (L322). A4 surfaces treasury dependence at a high level (flag 8 "consol PAT ~76% treasury-driven"; Step 2 diagnostic 6 "~46% of PBT, MTM-lumpy") but treats the interest-vs-dividend-vs-MTM split as an **open question for management** (Q9 asks management to "break down the composition… fair-value MTM"), when the extract (L1162 + L1169) already answers it. The stronger, extract-grounded bear reading — that roughly two-fifths of record consolidated PAT is unrealized, non-cash, and reversible — is absent from A4 and must be grafted.
Reinforcing leg (same claim): consolidated CFO grew only **+2% YoY** (161→163, deck L1107/L1907) against consol PAT **+12.2%** — a **same-season** (Q1-vs-Q1) conversion deterioration that seasonality does not explain; A4 attributes the cash softness to seasonality/advance-collection timing without addressing the like-for-like YoY divergence.

Survives? **YES.** The Rs 96 Cr unrealized-MTM composition (L1162/L1169) is a specific, material, extract-derivable bear fact not stated in A4, and it upgrades A4's Q9 from "please disclose composition" to "composition is already disclosed and ~90% is unrealized." **Must be grafted into A4 (loop to A4).**

---

## VERDICT

**INCOMPLETE.** Loop back to **A4**.

Exact gap: A4 must graft the surviving bear counter under Adversarial claim 3 — that per the deck's own Cash Generation table, ~Rs 96 Cr of the Rs 106.7 Cr consolidated Other Income this quarter is **unrealized fair-value MTM gain** (realized non-operating income only Rs 16 Cr, L1162; Δ fair-value gain on treasury Rs 96 Cr, L1169), equal to ~41% of consol PBT and ~41% of the Rs 172.2 Cr record consol PAT, and demonstrably reversible (Q4 FY26 consol OI −Rs 33.9 Cr, L322). A4 currently poses this composition as an unanswered management question (Q9) rather than stating the extract-disclosed answer; the quantified, reversible-MTM framing must be added to flag 8 / the combined verdict before save. Secondary items for the same loop: reconcile the non-additive PAT bridge (ARITH-1); soften/cite the "active buyers −3%→−5% 2nd consecutive decline" claim (OBS-C2) which is not derivable from the extract; and flag the deck-internal enquiries −11% vs 31→26 (−16%) inconsistency (OBS-C1) for A3/A4 reconciliation.

Coverage: PASS (all counts reconcile; no material orphan row). Arithmetic: PASS on every headline derived metric (one non-additive-bridge defect). Adversarial: one surviving counter unincorporated.

---

```yaml
stage: A5-adversary
company: "INDIAMART"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - {metric: "PAT bridge additivity (consol Step 4A)", a4_value: "components imply +25.3 vs stated total +18.7", recomputed: "stated total +18.7 correct (172.2-153.5); listed components non-additive (mix pre-tax contribution with rate-only tax)", source_line: "results L341; review Step 4A"}
  - {metric: "PAT bridge additivity (standalone Step 4B)", a4_value: "components imply +16.1 vs stated total +10.1", recomputed: "stated total +10.1 correct (176.1-166.0); listed components non-additive", source_line: "results L633; review Step 4B"}
surviving_bear_counters:
  - {claim: "Rolling CFO/PAT ~1.41x elite and consol PAT +12.2% at/above base (record quarter)", counter: "~Rs 96 Cr of the Rs 106.7 Cr consolidated Other Income is UNREALIZED fair-value MTM gain (realized non-operating income only Rs 16 Cr); that is ~41% of consol PBT and ~41% of the Rs 172.2 Cr record consol PAT, demonstrably reversible (Q4 FY26 consol OI -Rs 33.9 Cr). A4 poses the OI composition as an open management question (Q9) when the deck already discloses it. Reinforcing: consol CFO +2% YoY vs PAT +12.2% is a same-season conversion deterioration seasonality does not explain.", source_line: "results L322/L334/L341; deck L1162/L1169/L1107/L1907"}
loop_back_to: "A4"
gap: "A4 must graft the extract-disclosed composition of consolidated Other Income: ~Rs 96 Cr (of Rs 106.7 Cr) is unrealized fair-value MTM gain (deck L1162 realized 16, L1169 fair-value gain 96), ~41% of consol PBT and ~41% of record consol PAT, reversible per Q4 FY26 OI -33.9 (L322). Currently framed only as unanswered Q9; the quantified reversible-MTM reading must be added to flag 8 / combined verdict. Secondary in same loop: reconcile non-additive PAT bridge (Step 4A/4B); cite-or-soften 'active buyers -3%->-5% 2nd consecutive decline' (not in extract); flag deck-internal enquiries -11% vs 31->26 (-16%) inconsistency."
```
