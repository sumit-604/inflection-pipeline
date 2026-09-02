# A3 FORENSIC NOTES — MANINDS Corporate Presentation (2026-09) — doctype: presentation

Inputs read (no source access):
- Structured extraction: `runs/maninds-corppres-2026-09/extracted/maninds-presentation-2026-09-structured.md`
- Fulltext (row quotes read at line numbers): `runs/maninds-corppres-2026-09/extracted/maninds-presentation-2026-09-fulltext.md`
- A2 ledger: `runs/maninds-corppres-2026-09/work/phase2/ledger_presentation_maninds_2026-09.md`

Ledger reconciliation: 335 disclosure rows (223 NUMBER + 49 ENTITY + 20 FORWARD + 43 DATE)
plus 37 slide-inventory rows and 4 footnote rows read verbatim at cited lines. 100% read.
Prior-quarter deck: none supplied. F16 dropped-disclosure diff not runnable this run.

Note on an A2 gap I closed: A2 flagged the `EBITDA*` footnote (rows 153/165) FOOTNOTE_UNRESOLVED.
The A1 fulltext resolves it at line 775 and line 812: "* EBITDA is inclusive of Other Income,
since it's operational in nature." Material, see F14 finding A9.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A1 | F2 | NUM 159 / NUM 171 | p28 L769 / p29 L806 | standalone "PAT FY26 1,958 / FY25 1,370"; consolidated "PAT FY26 1,705 / FY25 1,532" | AMBIGUOUS | Consolidated PAT is BELOW standalone in FY26 (1,705 < 1,958) though consolidated revenue is higher. Subsidiaries added +162 Mn in FY25 but drag -253 Mn in FY26: a swing of ~415 Mn = ~25 pts of standalone PAT, far above the 5pt gate. Consolidated PAT grew +11.3% vs standalone +42.8%. Ask which subsidiary drives the loss (Merino / MISIC-Dammam carrying cost / NPC 40-day). Directly hits the Notion "consolidated vs standalone PAT divergence" tripwire. |
| A2 | F6 | FWD 1,2,5,8,9,14 | p5 L125; p16 L418; p17 L445; p32 L941; p34 L965 | "Production Targeted: Mar'2027"; "on track for Mid-September 2026"; "expected to be reflected from Q2 FY27 onwards" | FORWARD-SIGNAL | Dated management commitments for the Role 5 promise-vs-delivery tracker. See Commitment Register. Jammu is status "underway" (₹350 Cr of ₹600 Cr spent); Merino launch is dated Mid-Sep 2026 (within days of this deck); NPC full contribution deferred to Q2 FY27. |
| A3 | F8 | NUM 158 / NUM 170 / NUM 133 | p28 L767 / p29 L804 / p26 L728 | standalone "Tax FY26 672"; consolidated "Tax FY26 665"; NPC "Tax Rate (%) 11.4%" | CONFIRMATORY-NEGATIVE | Consolidated ETR 28.1% (665/2,370) exceeds standalone 25.6% (672/2,630) and the 25.17% statutory rate. Consolidated tax is nearly equal to standalone on lower consolidated PBT: subsidiary losses carry no tax shield (unrelieved). Forward offset: NPC pays only 11.4% (Saudi Zakat), so blended consolidated ETR should fall once NPC consolidates fully from Q2 FY27. |
| A4 | F10 | NUM 173 / NUM 174 | p30 L823 / p30 L825 | "Equity Share Capital FY24 324 / FY25 324 / FY26 375"; "Other Equity FY24 13,725 / FY25 15,749 / FY26 20,490" | AMBIGUOUS | Paid-up capital rose +15.7% (324->375 Mn) in FY26; a corporate action the deck never narrates on the capital line. Other Equity rose +4,741 Mn while FY26 PAT was only 1,705 Mn: ~3,036 Mn of the rise is securities premium. Implied equity raise ~Rs 300 Cr, consistent with the USD 32 Mn NPC equity leg. Ask: instrument, warrant terms, dilution %, EPS impact (deck omits EPS). |
| A5 | F12 | NUM 191 / NUM 185 | p30 L828 / p30 L847 | "Capital WIP FY24 305 / FY25 1,334 / FY26 3,258"; "Other financial liabilities FY24 278 / FY25 301 / FY26 5,797" | FORWARD-SIGNAL | Capital WIP up 10.7x in two years, Right-of-use assets 163->1,389 (8.5x): equity/debt-funded pre-commissioning build (Jammu, Dammam) with no revenue until Mar 2027. Current "Other financial liabilities" jumped 301->5,797 Mn; USD 70 Mn NPC debt at ~83.6 INR ~= 5,850 Mn, so the acquisition debt appears to sit in CURRENT liabilities = near-term refinancing / repayment. Swings the net-cash-vs-net-debt reading (Notion tripwire) toward net debt. |
| A6 | F14 | ENT 41 / DATE 32 / NUM 115 vs NUM 124 | p22 L569; p24 L639; p24 L643; p26 L715 | "40+ Year Relationships"; "since 2005"; acquire-route "15-18% EBITDA Margin"; NPC actual "EBITDA Margin (%) 24.8%" | AMBIGUOUS | Internal inconsistencies, cumulatively a governance data point. Aramco tie stated as "40+ Years" (p22) but AVL "since 2005" ~20 years (p24) and "2+ Decades" (p21). The build-vs-buy slide models NPC at 15-18% EBITDA margin, but NPC's actual CY2025 margin is 24.8%: either conservative sandbagging or a blended post-integration number. Slide-4 "Revenue Rs 3,592 Cr" equals consolidated Total Income (35,925 Mn incl. other income), not Revenue from Operations (35,639). |
| A7 | F15 | DATE 41 / ENT 37 | p32 L938 / p19 L476 | "completion of 100% acquisition on 21st May 2026"; "MISIC... wholly owned subsidiary of Man Industries" | FORWARD-SIGNAL | Consolidation scope expanded: NPC entered the group on 21 May 2026 via the new WOS MISIC; Q1 FY27 carries only 40 days of NPC. First full-quarter consolidation lands in Q2 FY27, which will materially reshape consolidated revenue, margin and debt. No prior entity list to diff; change is evidenced inside this deck. |
| A8 | F16 | NUM 144 | p26 L729-730 | "order position of USD 120 Million (Rs 1,130-1,150 crore) (including executed to date)" | AMBIGUOUS | The USD 120 Mn NPC "order book" is defined to INCLUDE orders already executed to date. A backlog normally counts pending work only, so true forward backlog is below USD 120 Mn. Soft order-book definition; ask management to split executed vs pending. Repeated as a headline value-creation number (p24 L641, p25 L696). |
| A9 | F14 | FOOTNOTE 2/3 (A2 unresolved) | p28 L775 / p29 L812 | "* EBITDA is inclusive of Other Income, since it's operational in nature" | AMBIGUOUS | EBITDA is defined to include Other Income. Stripping it: consolidated EBITDA ex-OI = 4,679 - 286 = 4,393 Mn on revenue 35,639 = 12.3%, BELOW the reported 13.0% and below the Notion 13% floor tripwire. Standalone ex-OI = (4,928-531)/34,552 = 12.7%. The margin clears the floor only because Other Income is counted inside EBITDA. |

---

## CHECKLIST SCORECARD (17 checks)

| # | Status | Basis |
|---|---|---|
| F1 | PASS | Two ZERO_STANDING rows on p30 BS (Intangibles FY24 "-"; Current Tax Assets "-" all 3 yrs, NUM 194/206). Ordinary recurring template lines (advance-tax receivable, software), not exceptional / discontinued / sale-of-subsidiary anticipators. No exceptional-item line in the P&L. |
| F2 | FINDING | A1: standalone vs consolidated PAT gap flips +11.8% (FY25) to -12.9% (FY26), ~25pt swing, above 5pt gate. |
| F3 | N.A. | Presentation carries no per-entity (subsidiary) cost-line breakdown; shell detection not computable. NPC CY2025 P&L (p26) shows real operations, so no shell among named entities. |
| F4 | N.A. | No auditor Other Matters paragraph in a presentation; unaudited-contribution ratio not derivable. |
| F5 | N.A. | No Going Concern / Emphasis-of-Matter in a presentation. |
| F6 | FINDING | A2: dated commitment lexicon hits (Mar'2027, Mid-Sep 2026, Q2 FY27, "on track", "Will be Upgraded"). Register below. |
| F7 | PASS | Only standard safe-harbor boilerplate (p36 L1013-1037: "No representation or warranty", "subject to" risks). No newly added substantive hedge on revenue lumpiness or customer concentration. |
| F8 | FINDING | A3: consolidated ETR 28.1% > standalone 25.6% > statutory 25.17%; NPC 11.4% = future blended relief. |
| F9 | N.A. | No OCI / actuarial statement in a presentation. |
| F10 | FINDING | A4: paid-up capital +15.7% and Other Equity up ~4,741 Mn vs 1,705 Mn PAT = undisclosed equity raise / dilution. |
| F11 | PASS | Net worth ties out: Equity 375 + Other Equity 20,490 = Shareholders Fund 20,865 Mn (NUM 175) = slide-4 "Rs 2,087 Cr Networth" (NUM 20). Gap < 0.1%. |
| F12 | FINDING | A5: Capital WIP 10.7x build with no revenue; USD 70 Mn acquisition debt appears in current Other financial liabilities (5,797 Mn). |
| F13 | N.A. | No board-meeting outcome, AGM notice, record date or director term dates in the deck (directors listed p8 without appointment/tenure dates). |
| F14 | FINDING | A6 + A9: internal inconsistencies (Aramco 40+ yrs vs since-2005; 15-18% vs 24.8% NPC EBITDA; Revenue vs Total Income label) and EBITDA-includes-Other-Income definition lifting margin over the 13% floor. |
| F15 | FINDING | A7: consolidation scope expanded, NPC in from 21 May 2026 via new WOS MISIC. |
| F16 | FINDING | A8: prior-deck diff NOT runnable (no prior deck supplied); reframing found within deck: NPC "order book USD 120 Mn including executed to date" = soft backlog definition. |
| F17 | N.A. | Doctype is presentation, not a concall; no transcript to run the silence audit. |

Blank checks: none. GATE A3: pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | slide / line ref | status word |
|---|---|---|---|
| Dammam Coating Plant (KSA) production | Mar 2027 | p5 L125 | targeted |
| Jammu Stainless Steel Plant production | Mar 2027 | p5 L125 / p16 L418 | underway (Rs 350 Cr of ~Rs 600 Cr capex incurred) |
| Merino Shelters project launch | Mid-September 2026 | p17 L445 | on track |
| Merino Shelters cashflow Rs 35-50 Cr | FY27 | p17 L446 | expected |
| Merino Shelters annual cashflow Rs 80-120 Cr | from FY28 | p17 L433 | expected |
| Merino Shelters revenue Rs 700-800 Cr | next 5-6 years | p17 L440 | projected |
| NPC full earnings contribution | Q2 FY27 onwards | p32 L941 | expected |
| NPC HSAW OD upgrade to 120" | undated | p21 L559 | "Will be Upgraded" (initiated) |
| Revenue CAGR 20-25% | next 5 years | p34 L965 | targeted |
| EBITDA margin to stable 15% | long-term | p34 L970 | targeted |

---

## FORWARD-SIGNAL / AMBIGUOUS flags for A4
- FORWARD-SIGNAL: A2 (commitments), A5 (build + acquisition debt placement), A7 (NPC full consolidation from Q2 FY27).
- AMBIGUOUS (convert to management questions): A1 (S-vs-C PAT drag), A4 (equity raise / dilution terms), A6 (Aramco tenure + 15-18% vs 24.8% margin), A8 (order-book "executed to date"), A9 (EBITDA-incl-Other-Income vs 13% floor).
