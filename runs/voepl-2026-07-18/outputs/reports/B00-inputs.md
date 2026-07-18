# B00 — Input Validation & Inventory (Stage 0)

**Company:** Virtuoso Optoelectronics Ltd (VOEPL) · **Run:** 2026-07-18 ·
**run_type:** full · CMP Rs509 · Mkt cap Rs1,621 Cr

manifest.yaml present and parses. inputs/ tree non-empty. No mechanical
halt condition. Run proceeds.

## Company identity (for downstream anchoring, from rating + AR, this run)
- Incorporated 11-Sep-2015 (Nashik) as Virtuoso Optoelectronics Pvt Ltd;
  converted to public ltd Mar 2021. EMS / consumer-durables contract
  manufacturer (RAC/AC ODM, EMS/LED/PCBA, commercial refrigeration/deep
  freezers, reciprocating compressors from Jan 2026, components/polymers).
- Listed BSE SME (~2022, scrip 543597); migrated to BSE Main Board
  (in-principle Feb-2024, effective FY26; operator digest: mainboard
  effective 1-Jul-2026). ISIN INE0I0T01010.
- ICRA [ICRA]BBB (Stable), reaffirmed 3-Oct-2025.

## Inventory by subfolder
| Folder | Count | Files / note |
|---|---|---|
| prospectus | 0 | ABSENT — SME DRHP/RHP not collected |
| annual-report | 1 | FY2024-25 AR (92 pp) |
| results | 2 | two results PDFs |
| rating | 1 | ICRA 138187.pdf (BBB Stable, 3-Oct-2025) |
| concalls | 4 | Q4FY25 (Jun-25), Q2FY26 (Nov-25), Q3FY26 (Feb-26), Q4FY26 (Jun-26) — concalls_available:true |
| peer-concalls | 16 | AMBER x4, ELIN x4, EPACK x4, PGEL x4 |
| presentation | 1 | Investor_Presentation_1.pdf |
| screening | 30 | screener + AMBER/ELIN/EPACK/PGEL CSVs (BS/CF/Cust/Data_Sheet/P&L/Quarters each) |
| shareholding | 1* | OPERATOR-SUPPLIED screener SHP screenshot (see gaps) |
| announcements | 1* | OPERATOR-SUPPLIED operational digest H1-2026 (see gaps) |
| research | 0 | ABSENT |
| other | 0 | — |

Concall chronology (oldest first), confirmed from each transcript p1 subject line:
1. `Concall_Jun_2025_Transcript.pdf` = H2 & FY2024-25 (Q4 FY25 / FY25 annual)
2. `Concall_Nov_2025_Transcript.pdf` = Q2 & H1 FY2026
3. `Concall_Feb_2026_Transcript.pdf` = Q3 & 9M FY2026
4. `Concall_Jun_2026_Transcript.pdf` = Q4 & H2 FY2026
No Q1 FY26 call present (gap in the sequence). Stage 5 runs the FY26 chain
(Q2/Q3/Q4) as primary promise-delivery, with Q4 FY25 as the baseline call.

## input_gaps
- **prospectus ABSENT (MEDIUM, borderline-HIGH):** SME-IPO ~2022, so ~4 years
  pre run_date — just outside the strict ~3y RECENTLY-LISTED window, but the
  SME DRHP carries pre-IPO restated financials, the promoter/group-company map,
  and related-party history nothing else holds. Effect per DEGRADATION MAP:
  stages 2/3 build the backward baseline from the FY24-25 AR (fewer restated
  years); stage 8 sources promoter/group background from web + AR governance
  and flags the group map as web-derived not filing-anchored; FTTCP backward
  baseline runs on post-listing years and says so.
- **announcements PARTIALLY FILLED (non-anchored):** no Reg 30 PDFs collected.
  Operator supplied a mid-run operational digest (Q3/Q4 FY26 concalls +
  presentations + announcement dates), saved as
  `inputs/announcements/OPERATOR-SUPPLIED-operational-digest-H1-2026.md`.
  Status DIRECTIONAL LEAD + CROSS-CHECK, NON-ANCHORED: the Q3/Q4 concalls and
  presentation it summarises ARE in inputs/ and stages read those PDFs
  directly; the specific announcement events (OCD DTD 28-May-2026; mainboard
  migration 30-Jun-2026) have no underlying filing PDF, so treat as
  directional-to-corroborate. Stage 8 still leans on web search for material
  events; intent-and-action cross-check cannot grade Reg 30 actions off
  primary filings.
- **shareholding FILLED (anchored-equivalent):** operator supplied a screener
  SHP screenshot (Sep 2022 to Jul 2026 quarterly), saved as
  `inputs/shareholding/OPERATOR-SUPPLIED-shareholding-screener-screenshot.md`.
  Screener class, treated as anchored-equivalent for the SHP trend series.
  Closes the FII+DII UA qualifier and the promoter-holding trend. Pledge row
  NOT in this source (screener SHP carries no pledge %); pledge remains
  gap-noted, to be closed from AR/rating if stated.
- **research ABSENT:** no effect on anchored evidence (research is never
  anchored); synthesis loses one lead-generation / management-intent source.

## Manifest defect (recurring collect_to_repo v3 class)
- **sector_cap_row "Agri processing" is WRONG.** VOEPL is a consumer-electronics /
  durables EMS + contract manufacturer (AC ODM, EMS/PCBA, refrigeration,
  compressors); the collected peer set is AMBER, ELIN, EPACK, PGEL — all
  electronics/appliance EMS names. Override to evidence-maximizing default:
  Consumer electronics / EMS / durables contract manufacturing. Sector cap
  flagged for phase-3 stage-11 confirmation against the Section 1B cap table
  (same defect class as KARNIKA / OBSCP / SFL). Do NOT use "Agri processing".
- manifest `concalls_available: true` is correct this run (4 genuine
  transcripts present). NO-CONCALL MODE does not apply.
- manifest `listed_date` blank; derived SME-IPO ~2022 (see prospectus gap).

## COMPANY MEMORY
`companies/VOEPL.md` does not exist (first workup). No PRIOR RUN CONTEXT.

## Operator interaction (single permitted question)
The stage-0 empty-folder confirmation was surfaced; the operator declined the
question tool and instead supplied, mid-run, the two items above (shareholding
screenshot + operational digest), which retro-fill the shareholding gap and
partially fill the announcements gap. Read as: proceed with the remaining gaps
recorded. No further stage-0 question asked (single-question rule honoured).

```yaml
stage: B00-inputs
company: VOEPL
run_date: 2026-07-18
model: orchestrator
status: complete
run_type: full
manifest_ok: true
concalls_available: true
no_concall_mode: false
sector_cap_row_manifest: "Agri processing"
sector_cap_row_override: "Consumer electronics / EMS / durables contract manufacturing"
sector_cap_confirm_phase3: true
listed_venue: "BSE SME ~2022 (scrip 543597), migrated BSE Main Board effective FY26/1-Jul-2026"
inventory:
  prospectus: 0
  annual_report: 1
  results: 2
  rating: 1
  concalls: 4
  peer_concalls: 16
  presentation: 1
  screening: 30
  shareholding: 1   # operator-supplied screener screenshot
  announcements: 1  # operator-supplied digest, non-anchored
  research: 0
  other: 0
concall_chronology:
  - {file: Concall_Jun_2025_Transcript.pdf, period: "Q4/H2 FY2025 (FY25 annual)"}
  - {file: Concall_Nov_2025_Transcript.pdf, period: "Q2/H1 FY2026"}
  - {file: Concall_Feb_2026_Transcript.pdf, period: "Q3/9M FY2026"}
  - {file: Concall_Jun_2026_Transcript.pdf, period: "Q4/H2 FY2026"}
input_gaps:
  - "prospectus ABSENT (MEDIUM/borderline-HIGH): SME-IPO ~2022; pre-IPO restated financials, promoter/group map, RPT history unavailable; backward baseline on post-listing years; stage 8 group map web-derived"
  - "announcements: no Reg 30 PDFs; operator digest supplied (non-anchored, directional); OCD 28-May-2026 and mainboard-migration 30-Jun-2026 events uncorroborated by primary filings"
  - "shareholding: no primary SHP filing PDF; operator screener screenshot used (anchored-equivalent trend); pledge % not in source"
  - "research ABSENT: no broker notes (non-anchored anyway)"
  - "no Q1 FY26 concall in the sequence"
operator_supplied:
  - "inputs/shareholding/OPERATOR-SUPPLIED-shareholding-screener-screenshot.md (screener class, anchored-equivalent SHP trend)"
  - "inputs/announcements/OPERATOR-SUPPLIED-operational-digest-H1-2026.md (non-anchored, directional lead + cross-check)"
prior_run: none
company_memory: none
flags: []
```
