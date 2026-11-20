# Verifier summary: QLL (Qualitek Labs Ltd), run 2026-11-15, phase 1

Scope: Verifier A (numerical), Verifier B (red flags), Verifier C (Gate 0 and Emerging Moat portion only; valuation audit pending phase 3), Verifier D (peers). Each verifier ran once (verifier_runs A 1, B 1, C 1, D 1); remediation cycles 0. Figures are INR Lakh unless a row states otherwise.

## Confidence delta (phase 1)

| Component | Value | Verifier | Basis |
|---|---|---|---|
| numerical_acceptance | 98.8 | A | 332 numbers checked; mandatory 143 of 143; 0 CRITICAL, 4 MAJOR (all source_fidelity: true); 5 false positives struck |
| redflag_coverage | 64 | B | material_found 14, material_caught 9 (caught 4 + partially caught 5); 5 MAJOR missed |
| framework_adherence | 88.7 | C | 63 of 71 rules (Gate 0 38/41 = 92.7; EM 25/30 = 83.3); valuation pending phase 3 |
| peer_utilisation | 100 | D | 12 of 12 peer transcripts SUBSTANTIVE (3 peers) |
| overall | 64 | set by redflag_coverage | band 60-74: PROCEED verdicts downgrade one level |

REWORK check: confirmed Verifier A CRITICAL 0; acceptance below 60: none; rework false.

Acceptance rates: A 98.8 | B 64 | C 88.7 | D 100.

Severity counts: A 0 CRITICAL / 4 MAJOR / 0 MINOR. B 0 / 6 / 9. C 0 / 1 / 7. D 0 / 0 / 2.

## Findings, sorted by severity

CRITICAL: none from any verifier.

| # | Severity | Verifier | Location anchor | Note |
|---|---|---|---|---|
| 1 | MAJOR | A | 01-gate0.md section 0 load-bearing fact 1 (H1 FY26 revenue base); B00 memory line | Source truth Rs 5,424.38 Lakh, growth +33.2% (PDF image H1FY27 p.11; FY26 results 20260520-dc0311a3 p.5; MD&A "Rs 54.24 Crore"). OCR text layer misread; stage 3 has the correct figure; no decision effect. source_fidelity: true. Corrected at source by erratum |
| 2 | MAJOR | A | 03-ardeep.md section 3A H1 FY27 CFO quality line | Source truth net cash change (400.51) (PDF image H1FY27 p.15; 359.17 - 2,470.14 + 1,710.46 = -400.51). OCR copy error, 0.04 Lakh. source_fidelity: true. Corrected at source by erratum |
| 3 | MAJOR | A | 07-emoat.md section 2A H1 FY27 gross capex row | Source truth intangibles under development 31 Mar 2026 = 44.21 (AR26 p.102; PDF image H1FY27 p.12); derived capex 3,578.79. OCR copy error; no effect on 56.8% of plan. source_fidelity: true. Corrected at source by erratum |
| 4 | MAJOR | A | 02-notes.md Top 15 rank 1 and B02 top_findings rank 1; 02-notes-pass1.md section 6 QTIPL and LabOps lines | Figures labelled as ITCPL and QTIPL net assets are share in CONSOLIDATED net assets (C-Note 34 p.140); own net worth per AOC-1 AR26 p.66: ITCPL 1,905.65, QTIPL -11.25, LabOps -15.71. UNANCHORED basis, unlabelled; the ratio built on it rides on that basis; stage 3 corrects it. source_fidelity: true. Corrected at source by erratum (cost 8,498.99 = 4.46x own net worth governs) |
| 5 | MAJOR | B | B05 promise row '2X revenue'; B06 Claim 2, FLAG-PEER-BASE-RATE | Standalone +47% treated as organic; Mumbai slump sale sits in standalone; organic growth below 47% by an amount NOT FOUND; B06 flag OVERSTATED on its QLL leg. Evidence: H1 FY27 results note 7 [page 5]; standalone CF FY26 goodwill 219.86 [page 7] |
| 6 | MAJOR | B | B05 Sections 2, 4; B06 Part 5 QLL test | Margin gap is in acquired subsidiaries, not new labs; B06 hypothesis test mis-aimed (OVERSTATED). Evidence: derived subsidiary EBITDA margin 18.6% H1 FY26, 25.5% H2 FY26, 14.6% H1 FY27; standalone 22.6%, 25.8%, 25.9% (H1 FY27 results [page 4], [page 11]) |
| 7 | MAJOR | B | B05 Section 2D; B06 input_gaps | ITCPL promoter group status, swap with Ultimate Holding Company at +57.5% step-up, and repeated 'external' wording not carried. Evidence: Prospectus [page 198]-[page 199]; AR 2026 [page 49], [page 114], [page 139] |
| 8 | MAJOR | B | B05 Sections 2D, 4D | ROE and ROCE contradiction between deck and AR not flagged. Evidence: Deck [page 13] 22%/17% vs AR [page 77]-[page 78] 6.9%/7.4%; derived consolidated 12.2%/9.4% |
| 9 | MAJOR | B | B05 Section 2D | Managerial pay cap hike to 35% of net profits and its unexplained withdrawal not carried. Evidence: 20260829-8f6cab84 [page 2]; 20260907-d2d6e19d [page 1] |
| 10 | MAJOR | B | B05 Section 4 load-bearing fact 1; B06 Claim 1 | Margin guide called 'settled as NOT delivered' at H1 on a seasonal series (OVERSTATED); B06 compares H2 needs with the H1 print. Evidence: same-half EBITDA margin 20.7% to 21.6%; full-year 25% needs H2 FY27 27.4-27.6% vs 25.7% H2 FY26; VIMTALABS Q2 FY27 [page 6], Q1 FY27 [page 16] |
| 11 | MAJOR | C | 07-emoat.md section 2C lines 83-94; B07-emoat.yaml line 32 (rule E08, 2C capex x historical FAT) | Recomputed 98 (total CWIP 6,977.28 Lakh at 30 Sep 2026 x FY26 FAT 1.743 = 12,158.6 Lakh = 97.6% of FY26 revenue 12,451.81 Lakh) vs field 72 (case B, CWIP less Barwala land and building 1,813.01). Field understates the as-written figure by 25.3 points; 1,813.01 is a 31 Mar 2026 value whose 30 Sep 2026 value is NOT FOUND. EM score and class unaffected. Carry 98 as headline, cases B to D as sensitivities |
| 12 | MINOR | B | B05 promise row '2X revenue' | Consolidation-timing misstatement and like-for-like +46.5% vs 77% headline not flagged. Evidence: MD&A [page 2]; AR [page 70]; deck [page 7] vs [page 8]; May 2025 deck [page 6], [page 9] |
| 13 | MINOR | B | B05 input_gaps[3], red_flags[4] | Bengaluru claim graded medium without the audited-note test; USFDA and Hyderabad deck lines merged. Evidence: AR Note 34 [page 139]; deck [page 23] |
| 14 | MINOR | B | B05 promise row 'USFDA lab / Hyderabad' | Classified 'partial'; filed record supports 'missed to date' for Hyderabad (first due H2-FY26, absent from AR 2026); spot check WRONG. Evidence: AR 2025 [page 22]; deck [page 23]; H1 FY27 results [page 5], [page 13] |
| 15 | MINOR | B | B06 Part 2A, 2E item 4 | Peer food-sample shock not linked to QLL food share, Navi Mumbai lab or subsidiary slowdown. Evidence: VIMTALABS Q4 FY26 [page 10], Q1 FY27 [page 4], Q2 FY27 [page 6]-[page 7]; deck [page 23] |
| 16 | MINOR | B | B06 2E item 8 | Management and board exits noted but not graded; 78-day gap from first Company Secretary letter to cessation not anchored. Evidence: 20260209-7b6ff1b4 [page 1]; 20260730-44102f7e [page 2]-[page 3]; 20261029-5e7edc16 [page 1] |
| 17 | MINOR | B | B05 Sections 2C, 2D | Tone shift and thin liquidity not carried. Evidence: MD&A [page 3] vs AR [page 73]; standalone cash Rs 15.41 Lakh [page 6]; current ratio 0.92 AR [page 77] |
| 18 | MINOR | B | B05 overall | Communication-care items 17-23 and 25 missed (see 12b report Section 1, items 17-23, 25) |
| 19 | MINOR | B | B06 Part 2 | Peer cross-reads on food pricing and EMI/EMC volume missed. Evidence: VIMTALABS Q4 FY26 [page 8]; Q2 FY27 [page 11] |
| 20 | MINOR | B | B05 overall | Change to main objects in the memorandum missed. Evidence: H1 FY27 results [page 1] |
| 21 | MINOR | C | 01-gate0.md section 3, line 57 (rule G06, A3 median ROE fallback) | Recomputed FY21 ROE on closing = 15.61 / -53.46 = -29.2%; median of 6 = 15.9%; A3 = 4; Block A 8; core 44. AVERAGE unchanged; DB1 not fired. B01 N/M is the sound economic reading; operator ruling requested on negative denominators (ROE and ROCE) |
| 22 | MINOR | C | 01-gate0.md section 9, M9 row line 118; M5 row line 114 (rule G34) | Recomputed M9 = 0: no tier fits +3.9pp with growth 81.3%, and missing KRSNAA data triggers PEER DATA NEEDED = 0; moat 14/60; 4 present; STRONG. Moat class unchanged; full peer data could lift M9 to 3, a fifth moat, still STRONG |
| 23 | MINOR | C | 01-gate0.md section 9, M11 row line 120 (rule G36) | Reported series FY24-FY26 CAGR 106.6% > FY21-FY23 73.5% with S&A declining: M11 = 5, moat 17; like-for-like standalone FY24-FY26 52.2% < 73.5%: tier 3. 4 moats and STRONG either way; operator ruling requested on the window definition at exactly 6 years |
| 24 | MINOR | C | 07-emoat.md lines 114, 115, 119, 135, 228 (rule E02) | Items untagged (A3 gross margin; A4 business lines; B2 defence standards JSS 55555 / MIL 810; F1 no-ESOP statement; R1 4B PPP labs); each needs a DOC, CLAIM or INFER tag. No score change by itself |
| 25 | MINOR | C | 07-emoat.md 4C line 232, recount line 182, 4B line 228; B07-emoat.yaml analyst_note line 51 (rule E11) | Customer orders are neither approvals nor policy tailwinds; on remaining R1-scope evidence R1 = 1.4 to 2.0; total 10.4 to 11.0. Class NONE unchanged; at 1.4 R1 ranks Weak and active_categories falls to B2 alone. Move the orders to 1A (LPO) or C1 |
| 26 | MINOR | C | 07-emoat.md lines 276-288 (11 rows); B07-emoat.yaml lines 33-43 (10 rows) (rule E23) | Block missing register row 'Digital / AI compliance services' (digital revenue disclosed, client dashboard usage; AR27 MD&A; 12-24 months), report line 287. Add the row to the block |
| 27 | MINOR | C | 07-emoat.md line 361 (rule E29) | Stage report written without the closing YAML block; orchestrator appended a verbatim copy that matches the block file line for line. No content effect; output-contract miss on record |
| 28 | MINOR | D | 06-peers.md Claim 4 | Claim 4 labelled two peers but cites three; Lal gives no ramp period |
| 29 | MINOR | D | 06-peers.md Caveats | Call labels differ from file names; mapping needs the Caveats note |

## Verifier B: independent flags the pipeline missed (missed[] list), sorted by severity

| # | Severity | Item | Anchor |
|---|---|---|---|
| 1 | MAJOR | Standalone +47% called organic; Mumbai slump-sale lab sits inside standalone from 1 Sep 2025; B05 and B06 adopted the claim | MD&A 20260520-78cbc582 [page 2]; AR 2026 [page 75]; H1 FY27 results 20261113-190e3152 standalone note 7 [page 5] |
| 2 | MAJOR | H1 FY27 margin gap sits in acquired subsidiaries (derived 14.6% vs 18.6% H1 FY26; revenue +9.3%) while standalone held 25.9%; MD&A named acquired entities as the FY27 margin driver | H1 FY27 results [page 4], [page 11]; MD&A [page 3] |
| 3 | MAJOR | ITCPL is a promoter group company; 50.01% bought from TIC Services (Ultimate Holding Co) and S. Khullar at Rs 2,039.4 vs Rs 1,294.6 per share a year earlier (+57.5%); results notes call them 'external equity shareholders' in three filings | Prospectus [page 198]-[page 199]; AR 2026 [page 49], [page 114], [page 139], [page 84]; results 20251112 [page 10], 20260520-dc0311a3 [page 5], [page 12], 20261113 [page 5], [page 13] |
| 4 | MAJOR | Deck FY26 ROE 22% and ROCE 17% contradict AR RoNW 6.9% and ROCE 7.4%; derived consolidated 12.2% and 9.4% | May 2026 deck [page 13]; AR 2026 [page 77]-[page 78] |
| 5 | MAJOR | Managerial pay cap proposed up from 28% to 35% of net profits, withdrawn nine days later with no reason | 20260829-8f6cab84 [page 2]; 20260907-d2d6e19d [page 1] |
| 6 | MINOR | EBITDA guide 25-27% (MD&A) vs 25-26% (deck, next day) | MD&A [page 3]; May 2026 deck [page 25] |
| 7 | MINOR | 'Crossed Rs 125 Crore' vs filed Rs 12,451.81 Lakh | MD&A [page 2]; deck [page 4]; H1 FY27 results [page 11] |
| 8 | MINOR | FY25 CEO letter says results aligned with margin targets while deck shows PAT margin 15% to 11% | AR 2025 [page 19]; May 2025 deck [page 4] |
| 9 | MINOR | AR 2025 calls 49.99% ITCPL holding a majority stake | AR 2025 [page 59], [page 181] |
| 10 | MINOR | Staff sub-counts (450/363/180/7) reused under 1000+ and 1200+ | May 2025 deck [page 15]; May 2026 deck [page 19] |
| 11 | MINOR | NABCB accreditation dated FY24-25, FY2026 and June 2026 | May 2025 deck [page 12]; AR 2026 [page 11], [page 23]; 20260625-fe69b871 [page 2] |
| 12 | MINOR | Silent drops: Karnal PPP lab, Nellore lab, FY27 R&D division | May 2025 deck [page 12]; AR 2025 [page 22], [page 23] |
| 13 | MINOR | Disclosure care: EGM corrigendum for shareholding discrepancies and allottee swap; results meeting rescheduled; '31 September'; 'within India' segment note vs Rs 333.06 Lakh overseas | 20261012-7e45c616 [page 2]; 20260922-b4cbe4e6 [page 2]; 20260515-7ab51708 [page 1]; H1 FY27 results [page 5]; AR 2026 [page 137] |
| 14 | MINOR | Vimta: food testing is 'levelled ground' vs QLL 'up the value chain' | VIMTALABS Q4 FY26 call [page 8]; MD&A [page 2] |
| 15 | MINOR | Vimta: EMI/EMC volumes are once per development cycle vs QLL EMI/EMC 'new revenue stream' | VIMTALABS Q2 FY27 call [page 11]; May 2026 deck [page 24] |
| 16 | MINOR | Main objects in the memorandum altered to add TIC and Inspection Body work after inspection was already marketed | H1 FY27 results [page 1]; May 2025 deck [page 12] |

Verifier B other positions: pipeline_flags_not_supported none; promise_delivery_spot_checks 5 checked, 4 confirmed, 1 wrong; credibility_grade_concur "lower (D): a promoter-group roll-up called 'external', an acquisition the audited notes do not record, a deal that slipped twice then vanished, false 'organic' and consolidation-timing statements, and return ratios that cannot be reproduced make this a disclosure-integrity pattern, not only guidance slippage".

## Coverage as the verifiers stated it

- Verifier A: "Mandatory tier = Gate 0 scorecard inputs (phase 1 has no verdict card or Section 1B pillar): 143 of 143 checked, 0 mismatches. Sample tier: 420 material numbers counted, 189 checked plus 25 stage 9 arithmetic steps; about 88 not checked." Unchecked by reason: stage 9 third party web market figures and stage 8 web items; board report page anchors spot checked only; stage 4 deck pp.9/17 and about 20 stage 6 peer call page anchors (number found, page not re-verified); stage 2 derived ratios 8,159.37 base, 84%, +224%, +119% not re-run. H1FY27 results pages 11, 12, 14, 15 opened as PDF images because the text layer is OCR; findings 1 to 3 come from that difference.
- Verifier B: 14 material (0 CRITICAL, 14 MAJOR) of 29 listed; 4 caught, 5 partially caught, 5 missed; material_caught 9 of 14 = 64%; caught only rate 4 of 14 = 29%. No main transcripts (no concall mode); peer calls: Vimta Q2 FY27 read pp.3-13, other 11 searched by topic; MD podcast PENDING LIVE VERIFICATION.
- Verifier C: phase 1 scope, Gate 0 (41 rules) and Emerging Moat (30 rules); valuation, expectation ledger and business narrative checks pending. Gate 0 AVERAGE, moat STRONG, EM NONE and combined AVERAGE survive every FAIL recomputation.
- Verifier D: 3 peers audited, 3 substantive confirmed; no unsupported or unused relevant peer; all claims addressed; no verdict discipline fails.

## Verifier disagreement log

Each row is a Verifier A source fidelity finding. Each was corrected at source by an orchestrator erratum appended to the stage report, and the corrected value governs downstream. No downstream step kept a flagged figure, and no source re-check cleared a flag.

| Date | Run (ticker-date) | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-11-15 | QLL-2026-11-15 | H1 FY26 consolidated revenue base and H1 FY27 growth (01-gate0.md section 0, load-bearing fact 1) | MAJOR, source_fidelity: true. Correct: Rs 5,424.38 Lakh, +33.2% (H1 FY27 results PDF image p.11; FY26 results 20260520-dc0311a3 p.5; MD&A "Rs 54.24 Crore") | Stage 1 carried an OCR text layer misread (base 3.00 Lakh low, growth 0.1 point high); stage 3 carried the correct figure; no Gate 0 score used it | GATE HELD - figure corrected at source (erratum appended to 01-gate0.md) | No decision effect. The stage 0 load-bearing fact text and company memory are web memory, never anchored evidence; this synthesis uses +33.2% only |
| 2026-11-15 | QLL-2026-11-15 | H1 FY27 consolidated net cash change (03-ardeep.md section 3A, CFO quality line) | MAJOR, source_fidelity: true. Correct: (400.51) Lakh (H1 FY27 results PDF image p.15; 359.17 - 2,470.14 + 1,710.46 = -400.51) | Stage 3 OCR copy error of 0.04 Lakh; no verifier recompute or verdict input used the flagged figure | GATE HELD - figure corrected at source (erratum appended to 03-ardeep.md) | No decision effect |
| 2026-11-15 | QLL-2026-11-15 | Intangibles under development at 31 Mar 2026 and derived H1 FY27 gross capex (07-emoat.md section 2A) | MAJOR, source_fidelity: true. Correct: 44.21 Lakh and 3,578.79 Lakh (AR26 p.102; H1 FY27 results PDF image p.12) | Stage 7 OCR copy error of 0.02 Lakh; the 56.8% of plan read is unaffected; Verifier C's E08 recompute runs on CWIP 6,977.28, not on the flagged figure | GATE HELD - figure corrected at source (erratum appended to 07-emoat.md) | No decision effect |
| 2026-11-15 | QLL-2026-11-15 | ITCPL, QTIPL and LabOps net asset basis (02-notes.md Top 15 rank 1; B02 top_findings rank 1; 02-notes-pass1.md section 6) | MAJOR, source_fidelity: true. The figures are share in consolidated net assets (C-Note 34 p.140), not own net worth; own net worth per AOC-1 (AR26 p.66): ITCPL 1,905.65, QTIPL -11.25, LabOps -15.71 Lakh | Stage 2 labelled the consolidated share as own net assets and built a cost to net assets ratio on it; stage 3's triple pass caught the basis independently (cost 8,498.99 = 4.46x own net worth) | GATE HELD - figure corrected at source (erratum appended to 02-notes.md); the ratio on the mislabelled basis is withdrawn and 4.46x governs | Goodwill red flag stands on the corrected basis |
