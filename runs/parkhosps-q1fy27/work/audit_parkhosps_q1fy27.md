# A5 ADVERSARY / COMPLETENESS AUDIT — Park Medi World Limited (PARKHOSPS) — Q1 FY27

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Date: 2026-08-03
Under audit: review_parkhosps_q1fy27.md (A4). Re-derived independently from the four A1 extracts and diffed against the four A2 ledgers. A3 reasoning not consulted; A4 cites checked, not trusted.
Unit convention confirmed against every extract header: Rs Millions, x0.1 to Rs Cr. Filing column order Q1FY27 | Q4FY26 | Q1FY26 | FY26-full-year (verified against results L162-163 / L416).

---

## AUDIT 1 — COVERAGE (fresh grep/sweep vs A2 ledgers, then A2→A4 citation trace)

| Category (doc) | A2 count | A5 fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---:|---:|---|---|
| Results — numbered notes | 22 | 22 (standalone 10 @ L211/217/223/228/233/238/245/264/270/273; consol 12 @ L476/481/486/490/497/501/506/519/537/542/546/549) | none material | PASS |
| Results — P&L line items | 63 | 63 (standalone 27 @ L165-196; consol 36 @ L418-461) | none | PASS |
| Results — consolidation entities | 23 | 23 (Annexure-I L377-399) | none — Devina Derma exit + Healplus omission both surfaced (RES-A3-01/RES-A3-10) | PASS |
| Results — board/agenda items | 3 | 3 (L58 results; L62 Mehar; L68 IPO-object variation) | none | PASS |
| Results — auditor paragraphs | 12 | 12 (standalone I/2/3/4/5 @ L106-133; consol 1-7 @ L291-342) | none — unmodified opinion + 2 EoM-type + Para-7 Other-Matter all cited | PASS |
| Monitoring — notes | 15 | 15 (reconstruction at ledger L21 re-walked; certificate cites + Note1/Note2 + object narratives + GCP §5) | none material | PASS |
| Monitoring — line items | 21 | 21 (issue-size 3 + cost table 7 + progress table 7 + deployment 3 + delay 1) | none | PASS |
| Monitoring — governance questionnaire | 9 | 9 (L226-300) | none | PASS |
| Presentation — slides | 26 | 26 (26 PDF pages; 4 OCR dividers @ pp.7/16/20/23) | none | PASS |
| Presentation — numbers | 341 | 341 (spot-verified page 24 P&L 16 rows, page 6 chart block, page 25 stats; tally 115 axis + 125 label + 101 plain = 341) | none | PASS |
| Release — page units | 4 | 4 (L15/53/99/147) | none | PASS |
| Release — summary-table cells | 55 | 55 (11 metrics x 5 columns, L111-122) | none | PASS |

**A2→A5 count reconciliation:** every gated count reproduces exactly on a fresh pass. No row my pass found is missing from any ledger (no A2 loop-back). No numeric row is present in a ledger that A4 failed to reach.

**Flagged-row citation trace (the rows that carry an A2 flag — these are the ones that must reach A4):**
- Results ENTITY_CHANGE x4 → all in A4: Devina Derma (RES-A3-01, Step 0D/Q12), Healplus omission (RES-A3-10, Q15), V3/Rudrapur (Step 0D/Step 3/PRES-A6), Mehar (Board item 2). PASS.
- Results ZERO_STANDING x3 (exceptional items x2, standalone prior-year tax) → exceptional-nil surfaced (Q12/RES-A3-01); standalone prior-year tax subsumed in standalone tax read. PASS.
- Results Para-7 unaudited-contribution → A4 quantifies 83.9% outside principal-auditor review (RES-A3-03, caveat 2, Q3). PASS.
- Monitoring DELAY_DEVIATION (equipment 84% behind) → MON-A3-F6-01 (Step 5, Q5). PASS.
- Monitoring ZERO_STANDING x12 / idle Rs 648.32mn zero-yield → MON-A3-F1-01 (Step 5, Q4). PASS.
- Presentation PARTIAL_OWNERSHIP / occupancy-axis scaling / ARPOB-undisclosed → PRES-A6 / PRES-A7 / PRES-A9 (Step 2, Section B, Q7/Q9). PASS.
- Release UNIT_INCONSISTENCY / SUBSEQUENT_EVENT / SAME_DAY / roadmap non-reconciliation → REL-FND-01/05, RES-A3-05, Q14. PASS.

**Immaterial mechanical flags not individually surfaced by A4** (recorded, NOT scored as orphan FAILs — zero numeric/thesis consequence, and A4's contractual preamble states all four ledgers reviewed at cited lines): standalone auditor Membership-No. field blank vs "080475" on consolidated report (results §5A/§9A); consolidated IPO-utilisation table omits the "Total" subtotal row present in the standalone twin (results §1C — Grand Totals still tie 7,700.00/7,051.68/648.32); CRISIL report carries no UDIN and no signature timestamp (monitoring §2.7); duplicate "Annexure-I" label (results §7A). None alters a number or the verdict.

**COVERAGE VERDICT: PASS.** No orphan material row; no A2/A3 loop-back.

---

## AUDIT 2 — ARITHMETIC (every derived metric recomputed from raw extract figures)

Consolidated raw anchors: Rev 4,757.09/3,988.45/4,604.13/16,793.56 (L418); OI 76.46/68.72/75.03 (L419); PBT 1,050.84/818.99/1,033.90 (L430); D 188.40/147.71/175.06 (L427); Fin 98.10/151.33/139.75 (L426); Tax 164.91/163.93/266.12 (L437); PAT 885.93/655.06/767.78 (L438); owners 825.07/579.83 (L446).

| Metric | A4 value | A5 recomputed | Source lines | Status |
|---|---|---|---|---|
| Consol Op EBITDA Q1FY27 (PBT+D+Fin−OI) | 1,260.88 | 1,050.84+188.40+98.10−76.46 = 1,260.88 | L430/427/426/419 | MATCH |
| Consol Op EBITDA Q1FY26 | 1,049.31 | 966.70+151.33−68.72 = 1,049.31 | same | MATCH |
| Consol Op EBITDA margin Q1FY27 | 26.51% | 1,260.88/4,757.09 = 26.508% | L418 | MATCH |
| Consol Op EBITDA margin YoY | +20 bps | 26.508%−26.309% = +19.9 bps | derived | MATCH |
| Reported EBITDA Q1FY27 (PBT+D+Fin) | 1,337.34 | 1,050.84+188.40+98.10 = 1,337.34 | L430/427/426 | MATCH |
| Core PBT ex-OI Q1FY27 | 974.38 | 1,050.84−76.46 = 974.38 | L430/419 | MATCH |
| Core PBT ex-OI YoY % | +29.87% | (974.38−750.27)/750.27 = 29.87% | derived | MATCH |
| Effective Tax Rate Q1FY27 | 15.69% | 164.91/1,050.84 = 15.694% | L437/430 | MATCH |
| ETR Q1FY26 / Q4FY26 / FY26 | 20.02 / 25.74 / 22.85% | 20.016 / 25.740 / 22.851% | L437/430 | MATCH |
| PAT margin Q1FY27 | 18.62% | 885.93/4,757.09 = 18.622% | L438/418 | MATCH |
| Revenue YoY | +19.27% | 768.64/3,988.45 = 19.272% | L418 | MATCH |
| PAT (total) YoY | +35.24% | 230.87/655.06 = 35.244% | L438 | MATCH |
| Depreciation YoY | +27.55% | 40.69/147.71 = 27.547% | L427 | MATCH |
| Finance cost YoY | −35.18% | −53.23/151.33 = −35.176% | L426 | MATCH |
| EPS YoY | +20.59% | 0.35/1.70 = 20.588% | L460 | MATCH |
| PAT bridge foots | +230.87 | +211.57−40.69+53.23+7.74−0.98 = +230.87 | L438 vs components | MATCH |
| Tax tailwind vs 20.02% ETR | ~Rs 45.5mn | 1,050.84×20.016%=210.4; 210.4−164.91=45.5 | L430/437 | MATCH |
| Normalized PAT (add back 93.40 DT benefit) | ≈792.5mn → +21.6% | 885.93−93.40=792.53; 655.06−3.55=651.51; +21.65% | L435/438 | MATCH |
| EBITDA growth as % of PAT growth | 91.6% | 211.57/230.87 = 91.64% | derived | MATCH |
| Standalone Op EBITDA Q1FY27 | 12.84 | 17.11+33.81+8.60−46.68 = 12.84 | L177/174/173/166 | MATCH |
| Standalone Op EBITDA margin Q1FY27 | 3.83% | 12.84/335.32 = 3.829% | L165 | MATCH |
| Standalone core PBT ex-OI Q1FY27 | (29.57) | 17.11−46.68 = −29.57 | L177/166 | MATCH |
| Standalone OI/PBT Q1FY27 | 272.82% | 46.68/17.11 = 272.82% | L166/177 | MATCH |
| Standalone rev YoY / PAT YoY | +45.99% / −77.86% | 105.63/229.69=45.99%; −38.13/48.97=−77.86% | L165/185 | MATCH |
| Standalone cost ramps (emp/prof/dep/other) | +142.9/+219.0/+191.2/+204.0% | 142.9 / 218.98 / 191.2 / 204.0% | L171/172/174/175 | MATCH |
| Std-vs-consol PAT % (Q1FY27) | 1.22% | 10.84/885.93 = 1.223% | L185/438 | MATCH |
| Unaudited-contribution share | 83.9% | (717.68+26.00)/885.93 = 83.94% | L343/352/438 | MATCH |
| EPS struck on total (not owners) PAT | 2.05 = total; owners → 1.91 | 885.93/431.93m=2.051; 825.07/431.93m=1.910; Q1FY26 655.06/384.4m=1.704 | L438/446/460/L1046 | MATCH (anomaly correctly identified) |
| Trigger-4 per-bed: Rudrapur / Mehar | 0.54 / 0.71 Cr/bed | 177/330=0.536; 141.6/330=0.429; 107/150=0.713 | L266/L531/L588 | MATCH (both <1.0) |
| QoQ: rev +3.32% / core PBT +1.62% / margin −115bps | as stated | 15.30/460.41=3.32%; 15.51/958.87=1.62%; 26.51−27.66=−1.15pp | derived | MATCH |
| Idle IPO / equipment shortfall | 648.32mn; 84% behind | 72.32+576.00=648.32; 193.51/229.59=84.3% | mon L555/L583/L586 | MATCH |
| Annualised run-rate (rev/owners PAT/EPS x4) | 1,903 / 330 / 8.20 | 475.71×4=1,902.8; 82.51×4=330.0; 2.05×4=8.20 | derived | MATCH |
| Empty beds at 55.6% | ~1,758 | 3,960×0.444 = 1,758.2 | deck L111/L112 | MATCH |

Note on occupancy bps: A4 carries the release-disclosed −1,224 bps YoY / −692 bps QoQ (release L112) rather than the rounded 1-dp subtraction (−1,220 / −690 bps). This is adoption of a source figure, not an A4 derivation error — no FAIL.

**ARITHMETIC VERDICT: PASS.** Every derived metric in every A4 table recomputes within rounding from the raw extract. Zero mismatches above rounding. No A4 loop-back.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive A4 claims; strongest bear counter from the SAME extract)

**Positive claim 1 — "Core operating PBT ex-OI grew +29.87% YoY, faster than revenue; the operational core is genuinely expanding, not a treasury illusion" (Step 2 diag 3).**
Strongest bear counter (same text): the +29.87% is inorganic/bed-led, not same-store. Deck slide 10 (L513/525) attributes 65% of revenue, 69% of EBITDA and 77% of PAT to acquisitions, while occupancy fell −1,224 bps YoY to 55.6% (L112) on a +32% bed base — i.e., absolute core PBT rises because Agra/Panchkula were bolted on, not because the existing estate is doing more. And 83.9% of that consolidated PAT is outside principal-auditor review (results L342-353), so the "genuine core" is largely unaudited-by-Agiwal subsidiary earnings.
Survives? **Substantially incorporated in A4** — diag 1 already states growth is "bed-led, not utilisation-led," diag 2 flags same-store/ARPOB undisclosed (PRES-A9), and the 83.9% is caveat #2. No NEW surviving element requiring graft.

**Positive claim 2 — "Op EBITDA margin held at 26.51%, +20 bps YoY DESPITE a 1,224 bps occupancy fall; margin resilience is real at the reported level" (Step 2 diag 2 / Combined Verdict).**
Strongest bear counter (same text): the +20 bps YoY is measured against a Q1 FY26 base the auditor expressly states was **never subjected to limited review** (results L137/L325, EoM 5(b)), while the QoQ comparator is a Q4 FY26 "balancing figure" (L133) — so both anchors of the "resilience" claim carry audit caveats, and the one measured against the more-recent base moves the wrong way (−115 bps QoQ). Every YoY growth figure A4 leads with (rev +19.3%, core PBT +29.9%, PAT +35.2%) shares this unreviewed-prior-year base.
Survives? **Present in A4 but not tied to the claim.** A4 records the unreviewed comparative in Step 0D and the balancing-figure caveat in Step 3, and hedges resilience with "unverifiable without same-store... QoQ direction is down." The incremental point — that the unreviewed-base caveat should ride explicitly on the YoY growth trio in the Combined Verdict — is an emphasis refinement, not a missing fact. Does not rise to a graft-forcing gap.

**Positive claim 3 — "Bed roadmap ON TRACK; best-ever quarterly operating performance; both acquisitions <Rs 1.0 Cr/bed; net cash — growth/capital-allocation intact" (Step 6B/6D, Section B).**
Strongest bear counter (same text): the monitoring report contradicts "disciplined capital allocation." Rs 648.32mn IPO cash sits idle at ZERO yield (mon L549-555); 4 of 5 IPO objects were dormant this quarter; the medical-equipment object is 84% behind its FY26 schedule (36.08 of 229.59mn, mon L586); the Rs 2,453.18mn "unidentified acquisition/GCP" object is reported fully spent with NO named target and GCP detail "Not applicable" (mon L599-603); and the Board simultaneously filed a postal-ballot to VARY the IPO objects (results L68) while announcing Rs 2,840mn of fresh M&A — an object-plan being redrawn mid-stream.
Survives? **Fully incorporated in A4** — Step 5 monitoring facts, Step 6D rates capital allocation "AMBIGUOUS" (not on-track), Q4/Q5/Q6 to management, and the roadmap non-reconciliation (1,490 vs 1,450; 4,290 vs 3,960) is Q14/RES-A3-05. No surviving new element.

**Adversarial verdict:** all three strongest bear counters, when built from the same extracted text, are already carried in A4 (bed-led/same-store ambiguity; unreviewed comparator + QoQ down; idle capital + object variation + ambiguous allocation). No bear counter survives as an un-incorporated finding that must be grafted before save. One soft recommendation (non-blocking): A4 may elevate the auditor-unreviewed Q1 FY26 base (L137/L325) from Step 0D into an explicit rider on the YoY growth trio in the Combined Verdict — the fact is present, only its placement is diffuse.

---

## VERDICT

**COMPLETE.** Coverage PASS (all gated counts reproduce on a fresh pass; every flagged/material ledger row reaches A4; no orphan row, no A2/A3 loop-back). Arithmetic PASS (every derived metric in every A4 table recomputes within rounding from raw extract figures; zero mismatches, no A4 loop-back). Adversarial PASS (the three strongest bear counters are already incorporated in A4; none survives un-grafted). The single recommendation (elevate the unreviewed-comparator caveat onto the YoY trio) is non-blocking emphasis, not a completeness or arithmetic failure. Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "PARKHOSPS"
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
