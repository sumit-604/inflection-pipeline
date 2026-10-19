# A3 FORENSIC NOTES: presentation, KROSS (Kross Limited), Q2 FY27

Source of record: A1 fulltext `runs/kross-q2fy27/extracted/kross-presentation-q2fy27-fulltext.md` (788 lines, 38 pages), A1 structured `...-structured.md` (R001-R665), A2 ledger `runs/kross-q2fy27/work/ledger_presentation_kross_q2fy27.md` (R001-R665 plus ledger-only row M001, loop iteration 1). A3 did not open the source PDF or `inputs/`.
Prior-quarter fulltext: none supplied. Notion page (`work/notion-thesis.md`) is memory, not evidence. It is used only as the checklist and for the "vs memory" columns.
Model: claude-opus-5-5. First run 2026-10-19. Loop iteration 1 (M001) 2026-10-20.

## 0. Ledger reconciliation

- Ledger rows: 666. That is 665 structured IDs (R001-R665) plus 1 ledger-only row (M001, MISSING_FROM_STRUCTURED, added by A2 in loop iteration 1). Orphans: none (A2).
- Rows read at their cited fulltext line: 666 of 666 (100%). The fulltext was read in full (lines 1-788), so every cited line was covered. M001 was re-read verbatim at L339-356 in loop iteration 1. Spot re-reads of the conflict rows: R046/R047 (line 114), R260/R263/R273 (lines 246-259), R265/R266 (line 247), R284/R285 (lines 278-280), R654-R656 (line 785), R657-R665 (lines 787-788), R390-R392 (lines 511-515), R049/R063 (lines 116, 131-135).
- Superseded rows: 21 (R195-R241, R348-R361). Live values used: R650-R665 (image transcription, fulltext lines 784-788). No finding is built on a superseded row.
- LAYOUT_SCRAMBLED rows R439-R608 (pp30-31): read and accounted for. **No finding is built on them**, per the A2 instruction. Where a candidate pairing is mentioned below, it is labelled "candidate, not evidence".
- FOOTNOTE_UNRESOLVED: R335 (line 370), R337 (line 393). Used only in F14.
- M001 cross-references "press release p1 R063/R073". A3 was not given the press-release extract. Its cross-reference rows have the same IDs as this deck's R063/R073 but come from a different document, so A3 did not read them, and no finding here rests on the press release.
- Line check: all p8 arithmetic holds within rounding (Revenue - COGS = GP; GP - Employee - Other = EBITDA; EBITDA + OI - D&A - FC = PBT; PBT - Tax = PAT) for every column, except the H1 PAT/EPS item in FN-07.
- Correction from the first run: FN-08 (i) said p15 shows "2023 Established foundry Unit-V". That is withdrawn. The p15 year column cannot be resolved from the text layer (A2 M001: it "falls among 2006-2019 headers"). Only p24 (L511-515) dates the HPML foundry to 2023.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN-01 | F6 | R046, R047, R258-R266, R273, R284, R285 | L114, L246-259, L278-280 (p5, p11, p12) | "production trials targeted for February–March 2027" / "Production trials planned for Q4 FY2027." / "~18 months proposed capacity completion timeline" / "120,000 tons proposed capacity addition" | AMBIGUOUS | No commercial-production date appears anywhere in the deck. Only "trials" are dated. The Q1 call (memory) said "commercial Q4 FY27". The p11 slide still labels the capacity "proposed" and the capex "planned" while p5 says "mills installed". The 18-month clock has no start date. If it runs from today, completion is about Apr-2028. Leaning bear: seamless revenue starts in FY28 at the earliest, and the full ramp comes after that. A4 question: give the commercial-production date and the start date of the 18-month clock. |
| FN-02 | F6 | R049, R057, R063, R390, R391, R400, M001 | L116, L131-135, L511-515, L567 (p5, p6, p24, p27) | "High-pressure moulding line (Foundry) Progressing as planned to double existing casting capacity." / "Installation of High-Pressure Moulding Line" | AMBIGUOUS | Memory says the HPML was due Sept-2026. The deck covers the period to 30-Sep-2026 and says "progressing", not "commissioned". It gives no date. Casting is the most used shop: "75% Capacity Utilization" in H1 (L567). A slip caps casting volume first. A4 question: give the commissioning date, the capacity before and after, and the date of first commercial output. Identity of the line: see FN-18. |
| FN-03 | F6 | R031, R131-R143, R144-R146, R152-R154, R168-R171 | L103, L185-190 (p5, p8) | "Price revisions with most OEMs and Tier-1 customers concluded, supporting profitability despite input-cost pressures." vs "Gross Profit Margin 43.9% 44.8% 46.2%" | FORWARD-SIGNAL | Gross margin fell 230 bps YoY and 90 bps QoQ, even though the deck says the price revisions "concluded". EBITDA margin rose 175 bps YoY. The gain came from cost absorption: employee cost fell from 6.7% to 4.6% of revenue (+217 bps) and other expenses from 28.2% to 26.3% (+186 bps). These two offset the -230 bps gross-margin drop. The margin gain is volume leverage, not price. It reverses if volume stalls. "Most" means some customers have not settled. A4 questions: does Q2 COGS hold a retrospective steel settlement (a one-off)? Which customers are still open? Does the conversion-cost pass-through (pending, per memory) land in Q3? |
| FN-04 | F16 | R662-R665 (supersede R355-R361), R362 | L788, L430-443 (p20) | "Q1FY27 Top 5 Clients 59.47% ... Q2FY27 Top 5 Clients 64.21% \| Others 35.79%" under the title "Long Standing Customer Relationships" | FORWARD-SIGNAL | Top-5 share rose 474 bps in one quarter. Top-5 revenue was about Rs 109.6 cr and is now about Rs 151.0 cr (+38% QoQ). Others went from about Rs 74.7 cr to Rs 84.1 cr (+13%). The top 5 delivered about 81% of the Rs 50.8 cr QoQ revenue increase. Growth is concentration-led, which cuts against the "200+ customers" framing (L307). Reading caveat: this rests on the image legend colour (grey = Top 5). In the text layer, "40.53%" sits beside "Top 5 Clients" (L433) and L443 is garbled. The inverse reading would show concentration falling. Leaning bear, A3 takes the image reading. A4 questions: which top-5 account(s) drove the rise? Was it a one-time order? Confirm the legend. |
| FN-05 | F16 | R041, R062, R660, R657-R661 | L108, L131-133, L787 (p5, p6, p19) | "Exports now contribute approximately 8% of our total component business." vs "Exports 3.21%" (product-wise revenue Q2 FY27) | AMBIGUOUS | The deck's own chart puts exports at 3.21% of revenue (about Rs 7.5 cr). That is about 6.3% of the component business (3.21 / 50.69), not about 8%. The "8%" uses the narrower base (component business, not total revenue), and even on that base it does not tie to the chart. Memory records exports at about 4% with a 2-year 8% target. The headline makes that target look met when the total-revenue share is 3.2%. A4 question: give the export revenue in Rs cr and its base, and say whether exports bundled in other categories explain the gap. |
| FN-06 | F16 | R338-R343, R345, R060, R061, R657, R658 | L395-402, L131-135, L787 (p18, p6, p19) | "56.42% 59.34% 50.69%" (CV Components) / "43.58% 40.66% 49.31%" (Trailer Axles & Suspension Assembly) | FORWARD-SIGNAL | Trailer revenue was about Rs 74.9 cr in Q1 and about Rs 115.9 cr in Q2 (+55% QoQ, +103% YoY from about Rs 57.0 cr). CV components went from about Rs 109.4 cr to Rs 119.2 cr (+9% QoQ). Trailer delivered about Rs 41 cr of the Rs 50.8 cr QoQ increase. So the quarter's growth sits in the half with weaker pricing power (memory: #2 player, no retrospective mechanism), and it comes in the same quarter as the gross-margin fall in FN-03. The segment map relies on the legend order (R345 LAYOUT_ASSUMPTION). The "~49% ... Trailer" text (L131) corroborates it. A4 questions: what is the trailer volume vs realisation split? Is the trailer jump tied to the top-5 jump in FN-04? Is it a fleet or one-time order? |
| FN-07 | F10 | R215-R222, R231-R237, R654, R656, R086-R099 | L196, L198, L785 (p8), L162-173 (p7) | "Profit After Tax 19.7 13.3 8.1 143.5 ... 33.2" / "EPS (Rs.) 3.08 2.06 1.25 146.4 ... 5.14" / "PAT 47.9 \| ... \| EPS 47.9" | AMBIGUOUS | The deck holds two Q2 PAT sets. Set A: Q2 PAT 19.7, PAT margin 8.4%, PAT YoY 143.5%, EPS QoQ 47.9% (implies Q2 EPS about 3.05). Set B: H1 PAT 33.2 and H1 EPS 5.14, which imply Q2 PAT about 19.9 and Q2 EPS 3.08 (= 5.14 - 2.06). EPS YoY 146.4% is above PAT YoY 143.5%. Reading 1: Q1 PAT was restated to about 13.5 inside H1, and the Q2 EPS cell is a plug. Reading 2: Q2 PAT is about 19.9 and the 19.7 line is a different measure (the deck does not label the basis). Separating observation: the Q1 FY27 comparative column and the Q2 EPS in the results filing. Gap: about Rs 0.2 cr (0.6% of H1 PAT). Share count: the EPS series implies about 6.46 cr weighted shares through H1, which matches the pre-raise 6,45,09,422. No dilution from the Aug-2026 15,00,000-share preferential (memory) shows. A4 to cross-check the allotment date. |
| FN-08 | F14 | R390, R391, M001, R258, R259, R046, R655, R656, R240, R335, R337 | L511-515 vs L131-135 & L341-346; L246-256 vs L114; L785; L180-182; L370, L393 | "In 2023 Kross expanded its capabilities to castings by setting up a High-Pressure Mold Line (HPML) foundry which will double casting capacity" / "trailer axle manufacturers*" | NEUTRAL-FACT | Deck-internal inconsistencies. Each is small; together they are a governance data point. (i) p24 dates the HPML set-up to 2023, and p15's timeline (year column unresolved, M001) shows "Established foundry Unit-V, a high-pressure mould line", but p5/p6 say "Installation ... Progressing". The substance is in FN-18. (ii) The seamless capacity is "proposed" and the capex "planned" while the mills are "installed". (iii) The EPS QoQ cell (47.9) copies PAT QoQ (47.9), but the printed EPS gives about 49.5%. (iv) Pages 8, 30 and 31 do not label the basis (standalone or consolidated). (v) The asterisk footnotes on p17/p18 leadership claims are missing (FOOTNOTE_UNRESOLVED). (vi) The after-sales network is "~120 people" (L215) and the marketing, sales and service team is "120 members*" (L476), which may be the same headcount described two ways. |
| FN-09 | F16 | R176-R183, R199-R206 | L191, L194, L97-98 (p8, p5) | "Other Income 2.2 0.4 1.0 107.5 454.3" | AMBIGUOUS | Other income is 8.1% of Q2 PBT. It supplied about Rs 1.8 cr of the Rs 9.2 cr QoQ PBT increase (about 20%). The commentary (L97-98) is silent on it. FY26 cash was low (memory, Rs 4.4 cr), so treasury income cannot explain it. Part of the 47.9% QoQ PAT jump is non-operating. A4 question: what is in it (forex, export incentive, retrospective settlement, insurance, interest on deposits), and does it recur? |
| FN-10 | F6 | R264, R259, R191-R198, R651, R650 | L257-260, L251, L193, L785 (p11, p8) | "Funded through a mix of debt & internal accruals" / "Finance Cost 2.6 2.1 1.7 48.9" | FORWARD-SIGNAL | The capex funding statement names no equity, though memory records the Rs 63.6 cr Aug-2026 raise. Finance cost is +48.9% YoY and +22.8% QoQ, against D&A at +7.3% QoQ. Interest is rising ahead of capitalisation. With seamless trials in Q4 FY27 and a ~Rs 167 cr project, the finance-cost and D&A step-up lands before seamless revenue. Q2 PBT/finance-cost cover is about 11x, so this is not a solvency issue. It is FY28 earnings drag. A4 questions: debt drawn to date, the sanctioned term loan, the use of the preferential proceeds, and the capitalisation date. |
| FN-11 | F6 | R051, R059, R286 | L120, L281 (p5, p12) | "Cold Drawn Tubes: Forward Integration into manufacturing of Cold Drawn Tubes" | FORWARD-SIGNAL | This initiative carries no capex, capacity, timeline or funding line. It is not among the memory's growth levers. Leaning bear: it is an unbudgeted capex layer on top of the Rs 167 cr seamless project, on a cash-hungry balance sheet (memory: FCF negative for three years). A4 question: give the capex, the timing, the funding, and whether it depends on seamless output. |
| FN-12 | F6 | R243-R246, R036, R045, R067, R244, R344 | L104-105, L113, L209-214, L210, L399-402 (p5, p9, p18) | "capacity utilization is currently expected to deliver cost benefits going forward" / "actively engaging distribution partners" / "Current axle beam capacity stands at 7,500 units per month" | AMBIGUOUS | Commercial production is confirmed ("has commenced"). Utilisation is about 60-65%, and the cost benefit is still "expected", so it is not yet in gross margin (FN-03). The deck names distribution partners, not OEM adoption (memory open item: "extruded-beam OEM adoption"). The axle beam capacity of 7,500/month equals the trailer axle assembly capacity of "7,500 ... p. m." (L399-402). The deck does not separate the extrusion increment (memory: +50% axle capacity). A4 questions: OEM approvals for extruded beams, the extrusion-only capacity, and when the cost saving reaches COGS. |
| FN-13 | F6 | R043, R044, R054, R070, R071, R253-R257, R279, R280 | L112, L143-147, L232-236, L274-276 (p5, p6, p10, p12) | "Supplies progressing in line with plan" / "Further volume scale-up is expected in H2 FY27 through a structured approach focused on product validation" | AMBIGUOUS | No volume is disclosed against "800 kits/month" capacity (L236). Memory: 226 kits in Q1 (about 75/month) and a 500/month ramp "running behind". The "validation" wording means customer approvals are still open, and the scale-up date is now H2 FY27. "In line with plan" cannot be tested without the plan. A4 questions: Q2 kits supplied, the current monthly run-rate, and the date of the 500/month target. |
| FN-14 | F16 | R052, R053, R168-R175, R100-R104 | L122-124, L190 (p5, p8) | "Kross is well positioned to deliver healthy growth in FY27" / "EBITDA Margin 13.0% 12.2% 11.3%" | AMBIGUOUS | The deck gives no margin guidance. Memory says the Q1 call guided 14-15%, and Q2 is the second quarter below that band (Q1 12.2%, Q2 13.0%). Re-engage trigger 1, leg 1, fails (13.0% < ~14%). At 13.0% the margin sits between the ~12.5% bear line and the 14% gate, so the separating observation does not resolve this quarter. The page's FY27 base needs about 13.2% over Q2-Q4, and Q2 is 20 bps short. A4 question: is 14-15% still the guide, and for which period (Q4 exit or FY27)? |
| FN-15 | F6 | R028, R029, R030, R032 | L102 (p5) | "Q3 and Q4 volumes expected to be stronger than Q2 and historically also H2 is always 10-15% up than H1." | FORWARD-SIGNAL | This is a dated, testable commitment for Q3 and Q4 FY27 on the M&HCV segment. "Always" is an absolute claim; it is a backtest target for Role 5. The CV-components half grew only 9% QoQ in Q2 (FN-06). The claim is segment-level. Read company-wide (the deck does not say this), +10-15% on H1 Rs 419.4 cr would give H2 Rs 461-482 cr and FY27 about Rs 881-902 cr. That is above the page base (Rs 830 cr), so A4 should not lift the base on this line. |
| FN-16 | F6 | R040, R281-R283, R659 | L107, L274-276, L787 (p5, p12, p19) | "Target 15% of revenue share from the agriculture segment over the next two years" vs "Tractor Components 8.38%" | FORWARD-SIGNAL | Dated target: 15% by about H1 FY29. The Q2 base is 8.38% (about Rs 19.7 cr), below the memory baseline of 9-11%. Reaching it takes about +660 bps of mix in two years. Memory marks tractor as margin-dilutive. A4 questions: what is the path (new customers or wallet share), and what is the margin at 15%? |
| FN-17 | F6 | R287, R288, R289, R331 | L278-285, L348-353 (p12, p15) | "Strong international inquiries; purchase orders secured from a Sweden-based company and a leading European Tier-1 player" | AMBIGUOUS | The new European Tier-1 PO has no name and no value. The Sweden-based company is probably Leax AB (p15 "Commenced bulk exports to Leax AB"); this is an inference. A4 questions: the PO values, products, start dates, and whether the Tier-1 PO is the first beyond Leax. |
| FN-18 | F14 / F6 / F16 | M001; R390, R391, R392; R049, R057, R063; R400 | L341-346 (p15); L511-515 (p24); L116, L131-135 (p5, p6); L567 (p27) | p15: "Established foundry Unit-V, a high-pressure mould line along with its machine shop" vs p6: "Installation of High-Pressure Moulding Line (Foundry) Progressing as planned to double existing casting capacity" vs p24: "In 2023 Kross expanded its capabilities to castings by setting up a High-Pressure Mold Line (HPML) foundry which will double casting capacity" | AMBIGUOUS | The deck uses past tense ("Established", p15; "setting up ... in 2023", p24) and present-progressive tense ("Installation ... Progressing as planned", p5/p6) for what reads as the same asset. **Reading A (same line):** the Unit-V HPML has existed since about 2023. "Doubling" means filling or extending that line, not a new asset. If so, the Sept-2026 "commissioning" (memory) is a ramp milestone on a line that has taken about 3 years to approach full capacity. The p5/p6 "Installation" text is then stale carry-over, and casting capacity gain is a fill-rate story with little new capex. **Reading B (second line):** a new, second HPML is being installed beside Unit-V. p6's "double existing casting capacity" supports this: "existing" capacity already includes Unit-V. If so, there is a separate capex item and a separate commissioning date, neither disclosed (it adds to the FN-10/FN-11 capex load). Casting already runs at 75% (L567), so under A the headroom is the unfilled part of one line, and under B it is a new line. Leaning bear: neither reading is confirmed, and the Sept-2026 milestone stays unverified (FN-02). **Separating observation:** a capital-work-in-progress (CWIP) or fixed-asset entry for a new moulding line, with its rupee capex and commissioning date (results-filing CWIP note or the FY26 AR fixed-asset schedule), plus management's installed casting capacity in tonnes before and after. A4 question: "Is the high-pressure moulding line now being installed a second line in addition to the Unit-V HPML set up in 2023? Give its capex, its commissioning date, and casting capacity in tonnes per month before and after." Year caveat: the p15 timeline year for M001 cannot be resolved from the text layer. The 2023 date comes from p24 only. |

## 2. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 Zero-value standing lines | N.A. | Presentation. The A2 ledger has no ZERO_STANDING rows. A2 suggested checking pp30-31 for dashes against the rendered pages, but A3 has no source access, so it cannot. The results filing governs F1. |
| F2 Standalone vs consolidated | N.A. | The deck carries one unlabelled P&L (L180-182) and no S/C pair. The missing basis label is logged in FN-08 (iv). |
| F3 Shell-entity detection | N.A. | No S/C cost lines in the deck. |
| F4 Unaudited contribution ratio | N.A. | No auditor Other Matters in the deck. |
| F5 Going concern / EoM scope | N.A. | No EoM paragraph in the deck. No prior-quarter fulltext was supplied. |
| F6 Forward-commitment phrase mining | FINDING | Lexicon run (case-insensitive). Hits: "expected to be" L102. "commenc" L104, L113, L142-144, L209, L348. "will be" L69 (boilerplate). Extended hits: "expected" L99/104/106/211/221/233/248, "targeted" L114/142/280, "planned" L116/247/253/274, "on track" L115/134/145, "proposed" L247/256, "set to" L107, "will" L287/514, "soon" L754. M001 adds a completion word ("Established", L341). 22 commitments are in Section 3. Findings: FN-01, 02, 03, 10, 11, 12, 13, 15, 16, 17, 18. |
| F7 Hedge phrase mining | PASS | Lexicon run. The only hit is "subject to" at L75 (safe-harbour boilerplate). No "no assurance", "evaluating", "exploring", "in discussions" or "endeavour". The softer qualifiers ("most OEMs" L103, "currently expected" L104) are handled under FN-03 and FN-12. |
| F8 Tax forensics | N.A. | Doctype rule. The deck carries the total tax line only, with no current/deferred split and no earlier-year line. ETR for reference: Q2 FY27 27.0%, Q1 FY27 25.3%, Q2 FY26 31.4%, H1 FY27 26.3%, H1 FY26 26.8%, against statutory 25.17%. All are at or above statutory, so no shield is visible. The results filing governs F8. |
| F9 OCI forensics | N.A. | No OCI line in the deck. |
| F10 Share count and dilution | FINDING | FN-07. The EPS series implies about 6.46 cr weighted shares through H1, with no visible preferential effect. The Q2 PAT/EPS sets are inconsistent by about Rs 0.2 cr. Corroboration (candidate p31 pairing, not evidence): equity share capital 32.3 in FY25, FY26 and H1 FY27, consistent with no allotment by 30-Sep. The results filing governs. |
| F11 Reserves and net worth tie-out | PASS | The candidate p31 pairing ties exactly in all three columns: 32.3 + 402.2 = 434.5, 32.3 + 457.5 = 489.8, 32.3 + 490.7 = 523.0 (L641-644). Candidate other-equity growth in H1 is +33.2, which equals H1 PAT 33.2. That fits no dividend, no OCI and no preferential money in equity. The deck has no third-party net-worth figure to reconcile against. Per the A2 instruction, no finding is built on the scrambled page, and the results filing balance sheet governs. |
| F12 Segment forensics | N.A. | The deck has revenue mix only (p18, p19), with no segment assets or liabilities. The mix shift is logged under F16 (FN-06). |
| F13 Board outcome | N.A. | No board-outcome disclosure in the deck. p28 lists 8 directors (4 Rai-family executive, 4 independent) with no term dates. |
| F14 Note drafting inconsistencies | FINDING | Applied to deck-internal cross-slide drafting (there is no auditor letter in the doctype): FN-08 and FN-18. |
| F15 Entity list diffs | N.A. | No consolidation list in the deck. |
| F16 Dropped / reframed disclosures | FINDING | No prior deck was supplied, so dropped-slide diffs cannot be run (A2: "n/a (no prior ledger)"). Reframing within the deck and against memory: FN-04, FN-05, FN-06, FN-09, FN-14, FN-18 (the same asset described in both completed and in-progress tense). The silence table is in Section 4. |
| F17 Concall silence audit | N.A. | Doctype is presentation, with no transcript. The Notion checklist is still run against the deck in Section 4 (under F16), so A4 keeps it. |

## 3. COMMITMENT REGISTER (F6)

| # | commitment | implied date | ref (line / row) | status word |
|---|---|---|---|---|
| C01 | Utilisation to improve as capacity investments support growth | coming quarters (undated) | L98-99 / R027 | expected |
| C02 | M&HCV Q3 and Q4 volumes stronger than Q2; H2 10-15% above H1 | Q3-Q4 FY27 | L102 / R028-R030 | expected |
| C03 | Price revisions with most OEMs and Tier-1 customers | Q2 FY27 | L103 / R031 | concluded (completed, "most") |
| C04 | Extruded axle beam commercial production | done by Q2 FY27 | L104, L113, L142-144, L209 / R243 | commenced (completed) |
| C05 | Extrusion cost benefits | going forward (undated) | L104-105, L211 / R036, R245 | expected |
| C06 | Distribution partner engagement for extruded beams | undated | L212-214 / R246 | underway ("actively engaging") |
| C07 | Tractor momentum continues | Q3 FY27 | L106 / R038, R039 | expected |
| C08 | Agri/tractor share to 15% of revenue | about H1 FY29 ("next two years") | L274-276 / R281-R283 | target |
| C09 | Raise export contribution; broaden customer base | undated | L108-109, L282-285 / R042, R289 | committed |
| C10 | Tipping jacks volume scale-up | H2 FY27 | L112, L143-147, L233, L274 / R043, R255, R279 | expected / planned (supplies "progressing in line with plan") |
| C11 | Seamless tube mills | done by Q2 FY27 | L114, L142, L279 / R284 | installed (completed sub-step) |
| C12 | Seamless tube production trials | Feb-Mar 2027 = Q4 FY27 | L114, L144, L247, L280 / R046, R047, R265, R266, R285 | targeted / planned |
| C13 | Seamless tube completion | ~18 months, start undated (proposed) | L255-259 / R260, R263, R273 | proposed |
| C14 | Seamless capex ~Rs 167 cr, debt + internal accruals | n/a | L251-260 / R259, R262, R264 | planned |
| C15 | Forging capacity expansion (high-tonnage presses commissioned) | undated | L115, L141-148 / R048, R065 | on track (presses: commissioned) |
| C16 | HPML to double casting capacity | undated (memory: Sept-2026) | L116, L131-135, L513-515 / R049, R063, R391; conflicts with M001 L341-346 | progressing as planned (p5/p6) vs established (p15) / set up 2023 (p24): STATUS CONFLICT, see FN-18 |
| C17 | Robotic forging axle shaft capacity increase | undated | L117-119, L134-139, L267-272 / R050, R064, R275, R278 | on track |
| C18 | Cold Drawn Tubes forward integration | undated | L120, L281 / R051, R286 | stated (no status word) |
| C19 | Entry into TAG axles enabled by extrusion | undated | L271-272 / R276, R277 | strategy (no status word) |
| C20 | Export POs from Sweden-based company and a European Tier-1 | done by Q2 FY27 | L278-281 / R287, R288 | secured (completed) |
| C21 | FY27 "healthy growth" with "healthy order books" | FY27 | L123-124 / R052, R053 | expected (no number) |
| C22 | 3 MW PPA installation | "soon" | L752-754 / R644, R645 | to begin |

(22 rows. C22 is ESG and low-materiality, kept for completeness.)

## 4. DECK SILENCE TABLE (Notion Q2 checklist, growth levers and re-engage triggers vs this deck)

Count of consecutive silent quarters = 1 for every row. This is the first deck in the pipeline and no prior deck was supplied. The concall governs the final silence count.

| checklist item (memory) | what the deck says | ref | status |
|---|---|---|---|
| Trigger 1, leg 1: EBITDA margin > ~14% | 13.0% | L190 / R168 | ADDRESSED: FAILS |
| Trigger 1, leg 2: debtor days falling | p31 is scrambled; no clean receivables or days figure | L655 (scrambled) | NOT READABLE (results filing) |
| Limited Review Report qualification | not in deck | none | N.A. to deck |
| Separating observation (>=14% gate / <=12.5% bear) | 13.0%, between the two | L190 | UNRESOLVED |
| FY27 base needs ~13.2% over Q2-Q4 | Q2 13.0% | L190 | 20 bps short |
| HP moulding line due Sept-2026 | "Progressing as planned"; no date. p15/p24 call an HPML already established (2023) | L116, L341-346, L511-515 | SILENT ON DATE; LINE IDENTITY UNCLEAR (FN-02, FN-18) |
| H1 CFO and cash | no cash-flow slide; cash on p31 scrambled | none | SILENT |
| Aug-2026 preferential allotted? | no mention of the preferential or the warrants anywhere | none | SILENT (EPS implies no dilution yet, FN-07) |
| Seamless tube funding (debt vs equity) | "mix of debt & internal accruals" | L257-260 | ADDRESSED (no equity named, FN-10) |
| Top-5 customer de-growth (verification list) | share 59.47% -> 64.21% QoQ | L788 | PARTIAL (FN-04) |
| Extruded-beam OEM adoption | distribution partners only | L212 | SILENT ON OEMs (FN-12) |
| Identity of four non-promoter allottees | not in deck | none | SILENT |
| Lever: tipping jacks to 500/month | no volume | L112, L232-236 | SILENT ON VOLUME (FN-13) |
| Lever: seamless commercial Q4 FY27 | "production trials" in Q4 FY27 | L114, L247 | REWORDED (FN-01) |
| Lever: tractor 9% -> 15% | 8.38% now; 15% in two years | L274-276, L787 | ADDRESSED (FN-16) |
| Lever: exports 4% -> 8% | "~8% of component business"; chart 3.21% of revenue | L108, L787 | REFRAMED (FN-05) |
| Trigger 2: ROCE toward 20% | no ROCE in deck | none | SILENT |
| Q1-call guide: EBITDA margin 14-15% | no margin guidance | L122-124 | SILENT (FN-14) |

## 5. Notes for A4

- FORWARD-SIGNAL ids (management questions): FN-03, FN-04, FN-06, FN-10, FN-11, FN-15, FN-16.
- AMBIGUOUS ids (management questions): FN-01, FN-02, FN-05, FN-07, FN-09, FN-12, FN-13, FN-14, FN-17, FN-18.
- NEUTRAL-FACT: FN-08.
- FN-02 and FN-18 should be asked together. FN-18 decides what the HPML milestone means; FN-02 asks when it lands.
- Cross-document targets for the results-filing A3: Q1 FY27 comparative PAT and Q2 EPS (FN-07), paid-up capital at 30-Sep-2026 (F10/F11), receivables for debtor days (trigger 1, leg 2), the financial statements basis (standalone or consolidated), the composition of other income (FN-09), and any CWIP or capex note naming a moulding line (FN-18).

```yaml
stage: A3-forensics
company: "KROSS"
quarter: "Q2 FY27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/kross-q2fy27/work/forensics_presentation_kross_q2fy27.md"
ledger_reconciled_pct: 100        # 666 of 666 (R001-R665 + M001, loop iteration 1)
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: N.A.
  F9: N.A.
  F10: FINDING
  F11: PASS
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "FN-01", check: "F6", line: "L114, L246-259, L278-280", classification: "AMBIGUOUS", implication: "Seamless tube: only trials dated (Feb-Mar 2027 / Q4 FY27); no commercial date; ~18-month clock unanchored; capacity still 'proposed'. Lean bear: revenue FY28+."}
  - {id: "FN-02", check: "F6", line: "L116, L131-135, L511-515, L567", classification: "AMBIGUOUS", implication: "HPML 'progressing as planned' at 30-Sep, not commissioned; memory had Sept-2026. Casting is the most used shop (75%); a slip caps casting volume. Line identity: FN-18."}
  - {id: "FN-03", check: "F6", line: "L103, L185-190", classification: "FORWARD-SIGNAL", implication: "Price revisions 'concluded' but GM 46.2% -> 44.8% -> 43.9%; +175 bps EBITDA is fixed-cost leverage (employee +217 bps, other +186 bps vs GM -230 bps). Reverses if volume stalls."}
  - {id: "FN-04", check: "F16", line: "L788, L430-443", classification: "FORWARD-SIGNAL", implication: "Top-5 share 59.47% -> 64.21%; top-5 rev ~Rs 109.6 -> ~151.0 cr, about 81% of the QoQ increase. Concentration-led growth. Rests on the image legend reading."}
  - {id: "FN-05", check: "F16", line: "L108, L131-133, L787", classification: "AMBIGUOUS", implication: "'~8% of total component business' vs chart exports 3.21% of revenue (~6.3% of component). Narrow base makes the 8% export target look met."}
  - {id: "FN-06", check: "F16", line: "L395-402, L131-135, L787", classification: "FORWARD-SIGNAL", implication: "Trailer ~Rs 74.9 -> 115.9 cr (+55% QoQ) vs CV components +9%; growth in the half with weaker pricing power, in the same quarter as GM compression."}
  - {id: "FN-07", check: "F10", line: "L196, L198, L785", classification: "AMBIGUOUS", implication: "H1 PAT 33.2 vs Q1+Q2 33.0; Q2 EPS 3.08 = H1 - Q1 but EPS QoQ 47.9% implies ~3.05. Q1 restated or Q2 PAT ~19.9. Implied ~6.46 cr shares, no preferential dilution visible."}
  - {id: "FN-08", check: "F14", line: "L511-515, L341-346, L246-256, L785, L180-182, L370, L393", classification: "NEUTRAL-FACT", implication: "Cumulative drafting: HPML established/set up vs 'installation progressing' (substance in FN-18); 'proposed' capacity vs mills installed; EPS QoQ cell copies PAT; basis unlabelled; asterisk footnotes missing. Withdrawn: p15 '2023' year (p15 year unresolved)."}
  - {id: "FN-09", check: "F16", line: "L191, L194", classification: "AMBIGUOUS", implication: "Other income 2.2 cr (+454% QoQ) = 8.1% of PBT, about 20% of the QoQ PBT increase; nature undisclosed; part of the PAT jump is non-operating."}
  - {id: "FN-10", check: "F6", line: "L257-260, L193, L785", classification: "FORWARD-SIGNAL", implication: "Capex funded 'debt & internal accruals' (no equity named); finance cost +48.9% YoY, +22.8% QoQ vs D&A +7.3%. Interest and D&A step-up lands before seamless revenue (FY28 drag)."}
  - {id: "FN-11", check: "F6", line: "L120, L281", classification: "FORWARD-SIGNAL", implication: "Cold Drawn Tubes forward integration: no capex, timeline or funding; not in memory levers. Potential unbudgeted capex on a cash-hungry balance sheet."}
  - {id: "FN-12", check: "F6", line: "L104-105, L113, L209-214, L399-402", classification: "AMBIGUOUS", implication: "Extrusion commenced at ~60-65% utilisation; cost benefit still 'expected'; distribution partners named, not OEMs; 7,500/month equals assembly capacity, so the increment is not separable."}
  - {id: "FN-13", check: "F6", line: "L112, L232-236, L274-276", classification: "AMBIGUOUS", implication: "Tipping jacks: no volume vs 800 kits/month capacity; scale-up to H2 FY27 with 'product validation' wording, so approvals are still open; memory says the 500/month ramp is behind."}
  - {id: "FN-14", check: "F16", line: "L122-124, L190", classification: "AMBIGUOUS", implication: "No margin guidance; Q2 13.0% is the second quarter below the 14-15% Q1-call guide; trigger 1 leg 1 fails; between the 12.5% bear and 14% gate; 20 bps short of the 13.2% base need."}
  - {id: "FN-15", check: "F6", line: "L102", classification: "FORWARD-SIGNAL", implication: "Dated M&HCV claim: Q3/Q4 stronger than Q2; H2 'always' 10-15% above H1. Testable at Q3/Q4; segment-only, do not lift the company base on it."}
  - {id: "FN-16", check: "F6", line: "L274-276, L787", classification: "FORWARD-SIGNAL", implication: "Agri target 15% of revenue in two years from an 8.38% base (below the 9-11% in memory); +660 bps mix needed; margin-dilutive per memory."}
  - {id: "FN-17", check: "F6", line: "L278-285", classification: "AMBIGUOUS", implication: "POs from a Sweden-based company (probably Leax) and an unnamed European Tier-1; no value or start date."}
  - {id: "FN-18", check: "F14", line: "L341-346 (M001), L511-515, L116, L131-135, L567", classification: "AMBIGUOUS", implication: "HPML both 'Established' (p15) / 'set up 2023' (p24) and 'Installation ... Progressing' (p5/p6). A: same line, doubling = fill or extension, Sept-2026 is a ramp milestone, little new capex. B: second line, undisclosed capex and commissioning date. Separator: CWIP/capex entry for a new moulding line plus casting tonnes before/after."}
forward_signals: ["FN-03", "FN-04", "FN-06", "FN-10", "FN-11", "FN-15", "FN-16"]
ambiguous: ["FN-01", "FN-02", "FN-05", "FN-07", "FN-09", "FN-12", "FN-13", "FN-14", "FN-17", "FN-18"]
commitments:
  - {commitment: "Utilisation to improve", implied_date: "coming quarters", ref: "L98-99 R027", status_word: "expected"}
  - {commitment: "M&HCV Q3/Q4 stronger than Q2; H2 +10-15% vs H1", implied_date: "Q3-Q4 FY27", ref: "L102 R028-R030", status_word: "expected"}
  - {commitment: "Price revisions with most OEMs/Tier-1", implied_date: "Q2 FY27", ref: "L103 R031", status_word: "completed (concluded)"}
  - {commitment: "Extruded axle beam commercial production", implied_date: "by Q2 FY27", ref: "L104 L113 L209 R243", status_word: "completed (commenced)"}
  - {commitment: "Extrusion cost benefits", implied_date: "undated", ref: "L104-105 L211 R036 R245", status_word: "expected"}
  - {commitment: "Distribution partner engagement, extruded beams", implied_date: "undated", ref: "L212 R246", status_word: "underway"}
  - {commitment: "Tractor momentum into Q3", implied_date: "Q3 FY27", ref: "L106 R038", status_word: "expected"}
  - {commitment: "Agri share to 15% of revenue", implied_date: "~H1 FY29", ref: "L274-276 R281-R283", status_word: "target"}
  - {commitment: "Raise export contribution", implied_date: "undated", ref: "L108-109 L282-285 R042 R289", status_word: "committed"}
  - {commitment: "Tipping jacks volume scale-up", implied_date: "H2 FY27", ref: "L112 L233 L274 R043 R255 R279", status_word: "expected/planned"}
  - {commitment: "Seamless tube mills installed", implied_date: "by Q2 FY27", ref: "L114 L279 R284", status_word: "completed (installed)"}
  - {commitment: "Seamless tube production trials", implied_date: "Feb-Mar 2027 (Q4 FY27)", ref: "L114 L247 L280 R046 R265 R285", status_word: "targeted/planned"}
  - {commitment: "Seamless tube completion ~18 months", implied_date: "start undated", ref: "L255-259 R260 R263 R273", status_word: "proposed"}
  - {commitment: "Seamless capex ~Rs 167 cr, debt + internal accruals", implied_date: "n/a", ref: "L251-260 R259 R264", status_word: "planned"}
  - {commitment: "Forging capacity expansion", implied_date: "undated", ref: "L115 L141-148 R048 R065", status_word: "on track (presses commissioned)"}
  - {commitment: "HPML to double casting capacity", implied_date: "undated (memory Sept-2026)", ref: "L116 L131-135 L513-515 R049 R063 R391; M001 L341-346", status_word: "progressing (p5/p6) vs established (p15) / set up 2023 (p24): conflict, FN-18"}
  - {commitment: "Robotic forging axle shaft capacity", implied_date: "undated", ref: "L117-119 L134-139 R050 R064", status_word: "on track"}
  - {commitment: "Cold Drawn Tubes forward integration", implied_date: "undated", ref: "L120 L281 R051 R286", status_word: "stated"}
  - {commitment: "TAG axle entry via extrusion", implied_date: "undated", ref: "L271-272 R276", status_word: "strategy"}
  - {commitment: "Export POs Sweden-based co. + European Tier-1", implied_date: "by Q2 FY27", ref: "L278-281 R287 R288", status_word: "completed (secured)"}
  - {commitment: "FY27 healthy growth, healthy order books", implied_date: "FY27", ref: "L123-124 R052", status_word: "expected"}
  - {commitment: "3 MW PPA installation", implied_date: "soon", ref: "L752-754 R645", status_word: "to begin"}
gate_a3: pass
blank_checks: []
analyst_note: "Q2's 175 bps EBITDA gain is operating leverage, not price: gross margin fell 230 bps YoY and 90 bps QoQ although price revisions 'concluded'. Growth sat in trailer (~Rs 41 cr of the Rs 50.8 cr QoQ increase) and in the top 5 customers (~81%, on the image legend reading). Trigger 1 leg 1 fails (13.0% vs ~14%). 13.0% sits between the 12.5% bear line and the 14% gate, so the separating observation is unresolved. Debtor days cannot be read here (p31 scrambled). Seamless tube now says 'production trials' Q4 FY27, with no commercial date; lean bear: revenue FY28. The HPML is 'progressing' on p5/p6 but 'established' on p15 and 'set up 2023' on p24. Same line (a ramp milestone) or a second line (undisclosed capex)? A CWIP entry separates the two (FN-18). The EPS series implies ~6.46 cr weighted shares through H1, and H1 PAT carries ~Rs 0.2 cr not in Q1+Q2. A candidate p31 pairing (not evidence) shows share capital flat at 32.3, consistent with no preferential allotment by 30-Sep. Cold Drawn Tubes is a new, unbudgeted capex line."
```
