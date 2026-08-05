# A3 FORENSIC NOTES — Vaibhav Global Limited (VAIBHAVGBL) — Q1 FY27 — doctype: PRESENTATION

Source extract: `/home/user/inflection-pipeline/runs/vaibhavgbl-q1fy27/work/extract_presentation_vaibhavgbl_q1fy27.txt` (1168 lines, 39 slides, unit Crores)
Ledger: `/home/user/inflection-pipeline/runs/vaibhavgbl-q1fy27/work/ledger_presentation_vaibhavgbl_q1fy27.md`
Ledger reconciliation: 100% — every row of Tables A-I read verbatim at its cited line before judging.

## SCOPE NOTE (doctype = presentation, first-time coverage)
Per the checklist's doctype-applicability rule and the orchestrator's CONTEXT, the Reg-33 results-specific and auditor/balance-sheet checks (F2, F3, F4, F5, F9, F12, F13, F15) are N.A. for an investor deck that carries no standalone-vs-consolidated statements, no auditor report/Other-Matters/EoM, no OCI statement, no segment assets/liabilities, no board outcome, and (first coverage) no prior ledger. F16 is the primary check; F6/F7/F8/F10/F11 are run against the numbers/language the deck actually carries. F17 is N.A. (this is a deck, not a concall; the monitoring checklist is empty). Every check is marked below; none blank (GATE A3).

A2 flags weighed: `CHART_PAGE_OFFSET` (8/9 chart markers cite the slide before the rendered bars — treated as an extraction artifact; all chart numbers below are anchored to the RENDERED slide per Table B, NOT the marker's stated page; no finding raised on the offset itself). `OCR_QUALITY_ISSUE` (pages 2/5/10/19/23/30 — all cover/divider slides, no primary financial data at risk; the one finding touching an OCR page, F14 section numbering, is corroborated in the CLEAN text layer, not from OCR). `SECTION_NUMBERING_ANOMALY`, `ZERO_STANDING`, `PRIOR_LEDGER_UNAVAILABLE` addressed at F14/F1/F15 respectively.

---

## FINDINGS TABLE
| id | check | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FND-01 | F1 | Table I #1 | L472 / s16 | "0% marketplace take-rate on primary channels" | NEUTRAL-FACT | Sole zero-standing item is a promotional differentiator (own channels carry no marketplace commission), not a transaction-anticipating template line; implicitly disparages marketplace-reliant peers. No B/S implication. |
| FND-02 | F6 | Table D #7 | L1028 / s34 | "Expected to contribute towards profitability from FY27" (Germany) | FORWARD-SIGNAL | Dated management commitment: Germany segment profit inflection promised for FY27. Feeds Role 5 promise-vs-delivery tracker. Germany Q1FY27 EBITDA still only implied thin (see FND-03). |
| FND-03 | F7 | Table C s14; Table D | L387-388 / s14 | "margins are expected to strengthen meaningfully over the course of the year" | FORWARD-SIGNAL | Pre-emptive hedge on Europe margins. Europe FY26 EBITDA Rs7 Cr on Rs404 Cr rev (~1.7%); Q1FY27 EBITDA Rs1 Cr on Rs103 Cr rev (~1.0%, L384) — margin currently compressed, deck telegraphs it recovers "over the year." Next-quarter Europe margin is the tell. |
| FND-04 | F8 | Table F #6 | L540 / s18 | "Note: Q4FY26 PAT is excluding MAT credit of INR 47.2 cr" | AMBIGUOUS | Rs47.2 Cr MAT credit stripped out of the Q4FY26 PAT bar (shown as 44). Including it, Q4FY26 PAT was ~91, so Q1FY27 PAT of 56 is a QoQ DECLINE that the ex-MAT presentation masks as clean growth. MAT-credit utilisation = future cash-tax/ETR step-up risk. A4 question. |
| FND-05 | F10 | Table C s35 | L1042 / s35 | "74% PAT growth ... EPS up 73% to Rs16.0" | NEUTRAL-FACT | EPS growth (73%) trails PAT growth (74%) by ~1pp — small dilution tell (ESOP/share issuance). No basic-vs-diluted split, no share count in deck. A4 to reconcile share count at the results filing. |
| FND-06 | F11 | Table B #5; Table C s11/s35 | L275 & L1052 vs L731/L739 | "Rs296 Cr net cash position" "As on FY26" (s11) vs chart "Net Cash ... FY25 296 / FY26 387" | AMBIGUOUS | Net cash is headlined as Rs296 Cr "As on FY26" (s11 L275; s35 L1052) but the FCF/Net-Cash chart plots FY26 net cash = 387 and 296 as the FY25 bar. Gap of Rs91 Cr (>30%). Either the Rs296 Cr is a stale FY25 figure mislabeled FY26, or the chart's 387 is wrong, or 296 is an undisclosed Q1FY27 draw-down. A4 question. |
| FND-07 | F14 | Table H; Flags (SECTION_NUMBERING_ANOMALY); Table C s39 | L673/L680 & L874/L881; L54 vs L1163 | s23 "04 Key Strengths" and s30 "04 Growth Strategy" both badged "04"; ToC (s4) implies 5 sections; contacts split across "vaibhavglobal.com" (L54) and "vglgroup.com" (L1163) | NEUTRAL-FACT | Section badges run 01,02,03,04,04 (missing 05) — confirmed in clean text layer, not just OCR. Two corporate email domains used. Individually immaterial, cumulatively a drafting-discipline data point on a deck that leans on "Big Four audit / governance award" claims (L1066). |
| FND-08 | F16 | Table B #2 | L543 / s20 | "TV volume 1343/1373/1291(k), ASP $38.8/$40.5/$37.1" | FORWARD-SIGNAL | Headline says "TV Revenue INR 484 Cr, 9% YoY" (L225) — but underlying TV UNIT VOLUME fell 3.9% YoY (1343k->1291k) AND TV USD ASP fell 4.4% YoY ($38.8->$37.1). The +9% INR print is FX-driven (INR depreciation); TV is contracting on both price and volume. Digital, by contrast, has rising ASP ($33.8->$37.0). TV is the structurally weak leg. |
| FND-09 | F16 | Table B #3 vs Table C s18 | L560 / s21 vs L517 / s18 | "EBITDA margin walk Q1FY26 4.2 -> ... -> Q1FY27 11.1" vs "9% 10% 11%" EBITDA margins | AMBIGUOUS | The EBITDA Margin Walk starts from a Q1FY26 base of 4.2%, but the EBITDA chart two slides earlier reports Q1FY26 EBITDA margin at 9% (75 on 814). Walk internally sums (4.2+9.2+1.6-1.2-1.7-1.0=11.1) but its 4.2% base contradicts the 9% headline by ~4.8pp with no reconciliation. Suggests a normalized/ex-other-income base disclosed nowhere. A4 question on the walk base. |
| FND-10 | F16 | Table C s28; Table F #8/#11; Table C s18 | L813 / s28; L1148 / s38; L520 / s18 | "FY20 FY25 FY26" axis (skips FY21-24); "Budget Pay ... reached 38% of B2C revenue"; "* 50% YoY" (PAT) | AMBIGUOUS | (a) Multiple trend charts sample only FY20/FY25/FY26, dropping FY21-24 — non-uniform baseline that flatters the shape. (b) Budget Pay (EMI/instalment financing) at 38% of B2C is framed purely as "affordability," never as customer-receivable/credit exposure. (c) Headline PAT "50% YoY" vs arithmetic 38->56 = +47.4% — optimistic rounding. A4 to probe Budget Pay receivables and normalize the base years. |

---

## CHECKLIST SCORECARD (all 17, one status each)
| Check | Status | Basis (one line) |
|---|---|---|
| F1 ZERO-VALUE STANDING ITEMS | FINDING | One ZERO_STANDING row (L472, 0% marketplace take-rate) = promotional comparator, not a transaction template line — FND-01. |
| F2 STANDALONE vs CONSOLIDATED | N.A. | Deck presents consolidated only; no standalone statements to decompose. |
| F3 SHELL-ENTITY DETECTION | N.A. | No standalone-vs-consolidated cost lines (COGS/employee/depreciation) disclosed in a deck. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor report / Other Matters in an investor presentation. |
| F5 GOING CONCERN / EoM | N.A. | No auditor EoM/going-concern paragraph; first-time coverage, no prior quarter to verbatim-diff. |
| F6 FORWARD-COMMITMENT MINING | FINDING | "Expected to contribute towards profitability from FY27" (L1028) + full commitment register below — FND-02. |
| F7 HEDGE PHRASE MINING | FINDING | New pre-emptive hedge on Europe margins "expected to strengthen ... over the course of the year" (L387-388) — FND-03. |
| F8 TAX FORENSICS | FINDING | Rs47.2 Cr MAT credit stripped from Q4FY26 PAT (L540); future ETR/cash-tax step-up; masks a QoQ PAT decline — FND-04. |
| F9 OCI FORENSICS | N.A. | No OCI / actuarial statement in a deck. |
| F10 SHARE COUNT & DILUTION | FINDING | EPS +73% vs PAT +74% (L1042) — ~1pp dilution tell; no basic/diluted split disclosed — FND-05. |
| F11 RESERVES / NET WORTH TIE-OUT | FINDING | Net cash Rs296 Cr "As on FY26" (L275/L1052) contradicts chart FY26 net cash 387 / FY25 296 (L731) — FND-06. |
| F12 SEGMENT FORENSICS | N.A. | Deck gives geographic segment revenue/EBITDA only; no segment assets/liabilities to trend (margin observations captured at F3/F7/F16). |
| F13 BOARD OUTCOME | N.A. | No AR/AGM notice, record date, or director-appointment term dates in a deck (only an ESG "board-level ambition," L1133). |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | Duplicate section badge "04" x2 / missing "05" (L673,L874); two email domains (L54 vs L1163) — FND-07. |
| F15 ENTITY LIST DIFFS | N.A. | PRIOR_LEDGER_UNAVAILABLE — first-time coverage; no prior consolidation list to diff (set baseline for Q2 FY27). |
| F16 DROPPED/REFRAMED DISCLOSURES | FINDING | TV FX-masked decline (L543), EBITDA-walk base 4.2% vs 9% headline (L560 vs L517), selective baselines/Budget-Pay framing (L813/L1148) — FND-08/09/10. |
| F17 CONCALL SILENCE AUDIT | N.A. | Doctype is presentation, not transcript; monitoring checklist empty (first coverage) — no commitments-vs-call cross-reference to run. |

Blank checks: none. GATE A3: pass.

---

## COMMITMENT REGISTER (from F6 — dated/dateable management commitments)
| commitment | implied date | ref | status word |
|---|---|---|---|
| Germany to contribute towards profitability | FY27 | L1028 / s34 | expected |
| Europe margins to strengthen "meaningfully over the course of the year" | FY27 (full year) | L387-388 / s14 | expected |
| Revenue target Rs5,000-5,500 Cr | FY30 | L1004 / s34 | targeted |
| Digital = 50% of B2C revenue (from 44% FY26) | FY27 | L1008 / s34 | underway (~45% now, L176/L658) |
| In-house brands = 60%+ of B2C (from 48.8%) | FY27 | L1018 / s34 | underway (Q1FY27 already 57.2%, L410) |
| Lifestyle products = 50% of B2C (from 35%) | medium-term | L1019-1020 / s34 | targeted |
| AI product-scheduling tool: "in beta last year -> now in production" | achieved | L463-464 / s16; L1027 / s34 | completed (beta->production milestone) |
| AI-assisted Shopify migration "completed in ~6 months" | achieved | L458 / s16 | completed |
| "All 4 channel sites migrated to Shopify" | achieved | L1057 / s35 | completed |
| 1 million meals/school day (ESG) | FY40 | L1133 / s38 | board-level ambition |
| Scope 1&2 -60% absolute; Scope 3 intensity -70% (FY24-25 base) | 2035 | L1142 / s38 | committed (SBTi) |

Status-change note for Role 5: the AI product-scheduling tool's "beta -> production" transition (L463) is a genuine milestone confirmation vs boilerplate. Germany's "first full year of positive EBITDA achieved in FY26" (L700/L1027) is a delivered prior commitment; the live open commitment is the FY27 profitability step (FND-02).

---

## A4 HANDOFF — questions to convert
- FORWARD-SIGNAL (surface prominently): FND-02 (Germany FY27 profit step), FND-03 (Europe margin recovery hedge), FND-08 (TV volume+ASP contraction masked by FX).
- AMBIGUOUS (turn into management questions): FND-04 (MAT-credit-adjusted PAT / true QoQ PAT trend), FND-06 (is FY26 net cash Rs296 Cr or Rs387 Cr; Q1FY27 figure), FND-09 (what is the 4.2% EBITDA-walk base and why below the 9% reported Q1FY26 margin), FND-10 (Budget Pay receivables/credit exposure; normalize baseline years).

```yaml
stage: A3-forensics
company: "VAIBHAVGBL"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/vaibhavgbl-q1fy27/work/forensics_presentation_vaibhavgbl_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: N.A.
  F10: FINDING
  F11: FINDING
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "FND-01", check: "F1", line: "472", classification: "NEUTRAL-FACT", implication: "Sole zero-standing item is a promotional 0% marketplace take-rate comparator, not a transaction template line."}
  - {id: "FND-02", check: "F6", line: "1028", classification: "FORWARD-SIGNAL", implication: "Germany profitability contribution promised from FY27 - promise-vs-delivery tracker item."}
  - {id: "FND-03", check: "F7", line: "387-388", classification: "FORWARD-SIGNAL", implication: "Pre-emptive hedge that Europe margins (Q1FY27 EBITDA ~1% of rev) recover over FY27; next-quarter Europe margin is the tell."}
  - {id: "FND-04", check: "F8", line: "540", classification: "AMBIGUOUS", implication: "Rs47.2 Cr MAT credit excluded from Q4FY26 PAT masks a QoQ PAT decline; future ETR/cash-tax step-up."}
  - {id: "FND-05", check: "F10", line: "1042", classification: "NEUTRAL-FACT", implication: "EPS +73% vs PAT +74% - minor dilution tell; reconcile share count at results filing."}
  - {id: "FND-06", check: "F11", line: "275", classification: "AMBIGUOUS", implication: "Net cash Rs296 Cr As-on-FY26 contradicts chart FY26=387 / FY25=296 (Rs91 Cr, >30% gap)."}
  - {id: "FND-07", check: "F14", line: "673", classification: "NEUTRAL-FACT", implication: "Duplicate section badge 04 / missing 05 and two email domains - cumulative drafting-discipline data point."}
  - {id: "FND-08", check: "F16", line: "543", classification: "FORWARD-SIGNAL", implication: "TV revenue +9% YoY in INR masks TV volume -3.9% and USD ASP -4.4%; TV contracting on price and volume, FX-flattered."}
  - {id: "FND-09", check: "F16", line: "560", classification: "AMBIGUOUS", implication: "EBITDA margin walk base 4.2% contradicts reported Q1FY26 EBITDA margin 9% (L517) - undisclosed normalization."}
  - {id: "FND-10", check: "F16", line: "813", classification: "AMBIGUOUS", implication: "Selective FY20/FY25/FY26 baselines; Budget Pay 38% framed as affordability not receivables; PAT 50% vs arithmetic 47.4%."}
forward_signals: ["FND-02", "FND-03", "FND-08"]
ambiguous: ["FND-04", "FND-06", "FND-09", "FND-10"]
commitments:
  - {commitment: "Germany to contribute towards profitability", implied_date: "FY27", ref: "L1028/s34", status_word: "expected"}
  - {commitment: "Europe margins to strengthen meaningfully over the year", implied_date: "FY27", ref: "L387-388/s14", status_word: "expected"}
  - {commitment: "Revenue target Rs5,000-5,500 Cr", implied_date: "FY30", ref: "L1004/s34", status_word: "targeted"}
  - {commitment: "Digital 50% of B2C revenue (from 44%)", implied_date: "FY27", ref: "L1008/s34", status_word: "underway"}
  - {commitment: "In-house brands 60%+ of B2C (from 48.8%)", implied_date: "FY27", ref: "L1018/s34", status_word: "underway"}
  - {commitment: "Lifestyle products 50% of B2C (from 35%)", implied_date: "medium-term", ref: "L1019/s34", status_word: "targeted"}
  - {commitment: "AI product-scheduling tool beta->production", implied_date: "achieved", ref: "L463/s16", status_word: "completed"}
  - {commitment: "AI-assisted Shopify migration completed", implied_date: "achieved", ref: "L458/s16", status_word: "completed"}
  - {commitment: "All 4 channel sites migrated to Shopify", implied_date: "achieved", ref: "L1057/s35", status_word: "completed"}
  - {commitment: "1 million meals per school day", implied_date: "FY40", ref: "L1133/s38", status_word: "ambition"}
  - {commitment: "Scope 1&2 -60% / Scope 3 intensity -70%", implied_date: "2035", ref: "L1142/s38", status_word: "committed"}
gate_a3: pass
blank_checks: []
```
