# CLEANMAX — Clean Max Enviro Energy Solutions Ltd
Run folders read: runs/cleanmax-2026-09-01 (origin/main)
Company file: companies/CLEANMAX.md (origin/main)

## Our base case
No FY27E / FY28E revenue, margin or profit base found. Valuation anchors are forward EBITDA:
> **Governing method:** EV/EBITDA on FY30 forward EBITDA (~Rs 4,100 Cr), FY29 exit, peer band 11-15x (thesis uses 12-14x). Equity after dilution.
Source: origin/main:runs/cleanmax-2026-09-01/outputs/final/fttcp-deliberation.md §OPERATOR-APPROVED VALUATION PILLARS L30-31
> It grows operating EBITDA from Rs 1,132 Cr in FY26 [FILED] to roughly Rs 4,100 Cr in FY30 [MGMT/INFERENCE] as the fleet reaches about 7,900 MW [MGMT].
Source: origin/main:runs/cleanmax-2026-09-01/outputs/final/role2-thesis.md L13
> **G2** Sum of bucket year-1 revenues reconciles to annualised Q1 FY27 revenue ~Rs 3,329 Cr ... PASS (Q1 FY27 total revenue 832.16 x 4 = 3,329).
Source: origin/main:runs/cleanmax-2026-09-01/outputs/valuation/role1-sotp-01.md §gates L284
> Commissioning profile. >=1.5 GW in FY27, 4.6 GW by 1-Apr-2027 [MGMT]. I model a two-year profile ...
Source: origin/main:runs/cleanmax-2026-09-01/outputs/valuation/role1-sotp-01.md L116
> FY26 revenue Rs 497.33 Cr, ~19.6% margin [FILED, Q4]. ... I do NOT extrapolate the Q1 spike. (RE Services bucket)
Source: same file L146
SOTP per share (recorded dissent): "Floor Rs 178/share (AR net debt) to de-risked central Rs 295 (AR); Rs 267 to Rs 385 on the management net-debt basis."
Source: fttcp-deliberation.md L31-32 (as read in section)

## Management guidance and promised catalysts
| FY27 capacity addition guidance | >=1.5 GW | FY27 | Q3 FY26 (reaffirmed Q4 FY26, Q1 FY27) |
| FY28 EBITDA guidance | >=Rs3,000 Cr (about 2.3-2.4x FY26's Rs1,290 Cr) | FY28 | Q1 FY27 (NEW) |
| Opex capacity floor for FY28 guidance | 4.6 GW minimum by 1-Apr-2027 | FY28 basis | Q1 FY27 (NEW) |
| Steady-state net debt at FY28 EBITDA target | ~Rs16,000 Cr | FY28 | Q1 FY27 (NEW) |
Source: origin/main:runs/cleanmax-2026-09-01/outputs/reports/05-concall.md §1B L36-48
| Land acquisition, FY27 capacity | ~80% acquired; 100% "latest by September 2026" | One-time commitment | Q3 FY26 only |
Source: same file L53
| Q3 FY26 | Bikaner (525 MW CTU) backdown resolved by CTU's own estimate, Oct-Dec 2026 | Missed/worsened | Q4 FY26: pushed to "September" per grid estimate, curtailment quantified at 30%. Q1 FY27: "this number keeps changing...difficult to hazard a guess," assume continues "for the rest of the financial year," curtailment now 70%.
Source: same file §2A L78
| Q4 FY26 | DSM impact + BESS/storage strategy to be properly announced "in three or four months" | Partial |
Source: same file L84
Calls: Q3 FY26 held 18-Mar-2026; Q4 FY26 held 13-May-2026; Q1 FY27 held 03-Aug-2026. Source: same file L5-7
ALMM2 module-cost benefit ~Rs60 lakh/MW, window to 31-Dec-2026. Source: origin/main:runs/cleanmax-2026-09-01/outputs/blocks/B05-concall.yaml guidance block

## Reported results (Q4 FY26 / Q1 FY27 / Q2 or H1 FY27)
| | FY24 | FY25 | FY26 | Q1 FY27 |
| Revenue | 1,390 | 1,496 | 1,913 | 832 |
| Operating profit | 706 | 901 | 1,132 | 421 |
| PAT | (38) | 19 | 86 | 55 |
| **Operating PBT ex other income** | **(497)** | **(62)** | **(34)** | **+51** |
Consolidated, Rs Cr. "[SECONDARY — Screener rendering of filed consolidated accounts]"
Source: origin/main:companies/CLEANMAX.md §4 L69-87
Q2 FY27: NOT FOUND (no actuals in files; "Q2 FY27 results, due late October 2026").
Source: origin/main:companies/CLEANMAX.md §2.2 L43-45

## Management's stated reasons
Bikaner: "this number keeps changing...difficult to hazard a guess" (Q1 FY27 call). Source: 05-concall.md L78
"RE Services revenue 7.32x YoY jump in Q1 FY27 ... coincides with a shrinking order book (215 MW -> 147 MW)" (analyst flag, not a management reason). Source: origin/main:runs/cleanmax-2026-09-01/outputs/blocks/B05-concall.yaml flags
Otherwise NOT FOUND.

## Risk flags raised before the result, and any overruling
All our files are dated 2026-09-01 or later; Q4 FY26 and Q1 FY27 results were published before. Flags after the fact:
> MEDIUM: Bikaner (525 MW CTU) curtailment escalated 30%->70% within one quarter; resolution timeline slipped ...
Source: origin/main:runs/cleanmax-2026-09-01/outputs/blocks/B05-concall.yaml red_flags
> Q2 FY27 operating PBT before other income prints below zero. That single next-quarter figure does the most damage to the transition thesis
Source: origin/main:runs/cleanmax-2026-09-01/outputs/final/gate-recommendation.md §Falsification line L83
Overruling: "2026-09-02: signed Mental Model v5 as PROCEED at Halt 1, overriding the v5 analyst SHALLOW WATCH recommendation" and "2026-09-04 ... PROCEED confirmed, superseding the FTTCP DEEP WATCH / analyst SHALLOW WATCH."
Source: origin/main:runs/cleanmax-2026-09-01/outputs/final/fttcp-deliberation.md §OPERATOR OVERRIDES; origin/main:companies/CLEANMAX.md L279-283

## Verdicts and dates
> Spear: OVERRIDE 2026-09-01 (operator) [Price: FAIL; CMP 1,247 vs provisional entry 610-800]. Source: origin/main:companies/CLEANMAX.md L8-29
> PROCEED WITH CAVEATS (gate-recommendation, phase 1). Source: origin/main:runs/cleanmax-2026-09-01/outputs/final/gate-recommendation.md L3
> Composite +3 / 8 -> DEEP WATCH ... Proof gate NOT FIRED. Source: fttcp-deliberation.md L6
> Decision Status WATCHLIST ... Entry Price Max Rs 715 ... vs CMP Rs 1,247. Source: origin/main:companies/CLEANMAX.md L276
> ARCHETYPE CHANGED from transition-alpha candidate to LEVERED ANNUITY BUILDER. Source: origin/main:companies/CLEANMAX.md L283
> Archetype: licence/scarcity business (RE Power Sales ...) ... RE Services (26%) is an order-book business. Source: same file L268

## Lessons archive mentions
> ## 2026-09-01 — CLEANMAX (runs/cleanmax-2026-09-01) /run-pipeline phase 1 (LESSONS_ARCHIVE.md L274)
> EVIDENCE WIN: verifier B resolved B06's self-declared "single most consequential" open question. Bikaner 525 MW is on TGNA ... (L280)
> OPEN (2026-10-03, corpus): CLEANMAX run folder holds six Vinyas filings; (L1000)
