# RUN LOG — quarterly review: PARKHOSPS (Park Medi World Limited) Q1 FY27

Orchestrator: /run-quarterly. Operator: Keerti Kaushik. Run date: 2026-08-03.
Company: Park Medi World Limited | NSE: PARKHOSPS | BSE: 544645 | Sector: Hospitals.
Quarter under review: Q1 FY27 (quarter ended June 30, 2026).

## TOOLCHAIN PRECHECK
- pdftotext 24.02.0, pdfinfo, pdftoppm, tesseract: ALL PRESENT (installed poppler-utils + tesseract-ocr this session via apt).
- Read-tool PDF rendering NOT used as evidence spine (poppler unavailable at session start; installed before A1).

## PROTOCOL-FILE CHECK
- frameworks/Quarterly_Results_Review_Protocol_v1_2.md  PRESENT
- frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md PRESENT (no concall in docs; not exercised)
- frameworks/Master_Project_Prompt_v3.3.md              PRESENT

## INPUT DOCUMENTS (5 supplied, 4 unique)
| file in inputs/ | source upload | pdfinfo pages | md5(extract) | doctype decision | basis |
|---|---|---|---|---|---|
| results.pdf | 83b9baf5 | 15 | 7ccd30de... | results | Reg 30/33 Board Outcome + Unaudited Financial Results (std+consol) + Limited Review Report |
| (duplicate) | 40ccf173 | 15 | 7ccd30de... | — DROPPED — | byte-identical to results.pdf (same md5); not reprocessed |
| presentation.pdf | b92bb247 | 26 | — | presentation | Reg 30 Investor/Earnings Presentation Q1 FY27, slide structure |
| earnings_release.pdf | 68a74900 | 4 | — | release (enumerate as presentation/narrative) | Reg 30 Media Release / Earnings Release, page-based narrative + KPI table |
| monitoring_agency.pdf | 7b6f706d | 13 | — | monitoring (enumerate as results/regulatory) | Reg 32(6) CRISIL Monitoring Agency Report on IPO proceeds utilization |

Doctype tokens `release` and `monitoring` are descriptive labels to avoid extract-filename collision; A1/A2 run the closest canonical enumeration path (presentation for release, results for monitoring). Orchestrator wins on extraction discipline per prompts/quarterly-00-orchestrator.md L7-9.

## COMPANY MEMORY / NOTION
- companies/PARKHOSPS.md: ABSENT (fresh coverage; no prior operator rulings/tripwires).
- runs/ prior folders for parkhosps: NONE.
- Notion live fetch: SUCCESS. Page "Park Medi World Ltd" (COMPANIES MASTER). Decision Status WATCHLIST, entry ₹101-126, MoS ₹101, Position None, Promoter Verdict MONITOR. Full monitoring checklist + 4 thesis-broken triggers + FY26 baseline captured in work/notion_thesis_brief.md and passed inline to A3/A4.

## GATES LOG
- 2026-08-03: Setup complete. A1 x4 launched in parallel (results, presentation, release, monitoring).
- GATE A1 release: PASS. 4pp/4ff, 100% coverage, unit=Millions (x0.1 to Cr), no OCR needed.
- GATE A1 monitoring: PASS. 13pp/13ff, 100% coverage, unit=Millions. A1 already flags IPO medical-equipment object deviation (~Rs 229.59mn planned vs 36.08mn actual) for A3.
- GATE A1 presentation: PASS. 26pp/26ff, 100% coverage, unit=Millions, OCR pages [7,16,20,23] all section-divider photos (no hidden data), 10 charts flagged inline. CAVEAT: this agent deleted shared work/ocr_tmp belonging to the concurrent results A1 — verify results gate carefully; re-run results A1 if any gap.
- GATE A1 results: PASS. 15pp/15ff, 100% coverage, unit=Millions. Pages 3-11 image-based, OCR 300-400dpi. Orchestrator cross-check vs clean release table: consol Q1FY27 PAT 885.93mn=release 886; Revenue 4,757.09=release 4,757; EPS 2.05=2.05; FY26 consol rev 16,793.56mn=Rs 1,679 Cr (matches Notion baseline). OCR VALIDATED. Column order = Q1FY27 | Q4FY26 | Q1FY26 | FY26. Early signals: occupancy 55.6% (vs 67.8% YoY), deferred-tax benefit (93.40)mn Q1FY27 flatters PAT.
- ALL FOUR GATE A1 PASS. Launching A2 x4 (parallel).
- GATE A2 results: PASS. notes22/lineitems63/zerostanding3/agenda3/auditorparas12/entities23/annexure10/sig5. Flags: ENTITY_CHANGE x4 (Devina Derma exit 5-Jun-26; Healplus step-down missing from Annexure-I; V3/Rudrapur; Mehar LLP pending), DISCLOSURE_INCONSISTENCY (consol IPO table drops Total row), ZERO_STANDING x3, OCR_GAP x12 (UDIN/seals). Going concern NOT FOUND (absent, recorded).
- GATE A2 presentation: PASS. slides26/numbers341/footnotes14. Flags: ZERO_STANDING (Rudrapur nil Q1 contribution), PARTIAL_OWNERSHIP (Rudrapur 80%), REPEAT_FOOTNOTE (p15=p8). DROPPED_SLIDE not computable (no prior deck).
- GATE A2 monitoring: PASS. notes15/lineitems21/zerostanding12/agenda9/auditorparas19/entities13. Flags: DELAY_DEVIATION, MISSING_UDIN, NO_TIMESTAMP, IMPORTANT_SCOPE_CARVEOUT, ZERO_STANDING x12, LINE_WRAP_SPLIT.
- GATE A2 release: PASS. pages4/lineitems55/mgmtnumbers8/notes10/entities12. Flags: UNIT_INCONSISTENCY (crs vs mn), SUBSEQUENT_EVENT (Rudrapur post-quarter), SAME_DAY_DISCLOSURE (Mehar agreement = release date), UNAUDITED, RESTATED.
- ALL FOUR GATE A2 PASS. Launching A3 forensics x4 (parallel). No prior-quarter extract (first quarterly run) -> QoQ diffs recorded as no-prior-quarter.
- GATE A3 monitoring: PASS 17/17, 100% recon. Key: medeq object 84% behind schedule (36.08 vs 229.59mn); Rs 648mn IPO cash idle, 4/5 objects dormant; Rs 2,453mn unidentified acq/GCP fully utilised no target named; CRISIL performs no audit.
- GATE A3 presentation: PASS 17/17, 100% recon. Key: ETR 15.7% vs 25.17% (F8 run on slide-24 P&L); occupancy chart axis -10% to 110% flatters 67.8->55.6% drop; ~12% IPO dilution (PAT+35 vs EPS+20); ARPOB touted improving but unquantified; 16-item dated bed roadmap.
- GATE A3 release: PASS 17/17, 100% recon. Key: occupancy -1,224bps buried in table, absent from headline/quote; QoQ softening masked by YoY framing; Mehar ~Rs107 Cr / 150+ beds = ~0.71 Cr/bed (inside trigger).
- GATE A3 results: PASS 17/17, 100% recon. Key: standalone PBT -72% YoY (parent core loss-making, other income 46.68>PBT 17.11) vs consol +28%; deferred-tax shield ~889bps ETR ~Rs93mn PAT; 83.9% of consol PAT NOT principal-auditor-reviewed + Rs26mn no-auditor; IPO object-variation postal ballot (Rs2,840mn M&A vs Rs648mn pending); actuarial OCI swing ~92% of full FY26; Healplus omitted from entity list; both acquisitions <Rs1.0 Cr/bed; going concern absent both reports.
- ALL FOUR GATE A3 PASS. Next: A4 merged analyst (Role 4 then Role 5).
- A4 COMPLETE. Verdict PROCEED WITH CAVEATS. Cash conversion INDETERMINATE (no Q1 cash-flow stmt; CFO/FCF/receivables=ND, first read H1FY27). Role 5 N.A. (no concall). S-vs-C PAT gap: Q1FY26 7.48% / Q4FY26 11.21% / Q1FY27 1.22% / FY26 13.39%. Four triggers: NONE fired -> Decision stays WATCHLIST. 15 Questions-for-Management, 17 monitorables. A4 corrected the presentation A3 per-bed unit slip (both acquisitions <1.0 Cr/bed confirmed). Flags: unaudited 83.9% of PAT, deferred-tax flattering (+35% -> ~+21% ex-benefit), standalone core loss-making, occupancy -1224bps, idle/behind IPO capex, IPO object-variation postal ballot.
- A5 adversary launched (only review + extracts + ledgers; independence absolute).
- GATE A5: COMPLETE. Coverage: every gated count reproduced on fresh pass, no orphan rows, no A2/A3 loop-back. Arithmetic: every derived metric recomputed from raw, zero mismatches. Adversarial: 3 most-positive claims each met their strongest same-text bear counter, all already grafted, none survives. loop_back_to="". One non-blocking recommendation only.
- NOTION SAVE: DONE. Full review + Questions-for-Management + monitorables + A3 scorecard + A5 verdict appended to page "Park Medi World Ltd" (364bb2b9...). Key Notes property PREPENDED with dated [03-Aug-26] line; all prior entries (31-Jul, 25-May, 30-Jun) preserved verbatim. Decision Status UNCHANGED = WATCHLIST (no trigger fired; flag-not-decide honoured).
- RUN COMPLETE. Verdict PROCEED WITH CAVEATS. Clean run, all 12 gates first-pass, A5 COMPLETE, zero loop-backs.
