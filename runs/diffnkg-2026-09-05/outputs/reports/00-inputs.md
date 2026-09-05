# Stage 0 — Input Validation and Corpus Audit (B00)

Company: Diffusion Engineers Ltd (DIFFNKG) | Run date: 2026-09-05
CMP Rs 475 | Market cap Rs 1,777 cr | run_type: full
Sector cap row (manifest, manually corrected): "Cables / Industrial products"
Spear gate: OVERRIDE 2026-09-05 (operator), companies/DIFFNKG.md.

## FOLDER INVENTORY

| Folder | Count | Status | Notes |
|--------|-------|--------|-------|
| prospectus/ | 0 | ABSENT — HIGH gap | Listed 4 Oct 2024 (AR2026 p.868-870); ~23 months to run_date, within ~3y. IPO prospectus carries promoter/group history + restated pre-IPO financials nothing else holds. |
| annual-report/ | 2 | PRESENT | FY2026 (primary) + FY2025 (backward). Contract is 0-1; extra AR is a bonus, not a gap. |
| results/ | 0 | ABSENT — gap | No standalone quarterly results PDFs. Gate 0 runs from screening + AR financials. |
| rating/ | 0 | ABSENT — gap | Stage 10 marks rating_wc_quote unresolved; Pillar 2 defaults conservative. |
| concalls/ | 4 | PRESENT | Nov 2025, Feb 2026, May 2026, Aug 2026. concalls_available: true. Contract caps stage 5 at 3; the 3 most recent (Feb, May, Aug 2026) feed stage 5 oldest-first. Nov 2025 available beyond the cap. |
| peer-concalls/ | 6 | PRESENT | ADOR x4 (Nov24, May25, Oct25, May26), GEE/504028 x2 (May26, Aug26). |
| announcements/ | 0 | ABSENT — gap | Loses the documented-ACTION (Reg 30) record; intent-and-action cross-check runs on concall/AR only; stage 8 leans on web. |
| shareholding/ | 0 | ABSENT — gap | Stage 10 marks FII+DII unresolved; UA withheld (all-three-qualifier rule); promoter/pledge trend falls back to AR with staleness noted. |
| research/ | 0 | ABSENT | .gitkeep planted. No effect on anchored evidence. |
| screening/ | 24 | PRESENT | DIFFNKG (screener-*), GEE (504028-*), ESAB INDIA (ESABINDIA-*), ADOR (ADOR-*): BS/CF/PL/Quarters/Data_Sheet/Customization each. |
| presentation/ | 1 | PRESENT | Investor_Presentation_1.pdf (40 pp). |
| other/ | 0 | ABSENT | — |

Peer identities confirmed from screening headers: 504028 = GEE Ltd; ESABINDIA
= Esab India Ltd; ADOR = Ador Welding Ltd. All welding-consumables peers.

## FRESHNESS PAIR CHECK

| Pair | Trigger present? | Mate | Status |
|------|------------------|------|--------|
| 1. Results -> same-quarter concall | No results filing in corpus (no trigger) | Aug 2026 (Q1FY27) concall present | PASS (not triggered; results absence recorded as input_gap, not a freshness fail) |
| 2. Rating bulletin -> full rationale | No rating in corpus (no trigger) | n/a | PASS (not triggered; rating absence recorded as input_gap) |
| 3. SEBI order -> order text | None referenced at stage 0 | n/a | PASS (no referenced order; stages surface if any) |
| 4. AR -> latest audited annual results | AR FY2026 present | Latest audited annual = FY2026 | PASS (AR not older than latest audited annual) |

freshness_verdict: FRESHNESS PAIRS OK. No CORPUS GAPPED-FRESHNESS cap.

## CORPUS VERDICT

CORPUS GAPPED (plain, not freshness). Present gaps: prospectus (HIGH), results,
rating, announcements, shareholding, research. None is a freshness-pair failure,
so the gate is not capped on freshness grounds. The dossier Section 1 verdict
line is CORPUS GAPPED.

## OPERATOR CONFIRMATION (empty folders)

The operator was shown the empty-folder list in the prior turn (prospectus HIGH,
results, rating, announcements, shareholding, research) and directed "run the
full pipeline." That is the single permitted stage-0 question, answered: proceed
with the gaps. No further pause.

## SECTOR-CAP FLAG (collect_to_repo v3 defect pattern)

manifest sector_cap_row was auto-picked "Pharma / CDMO" (wrong) and manually
corrected to "Cables / Industrial products". Diffusion Engineers is a
welding-consumables, wear-plate, and superconditioning industrial company. No
dedicated welding/industrial-consumables row is confirmed in the Section 1B cap
table here. Flag sector_cap for phase-3 (stage 11) confirmation against the live
cap table; do not treat "Cables / Industrial products" as final.

## POST-IPO REBASE NOTE (for Gate 0 / FLAG-GATE0)

AR2026 states ROE/ROCE fell in FY25 because the IPO enlarged the equity base
(p.1833). A post-IPO rebase is a historical depressor, not an operating
deterioration; Gate 0 should read the backward score with this in view.

```yaml
stage: B00-inputs
company: DIFFNKG
run_date: 2026-09-05
model: inline-orchestrator
status: complete
input_gaps:
  - type: prospectus
    severity: HIGH
    reason: "Listed 4 Oct 2024 (within ~3y of run_date); IPO prospectus is the foundational promoter/group + restated pre-IPO financials document. Absent."
  - type: results
    severity: normal
    reason: "No quarterly results PDFs; Gate 0 from screening + AR financials; stage 10 latest-period fields unresolved."
  - type: rating
    severity: normal
    reason: "No rating PDF; rating_wc_quote unresolved; Pillar 2 conservative default."
  - type: announcements
    severity: normal
    reason: "No Reg 30 filings; documented-ACTION record absent; stage 8 web-leaning; intent-and-action on concall/AR only."
  - type: shareholding
    severity: normal
    reason: "No shareholding pattern; FII+DII unresolved; UA withheld; promoter/pledge from AR with staleness."
  - type: research
    severity: low
    reason: "No broker notes; non-anchored source only; no effect on anchored evidence."
  - type: concalls-beyond-cap
    severity: info
    reason: "4 concalls present; stage 5 uses 3 most recent (Feb/May/Aug 2026); Nov 2025 available beyond the 3-cap."
  - type: sector-cap-unconfirmed
    severity: normal
    reason: "manifest sector_cap_row manually corrected from wrong Pharma/CDMO to Cables/Industrial products; no confirmed welding-consumables Section 1B row; confirm at stage 11."
freshness_pairs:
  - pair: "results->concall"
    trigger_doc: "none (no results filing)"
    mate_expected: "Q1FY27 concall (Aug 2026 present)"
    status: PASS
    missing_doc: "none (trigger absent; results recorded as input_gap)"
  - pair: "rating->rationale"
    trigger_doc: "none (no rating filing)"
    mate_expected: "n/a"
    status: PASS
    missing_doc: "none"
  - pair: "sebi_order->text"
    trigger_doc: "none referenced at stage 0"
    mate_expected: "n/a"
    status: PASS
    missing_doc: "none"
  - pair: "AR->latest_audited_annual"
    trigger_doc: "AR FY2026 present"
    mate_expected: "FY2026 audited annual"
    status: PASS
    missing_doc: "none"
freshness_verdict: "FRESHNESS PAIRS OK"
corpus_verdict: "CORPUS GAPPED"
listed_date: "2024-10-04"
recently_listed: true
peers_identified:
  - "GEE Ltd (BSE 504028)"
  - "Esab India Ltd (ESABINDIA)"
  - "Ador Welding Ltd (ADOR)"
sector_cap_row_manifest: "Cables / Industrial products"
spear_gate: "OVERRIDE 2026-09-05 (operator)"
flags:
  - id: SECTOR-CAP-UNCONFIRMED
    detail: "Confirm welding-consumables cap row at stage 11."
  - id: POST-IPO-REBASE
    detail: "FY25 ROE/ROCE depressed by IPO equity base; historical, not operating."
analyst_note: >
  Operator overrode the spear gate and directed a full Phase 1 run. Corpus is
  AR-heavy (FY25+FY26), concall-rich (4), peer-rich (6), screening-complete for
  4 names, but has no prospectus (HIGH, listed Oct-2024), no results/rating/
  announcements/shareholding. Freshness pairs pass (no present trigger lacks its
  mate). Extraction: all 13 PDFs pre-rendered to page-marked text under work/txt/
  (poppler installed, cffi fixed) so no stage hits the render wall.
```
