# A3 FORENSIC NOTES — ADF Foods Limited (ADFFOODS) — Q1 FY27 (quarter ended 30 June 2026) — DOCTYPE: PRESENTATION

Source extract: `runs/adffoods-q1fy27/work/extract_presentation_adffoods_q1fy27.txt` (50 pages, 1362 Read-tool lines)
Ledger reconciled: `runs/adffoods-q1fy27/work/ledger_presentation_adffoods_q1fy27.md` — all 285 Table-2 rows + Tables 1/1a/3/4/5 read verbatim at cited lines. Reconciliation: 100%.
Prior-quarter deck: NOT AVAILABLE (no prior ledger supplied). Per task, F16 deck-to-deck diff was NOT runnable; F16 is instead run against the FY26 AR / prior-guidance baseline in the Notion thesis and the not-possible-diff is flagged (finding F16-10).
Doctype applicability applied: F16 in full; F6/F7 (forward + hedge phrase mining) and F11 (equity figure) run because the deck carries them; F2 and F12 run because the deck carries both standalone/consolidated and segment revenue/EBITDA. F1, F3-F5, F8-F10, F13, F15, F17 are N.A. (relevant figures not carried on this doctype).

---

## FINDINGS TABLE
id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication

| id | check | ledger ref | line / slide | verbatim quote | class | forward implication |
|---|---|---|---|---|---|---|
| F2-1 | F2 | T2 p10/p11 PAT & p12 PAT | L341 & L424 (consol PAT 17.3) vs L388/L443 (standalone PAT 18.3); Q1FY26 L425 15.2 vs L443 17.0 | "PAT of INR 17.3 Crores" (consol) vs "INR 18.3 Crores" (standalone) | FORWARD-SIGNAL | Consolidated PAT sits BELOW standalone PAT in both Q1FY27 (17.3 < 18.3) and Q1FY26 (15.2 < 17.0): overseas subsidiary cluster is still loss-making at the PAT line (drag ~1.0 Cr Q1FY27, ~1.8 Cr Q1FY26). Narrowing but not gone; live against tripwire #9 (₹5.18 Cr subsidiary loss expanding to ₹15 Cr). A4 question: subsidiary-wise P&L and Australia/Ireland burn. |
| F6-1 | F6 | T2 p10 Surat, p37 CAPEX | L329-330 (p10); L1020-1023 (p37) | "has commenced commercial deliveries and initial container shipments" | FORWARD-SIGNAL | Surat status moved to "commenced… initial container shipments." Word "initial" signals ramp is nascent — consistent with a withheld utilisation %. Dateable milestone for the promise-vs-delivery tracker; next quarter must show a shipment cadence / utilisation number. |
| F7-1 | F7 | T2 p10 macro; p12 bullet | L319-320 (p10); L400-403 (p12) | "shipping and Container constraints limiting the full conversion of Customer demand into revenue" | FORWARD-SIGNAL | New/prominent hedges: "ongoing West Asia conflict", "vessel shortage, elevated fuel & ocean freight rates", and an order-book "conversion" hedge. The West Asia hedge maps directly onto the GCC (~15% of revenue, ~zero since Mar-26) that the FY27 ₹900 Cr guidance was explicitly conditioned on — see F16-1. Pre-emptive framing of a soft near-term top line. |
| F12-1 | F12 | T2 p14 Distribution EBITDA & revenue | L476-485 (p14); CHART L492 | "17.4% … 11.7% … 11.5%" (Distribution EBITDA margin); EBITDA "3.6 … 3.7 … 2.7" | FORWARD-SIGNAL | Distribution segment EBITDA margin roughly halved YoY (17.4%→11.5%) and absolute EBITDA fell 3.6→2.7 Cr YoY; revenue also fell QoQ (31.7 Q4→23.3 Q1FY27 per AMBIGUOUS_CHART_MAPPING). Deterioration is in the chart but not narrated. (Segment assets/liabilities not disclosed — the balance-sheet leg of F12 remains dark.) A4: what drove Distribution margin compression. |
| F14-1 | F14 | T2 p37 plant text | L1027 (p37) | "existing plants in Nadiad & Nasik" | NEUTRAL-FACT | Entity-name spelling inconsistency ("Nasik" on p37 vs "Nashik" on p6/p7/p37 map). Individually immaterial; logged as a cumulative drafting-quality data point only. |
| F16-1 | F16 | T2 p7, p19 guidance | L225 (p7); L590 & CHART L629 (p19) | "Strong Momentum upwards of INR 900 crores revenue in FY27" | FORWARD-SIGNAL | Deck retains the unchanged "upwards of ₹900 Cr" headline as an UNCONDITIONAL "900+" bar, but the prior (FY26 AR) framing was explicitly Gulf-conditional: ₹800-850 Cr (zero GCC) vs ₹925-1,000 Cr (GCC normalised). The conditional bifurcation is DROPPED while the very condition (GCC/West Asia) is stated as impaired on p10. Guidance softening masked behind a static headline. Also p7 "Moving towards ₹1,000 Crore Revenue" (undated). A4: reconfirm the GCC-zero vs GCC-normalised bands. |
| F16-2 | F16 | T2 p37 Surat | L329-330 (p10); L1020-1023 & L1013 (p37) | "Surat Greenfield expansion (~INR 90 crores – Phase 1)" | FORWARD-SIGNAL | Surat plant UTILISATION % is absent — the single most-monitored Q1 master-gate item (Green ≥35%, Red <25%). Surat's 10,000 MT frozen capacity is also not broken out (deck shows only total ~38,000 MT). Cost stated ~₹90 Cr (Phase 1) vs ₹50.52 Cr capitalised 12-Mar-2026 per AR — reconcile (project cost vs capitalised?). With only "initial container shipments," utilisation is likely low; the omission reads as avoidance. A4: Surat utilisation % and FY27 revenue contribution (prior guide ₹40-50 Cr). |
| F16-3 | F16 | T2 p23 Truly Indian; contrast p22 Ashoka chart | L711 (Ashoka chart) vs p23 L713-747 (no TI revenue) | Ashoka has "Ashoka Brand Sales (INR Cr.)" chart; Truly Indian slide carries none | AMBIGUOUS | Ashoka gets a full FY21-FY26 brand-sales chart (308 Cr FY26); Truly Indian gets only store count (3,000+) and social-reach stats — NO brand revenue. Prior communications carried Truly Indian ~$4-4.5M "doubling." Selective disclosure of the brand that is the US-mainstream thesis leg. A4: Truly Indian FY26 revenue and YoY. |
| F16-4 | F16 | T2 p31 retail campaigns | L923 (p31) | "Costco TX Rotation, Whole Foods Market national endcap!" | FORWARD-SIGNAL | Costco is described as a "TX Rotation" — a rotational/trial placement, NOT a permanent listing. Q1 master-gate item 5 needs "Costco permanent" (Green); "trial extended/de-listed" is Red. Safeway (named in the thesis one-liner) is absent from the deck entirely. Costco conversion remains an open catalyst, not confirmed. A4: Costco permanent-listing status and Safeway. |
| F16-5 | F16 | T2 p10 business update; p26/p34/p35 ADF Soul | L327 (p10); p26 L840-843; p35 CHART L986 | "ADF Soul strengthened its domestic brand presence with refreshed leadership" | AMBIGUOUS | ADF Soul run-rate is ABSENT (Q1 master-gate wants >₹1 Cr/mo Green; "vague/absent" is Red). Only SKU counts and retailer logos. "Refreshed leadership" is a euphemism that may confirm the monitored risk of a SECOND sales-head churn (checklist item 11 Red). A4: ADF Soul monthly run-rate and what "refreshed leadership" means. |
| F16-6 | F16 | T2 p13 charts | CHART L454; bars L423-425 | "196.7 … 167.3" (consol revenue Q4FY26 vs Q1FY27); PAT "25.9 … 17.3" | FORWARD-SIGNAL | All three consolidated metrics fell sequentially Q4FY26→Q1FY27: revenue 196.7→167.3 (-15%), EBITDA 34.3→29.7 (-13%), PAT 25.9→17.3 (-33%). Deck narrates ONLY YoY (+25.9% / +26.0% / +13.4%). Q1FY27 consol revenue 167.3 is below the master-gate Red line (<₹180 Cr) and Q1 annualised (~₹669 Cr) is far below the ₹900 Cr target — implies a heavy, unquantified H2 skew. (Q1 is seasonally weakest, but the YoY-only framing hides the gap to guidance.) A4: bridge Q1 run-rate to ₹900 Cr. |
| F16-7 | F16 | T2 p10/p11 & p12 margins | L341 (consol PAT 10.3% vs Q1FY26 11.5% L425); L392/L443 (standalone 15.1% vs 16.9%) | "PAT Margin at 10.3%" (was 11.5%) | FORWARD-SIGNAL | PAT grew only 13.4% while EBITDA grew 26.0% (consol); standalone PAT +7.6% vs EBITDA +22.6%. PAT margin compressed both consol (11.5%→10.3%) and standalone (16.9%→15.1%). The wedge is below-EBITDA (Surat depreciation now in P&L without full revenue ramp, plus interest/tax). Deck states the margins but does not explain the compression. Forward: PAT-margin drag persists until Surat utilisation lifts. |
| F16-8 | F16 | T2 p48 PAT; T3 footnote F3 | L1298 (96.8#); L1316 footnote | "#PAT excludes exceptional items of INR 6.8 crores due to labour code" | NEUTRAL-FACT | FY26 PAT is shown as 96.8 EX-exceptional (reported 89.92 per AR) — a +7.6% presentational uplift, transparently footnoted. The p9 claim "PAT grew at a strong ~20% CAGR over 4 years" holds on 96.8 (~18.9%) but is ~16.7% on reported PAT. Note the adjusted basis; not a red flag, but do not carry 96.8 as reported PAT downstream. |
| F16-9 | F16 | T2 p14 Distribution rev; p49 dividend | L180-flag/L492 (p14); L281/L1353 (p49) | "FY24 (first label) 13.2 … FY24 (second/duplicate label) 43.9" | AMBIGUOUS | Two chart-mapping ambiguities the enumerator flagged: (a) p14 Distribution revenue bar-to-quarter mapping unclear (20.7/31.7/23.3); (b) p49 dividend chart shows "FY24" twice with 13.2 and 43.9 (likely regular vs special/buyback dual-series, not an error, but unlabelled). Low-severity; verify against AR dividend/buyback schedule. |
| F16-10 | F16 | Notion thesis (Reg 30 29-Jul-2026); T5 | Notion L87; T5 L312-315 | "a NEW wholly-owned STEP-DOWN subsidiary in Ireland (EUR 20,000) 'to support growth plans in Europe'" | FORWARD-SIGNAL | Deck-to-deck diff was NOT possible (no prior ledger — flagged per task). Against the AR/thesis baseline: the same-day (29-Jul-2026) Reg 30 Ireland step-down subsidiary — a fresh Europe-expansion entity — is ABSENT from the deck despite the deck's Germany/Truly-Indian Europe theme. A material, dateable entity-list addition not surfaced in investor communication this quarter. A4: Ireland entity purpose, capital plan, and Europe roadmap. |

---

## CHECKLIST SCORECARD (all 17; one status each)

| Check | Status | Basis (one line) |
|---|---|---|
| F1 Zero-value standing line items | N.A. | Deck carries no statutory line-item template; A2 confirms ZERO_STANDING none (p48 table fully populated across FY22-26). |
| F2 Standalone vs Consolidated decomposition | FINDING | F2-1: consolidated PAT below standalone PAT in both periods = overseas subsidiaries loss-making (drag ~1.0 Cr Q1FY27). |
| F3 Shell-entity detection | N.A. | No standalone-vs-consolidated cost-line detail in a presentation. |
| F4 Unaudited contribution ratio | N.A. | No auditor Other Matters / component-auditor disclosure on this doctype. |
| F5 Going concern / EoM scope | N.A. | No auditor report or EoM paragraph in the deck. |
| F6 Forward-commitment phrase mining | FINDING | F6-1: "has commenced… initial container shipments" (Surat) + multiple "expected to / proposed / will continue" commitments — see Commitment Register. |
| F7 Hedge phrase mining | FINDING | F7-1: West Asia conflict + vessel/freight hedges and order-book "conversion" hedge; ties to GCC-conditional guidance. |
| F8 Tax forensics | N.A. | Deck carries no tax line / PBT / ETR (p48 shows PAT only). |
| F9 OCI forensics | N.A. | No OCI / actuarial disclosure in the deck. |
| F10 Share count and dilution | N.A. | Deck carries no share count or EPS (dividend amounts only, no per-share). |
| F11 Reserves and net worth tie-out | PASS | Deck carries Equity FY22-26 (345.6→571.9); monotonic and consistent with retained earnings less dividends; no paid-up/other-equity split and no third-party number to reconcile against; nothing anomalous. |
| F12 Segment forensics | FINDING | F12-1: Distribution EBITDA margin halved YoY (17.4%→11.5%), EBITDA fell 3.6→2.7 Cr; segment assets/liabilities not disclosed. |
| F13 Board outcome beyond results | N.A. | No board-meeting outcome / AGM / record date / director term dates on the deck (p43 bios carry no DIN or dates). |
| F14 Note-drafting inconsistencies | FINDING | F14-1: "Nasik" vs "Nashik" spelling variant (p37); immaterial, logged cumulatively. |
| F15 Entity list diffs | N.A. | Deck carries no consolidation/entity list (new Ireland/Australia subs captured under F16-10). |
| F16 Dropped / reframed disclosures | FINDING | F16-1..F16-10: GCC-conditional band dropped, Surat utilisation absent, Truly Indian revenue absent, Costco still "rotation", ADF Soul run-rate absent, QoQ decline masked, PAT-margin compression, ex-exceptional PAT, chart-mapping ambiguities, Ireland sub absent; deck-to-deck diff not possible (flagged). |
| F17 Concall silence audit | N.A. | No transcript supplied; presentation doctype. Monitoring-checklist silences captured under F16 for A4. |

---

## COMMITMENT REGISTER (from F6)

| Commitment | Implied date | Ref (line / slide) | Status word |
|---|---|---|---|
| Surat greenfield Phase 1 — commercial deliveries & initial container shipments | From Q4 FY26, ramping FY27 | L329-330 (p10); L1020-1023 (p37) | commenced ("has commenced… initial") |
| FY27 revenue "upwards of ₹900 Cr" | FY27 | L590, CHART L629 (p19) | guidance / underway |
| "Moving towards ₹1,000 Crore Revenue" | undated (long-term) | L225 (p7) | intends |
| Brownfield & debottlenecking + Nadiad cold-storage upgrade | done | L1025-1029 (p37) | completed |
| Retort Expansion + additional brownfield / infrastructure | done | L1031-1035 (p37) | completed |
| AEO-T3 certification (faster clearance, WC efficiency) | Q1 FY27 | L331-332 (p10); L1104-1118 (p41) | completed (achieved) |
| Nadiad hybrid renewable — meet ~70% of plant power | undated (future) | L1241 (p46) | proposed / "expected to" |
| Ashoka to "continue to lead," 20-25% CAGR | FY27+ | L599-606 (p19); L702-707 (p22) | forward / underway |
| Truly Indian — "replicate Germany's success in the USA," expanded range | ongoing | L604-608 (p19); L742-743 (p23) | underway |
| Aggressive ADF Soul growth via e-commerce & modern trade | ongoing | L840-843 (p26) | underway |

---

## NOTES FOR A4
- Highest-value forward signals to convert to management questions: F16-1 (GCC-conditional band dropped while GCC impaired), F16-2 (Surat utilisation withheld), F16-4 (Costco still rotation), F16-6 (QoQ decline + gap to ₹900 Cr), F16-7 (PAT-margin compression), F16-3/F16-5 (Truly Indian revenue & ADF Soul run-rate absent).
- Monitoring-checklist items the deck is SILENT on (would be F17 rows on a transcript; surfaced here): Surat utilisation %, CFO/PAT (no cash-flow in deck), WC days / named WC initiative, ADF Soul run-rate, Costco permanent status, UK-India FTA, promoter pledge, subsidiary loss trajectory, ex-Other-Income EBITDA margin. The named-WC-initiative silence now extends this deck (thesis notes it absent across prior artefacts).
- Deck-to-deck diff explicitly NOT possible (no prior-quarter ledger). Recommend A4/pipeline request the Q4 FY26 deck ledger to convert F16-3/F16-5 (absent brand revenue) into a true dropped-disclosure confirmation rather than a baseline-comparison inference.
