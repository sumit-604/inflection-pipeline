# A5 ADVERSARY / COMPLETENESS AUDIT — Ganesha Ecosphere Limited (GANECOS) — Q1 FY27

Agent: A5 ADVERSARY | Model: claude-opus-4-8 | Fresh context (A4 review + 4 A1 extracts + 4 A2 ledgers only; A3 reasoning not seen; re-derived independently).
Documents under audit (FOUR): results filing (Rs Lakh ×0.01→Cr) + Reg 30 board outcome + investor presentation (Rs Cr) + Q1 FY27 concall (as-spoken). Role 4 + Role 5.
Verdict up front: **COMPLETE.** Details below. Every figure carries a source line/turn; I checked A4's cites, I did not defer to them.

---

## AUDIT 1 — COVERAGE

Independent re-enumeration (fresh grep + manual sweep over each A1 extract), diffed against the four A2 ledgers, then checked that every material ledger unit is cited in A4 or reviewable as no-finding.

| Category | A2 count | My fresh count | Method / check | Orphan rows | Status |
|---|---|---|---|---|---|
| Doc1 notes | 14 | 14 | std notes 1-7 (ext L100-113) + consol notes 1-6 + unnumbered ESOP footnote (L261-264) | none | PASS |
| Doc1 line items | 64 | 64 | std 31 (L54-99) + consol 33 (L199-247), row-anchored | none | PASS |
| Doc1 zero-standing | 4 | 4 | std B(i)/B(ii) OCI + consol B(i)/B(ii) OCI | none | PASS |
| Doc1 auditor paras | 15 | 15 | std 4 (unnumbered prose L144-174) + consol 11 (L293-377; para1 OCR'd "I.") | none | PASS |
| Doc1 entities | 6 | 6 | L321-335: Parent, Ecopet, Ecotech, Nepal Overseas, Trust, assoc Ganesha Recycling Chain | none | PASS |
| Doc1 agenda items | 4 | 4 | board-outcome cover letter (L17-29) | none | PASS |
| Doc2 agenda items | 1 | 1 | SVP re-appointment (L19-23) | none | PASS |
| Doc2 annexure particulars | 4 | 4 | reason / date-term / profile / relationship (L53-75) | none | PASS |
| Doc2 related-party facts | 2 | 2 | son-of-EVC (L71-75); MD of Ganesha Ecoverse (L62-65) | none | PASS |
| Doc2 regulatory refs | 2 | 2 | Reg 30 (L15-19); Master Circular (L26-28/48-50) | none | PASS |
| Doc2 signatory | 1 | 1 | Sajnani, CS, ts 20:02:11 (L33-41) | none | PASS |
| Doc3 slides | 34 | 34 | fresh `[page N]` sweep = 34; pdfinfo 34 | none | PASS |
| Doc3 P&L line items | 28 | 28 | consol 14 (L672-689) + std 14 (L692-711) | none | PASS |
| Doc3 subsidiaries | 3 | 3 | Ecopet / Ecotech / Overseas (slide 15, L341-347) | none | PASS |
| Doc3 chart clusters | 45 | 45 | Table B slides 6-11,18,26 | none | PASS |
| Doc3 footnotes | 6 | 6 | Table D (4× production-caption + brownfield + safe-harbour) | none | PASS |
| Doc3 guidance units | 7 | 7 | Table E | none | PASS |
| Doc4 turns | 17 | 17 | fresh `grep ^\[TURN` = 15 bracket turns + OR-1/OR-2 = 17 | none | PASS |
| Doc4 questions | 74 | 74 | ledger two-pass 74; moderator "next question" cues grep = 17 (consistent with 15 analyst turns, some cues double-fired) | none | PASS |
| Doc4 mgmt numbers | 83 | 83 | M1-M83 (30 GUIDANCE, 4 ANALYST_STATED, 4 ASR_UNCERTAIN) | none | PASS |

**Fresh-pass counts equal every A2 count.** No row my pass found is absent from a ledger (nothing to loop to A2). No material ledger row is absent from A4 (nothing to loop to A3).

Targeted coverage checks demanded by the task:

- **(a) Four-ledger tie, no orphan unit.** A4 preamble (L13-18) states 14 notes / 17 turns / 34 slides / 74 questions / 83 mgmt numbers — matches all four ledgers and my fresh pass exactly. Concall 17/74/83 confirmed. PASS.
- **(b) Concall headline numbers reconcile; no 🎙️ treated as 📄.** production 42,826 MT (concall L23 = deck slide-6/8 42,826); PAT 29.03 (concall L23 = filing consol 2,903.48 Lakh = deck 29.03); EBITDA 59.8 (concall = deck 59.8; my recompute 59.78 at lakh precision); margin 14.1% (concall = deck; recompute 14.11%); standalone EBITDA 23.8 (concall = deck; recompute 23.79); OI 3.52 (concall L23 = filing 351.68 Lakh; deck bullet 3.53 vs table 3.52 flagged A3-F14-01). A4 §7A/§0 marks all as 📄-tied. The ~24/kg subsidiary EBITDA and 14,800 MT are ledger-flagged ANALYST_STATED (M48/M49); A4 treats them as derived/analyst figures, NOT as filed facts, and every FY27/FY28 target is carried 🎙️. PASS.
- **(c) Volume correction.** −11.2% consol / −13.4% std are QoQ vs Q4 FY26 (deck slide-12 L298-299; concall L23 "down by 13.4% from Q4 FI26"). QoQ math: consol 45,162→40,113 = −11.18%; std 29,234→25,321 = −13.4%. YoY consol volume UP: 33,650→40,113 = +19.2% (deck slide 8); production 36,049→42,826 = +18.8%. Concall confirms YoY up and Q2 reviving (L80 "expecting better volume"; L82 "it started already"; L99 one-off deferred purchases). A4 Step 2/§0 states this correctly. PASS.
- **(d) Subsidiary inventory-gain admission + 16-20/kg guide, line-cited.** Admission: concall L88 ("certainly we got some inventory gain... working out any great number is not possible") and L125 (analyst: 24/kg "more driven by inventory gain"; mgmt confirms). Sustainable guide: L103 ("a bita between 16 to 20 at a combined level in the subsidiary business... in the long long term"). A4 Step 4A / CC-F7-01 cites L88, L125, L103. PASS.
- **(e) Each concall AMBIGUOUS/FORWARD signal maps; 16-question map line-cited.** Step 8.5 maps all 16 Role-4 questions to concall answer-status with line cites (Q11 L23/36-37; Q12 L80-82,99; Q15 L40,104,162-164,226; Q1 L88,103,124; etc.). Tally 3 ANSWERED / 2-3 PARTIAL / 10-11 NOT ADDRESSED sums to 16. **Minor non-fatal note:** the Step 8.5 table marks Q9 "NOT ADDRESSED" while the tally line and Step 3E say "+Q9 partial (2-3 PARTIAL)" — a labeling wobble; totals to 16 either way and Q9 is line-cited (loans→equity dated ~end-Q4 FY26 only). Does not create an orphan or change the verdict. PASS.
- **(f) Net debt NOT computable, cash conversion INDETERMINATE, deflected on call.** Concall gives WC days (L194 legacy 75-90 / subsidiary 45-50) but no net-debt/borrowings/cash figure anywhere in the transcript (I searched). A4 Step 5 keeps net debt ND, cash conversion INDETERMINATE, tripwire 3 RED, pre-condition (ii) unmet, CC-F17-01. PASS.
- **(g) No NOT FOUND value estimated.** Next-year capex explicitly deferred (concall L69; ledger M31 NOT FOUND) — A4 records "deferred/no figure," not a number. Net debt ND, share-adjusted EPS ND, CFO / CFO-ratio ND — all left ND, none estimated. FY25 S-to-C gap +27.64 is a Notion pass-through, not a filing estimate. PASS.
- **(h) Decision Status unchanged, no committed trigger.** A4 Step 8 / Step 6C: WATCHLIST unchanged; no committed thesis-broken condition exists so none fired. PASS.
- **(i) Role 5 credibility ratio not-yet-computable.** A4 R5 Step 3 / verdict: first tracked concall, no prior transcript, trailing-4 ratio not computable, log seeded — stated as not-yet-computable, not invented. PASS.

**Coverage verdict: PASS. Zero orphan rows; zero rows missing from any ledger.**

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extracted numbers; lakh precision where it matters)

| Metric | A4 value | My recompute | Source line | Status |
|---|---|---|---|---|
| Std Op EBITDA Q1FY27 (PBT+D+Fin−OI) | 23.79 | 18.46+6.85+2.00−3.52 = 23.79 | ext L70,65,64,55 | PASS |
| Std Op EBITDA margin Q1FY27 | 9.07% | 23.79/262.30 = 9.07% | L54 | PASS |
| Std core PBT Q1FY27 | 14.94 | 18.46−3.52 = 14.94 | L70,55 | PASS |
| Std ETR Q1FY27 | 25.5% | (507.73−37.15)/1845.53 = 25.50% | L72,73,70 | PASS |
| Std Op EBITDA Q1FY26 / Q4FY26 / FY26 | 9.30 / 20.93 / 56.95 | 9.30 / 20.93 / 56.95 | L54-70 cols | PASS |
| Consol Op EBITDA Q1FY27 (V+D+Fin−OI) | 59.78 | (3718.02+1734.25+887.26−361.98)/100 = 59.78 | L216,210,209,201 | PASS |
| Consol Op EBITDA margin Q1FY27 | 14.11% | 59.78/423.67 = 14.11% | L199 | PASS |
| Consol ETR Q1FY27 | 21.7% | (507.73+298.26)/3709.47 = 21.73% | L220,221,218 | PASS |
| Consol core PBT Q1FY27 | 33.47 | 37.09−3.62 = 33.47 | L218,201 | PASS |
| Consol Op EBITDA Q1FY26/Q4FY26/FY26 | 36.31 / 52.35 / 141.71 | 36.31 / 52.35 / 141.71 (lakh) | L204-217 cols | PASS |
| Consol ETR Q4FY26 / FY26 | 24.8% / 29.2% | 766.99/3088.13=24.83% ; 1573.63/5394.98=29.17% | L220-221,218 | PASS |
| YoY std revenue | +18.4% | 40.83/221.47 = 18.44% | L54 | PASS |
| YoY std Op EBITDA | +155.8% | 14.49/9.30 = 155.8% | derived | PASS |
| YoY std margin (bps) | +487 | 9.07−4.20 = 4.87pp | derived | PASS |
| YoY std finance | +51.8% | (199.90−131.65)/131.65 = 51.84% | L64 | PASS |
| YoY std EBIT(op) | +394.6% | (1693.75−342.54)/342.54 = 394.5% (lakh) | derived | PASS |
| YoY std core PBT | +608.4% | (1493.85−210.89)/210.89 = 608.4% (lakh) | L70,55 | PASS |
| YoY std reported PBT / PAT | +79.5% / +79.4% | 79.54% / 79.43% (lakh) | L70,74 | PASS |
| YoY std EPS basic | +70.4% | (5.13−3.01)/3.01 = 70.4% | L98 | PASS |
| YoY consol revenue | +25.7% | 86.55/337.12 = 25.67% | L199 | PASS |
| YoY consol Op EBITDA | +64.6% | 23.47/36.31 = 64.64% | derived | PASS |
| YoY consol margin (bps) | +334 | 14.11−10.77 = 3.34pp | derived | PASS |
| YoY consol D&A / finance | +11.9% / −9.8% | 11.87% / −9.86% | L210,209 | PASS |
| YoY consol EBIT(op) | +103.9% | (4243.30−2081.05)/2081.05 = 103.9% (lakh) | derived | PASS |
| YoY consol core PBT | +206.0% | (3347.49−1094.03)/1094.03 = 206.0% (lakh) | L218,201 | PASS |
| YoY consol reported PBT / PAT | +159.1% / +170.0% | 159.07% / 170.05% | L218,222 | PASS |
| YoY consol EPS basic | +156.5% | (10.85−4.23)/4.23 = 156.5% | L245 | PASS |
| PAT bridge: rev contrib | +9.32 | 86.55×0.1077 = 9.32 | derived | PASS |
| PAT bridge: margin contrib | +14.15 | 0.0334×423.67 = 14.15 | derived | PASS |
| PAT bridge: PBT change | +22.77 | 37.09−14.32 = 22.77 | L218 | PASS |
| PAT bridge: tax change | −4.50 | −(8.06−3.56) = −4.50 | L220-221 | PASS |
| PAT bridge: PAT YoY change | +18.27→+18.28 | 29.03−10.75 = 18.28 | L222 | PASS (0.01 lakh rounding) |
| Std PAT bridge | +6.09 | 14.49−0.98−0.68−4.65−2.09 = 6.09 | derived | PASS |
| S-to-C gap Q1FY27 | +15.29 | (2903.48−1374.95)/100 = 15.29 (lakh) | L222,74 | PASS |
| S-to-C gap % of std PAT | +111% | 15.29/13.75 = 111.2% | derived | PASS |
| S-to-C gaps Q1FY26 / Q4FY26 / FY26 | +3.09 / +6.80 / −9.62 | 3.09 / 6.80 / −9.62 | L222,74 | PASS |
| FY26 quarterly-gap sum tie | −9.6 → −9.62 | +3.1−3.1−16.4+6.8 = −9.6 | derived | PASS |
| Q1FY27 gap decomposition | +15.29 | subs +15.04 (para7) −0.27 (para8) −0.09 (para10) +0.61 elim | L348,356,368 | PASS |
| Derived subsidiary EBITDA/kg | ~24 | 36.0 Cr / 14,800 MT = 24.3 Rs/kg | derived (analyst-stated inputs) | PASS |
| YoY consol volume | ~+19% | (40,113−33,650)/33,650 = 19.2% | deck slide 8 | PASS |

**Every derived metric reconciles.** The only numeric spread anywhere is lakh-vs-Cr rounding (59.77 vs 59.78; 15.28 vs 15.29; 22.77 vs 22.78; 18.27 vs 18.28) — all resolve exactly at lakh precision, i.e. within rounding. **No mismatch above rounding. Arithmetic verdict: PASS.**

---

## AUDIT 3 — ADVERSARIAL READ (three most positive A4 claims; strongest bear counter from the SAME extracted text)

**Claim 1 — "Consolidated PAT +170% YoY, ~100% of PAT growth is recurring core operations; core operating PBT +206%."** (A4 Step 2 / Step 4)
Bear counter (from extract): management ITSELF admitted part of the subsidiary margin (~Rs 24/kg) is a non-recurring inventory gain (concall L88, L125) and guided the sustainable level DOWN to 16-20/kg (L103). So the +14.15 Cr "margin-change" leg of the PAT bridge is partly non-recurring; "~100% recurring core" over-states durability. The −Rs 35.56 Cr consol inventory build (ext L206) is the mechanical source of that gain.
Survives? **Yes from the text — but ALREADY GRAFTED by A4:** Step 4A downgrades the subsidiary read explicitly ("management itself has told us the number is inflated; durable earning power is the guided 16-20/kg, not Q1 ~24/kg"), Step 4 tags the margin leg "part = inventory gain (CC-F7-01)," and it is a named flag. No un-incorporated residue. **Nothing to add.**

**Claim 2 — "Volume read corrected UP: YoY volume up ~19%; the sequential dip is one-off; Q2 already reviving."** (A4 Step 2 diagnostic 1)
Bear counter (from extract): the −11.2%/−13.4% QoQ decline is a filed/deck 📄 fact; "Q2 already reviving" is an unverified 🎙️ management claim (L82 "it started already"), and the ~19% YoY magnitude carries the deck's CHART_ORDER_APPROX caveat. Higher fibre prices caused customers to defer (L99) — a demand-elasticity signal that could recur while polymer volatility persists (management calls the industry "very volatile," L101/L153).
Survives? **Yes from the text — but ALREADY GRAFTED:** A4 tags the revival 🎙️/"pending Q2 proof," attaches the CHART_ORDER_APPROX caveat to the ~19%, and keeps volume revival as an unproven monitorable/flag. **Nothing to add.**

**Claim 3 — "Op EBITDA margin expanded +334 bps consol / +487 bps standalone."** (A4 Step 2 diagnostic 2)
Bear counter (from extract): the consol expansion leans on the subsidiary leg that is ~52% statutorily unreviewed (auditor Other-Matter paras 7-8, ext L346-361) and inventory-gain-inflated; the standalone +487 bps is realisation-led in a business management describes as "very volatile" and explicitly says "not really look at the realization number" (L101, CC-F7-02) — i.e. margin quality is not obviously durable.
Survives? **Yes from the text — but ALREADY GRAFTED:** A4 flags realisation-led standalone margin, the ~52%-unreviewed subsidiary leg (CC-F4-01), the volatility hedge (CC-F7-02), and the inventory-gain caveat. **Nothing to add.**

**Adversarial verdict:** the three strongest bear counters all survive on the text, and A4 has already incorporated every one (Step 4A downgrade, the 🎙️/📄 tiering, tripwires 1/3/7, and the flag block). **No surviving un-incorporated bear counter to loop back to A4.**

---

## MINOR (non-fatal) OBSERVATIONS — recorded, do NOT change verdict
1. Step 8.5 Q9 answered-status labeled "NOT ADDRESSED" in the table but "+Q9 partial" in the tally line (2-3 PARTIAL). Totals to 16 either way; Q9 is line-cited. Cosmetic; A4 may tidy but no action required.
2. Rounding spreads (59.77/59.78; 15.28/15.29; 22.77/22.78; 18.27/18.28) are lakh-vs-Cr artifacts; all correct at lakh precision.
3. Concall macro DATA_DISCREPANCY flags (M66 50% vs M46/M68 40% mandate; M69 2.8 vs 4.2 lakh industry capacity, both ANALYST_STATED) are captured in A4's R5 Step 2 "Input/market" row, which adopts management's 4.2 lakh / 40% current / 50% (2030) reading — reviewed, resolved, not an orphan.

---

## VERDICT

**COMPLETE.** All three audits pass. Coverage ties to all four A2 ledgers with zero orphan rows and zero rows missing from any ledger; my fresh enumeration equals every A2 count (notes 14, line items 64, auditor paras 15, entities 6, slides 34, turns 17, questions 74, mgmt numbers 83). Every derived metric recomputes to A4's value within lakh-rounding. The three strongest bear counters are supported by the extract and are already incorporated in A4. Net debt correctly NOT computable / cash conversion INDETERMINATE; no NOT FOUND estimated; Decision Status WATCHLIST unchanged with no committed trigger; Role 5 credibility ratio correctly stated not-yet-computable. Proceeds to Notion save.

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
