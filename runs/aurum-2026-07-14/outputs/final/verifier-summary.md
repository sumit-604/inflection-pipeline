# Verifier Summary (Phase 1): AURUM

Phase 1 scope: Verifier A (numerical, B12a), Verifier B (red flags, B12b), Verifier D (peers, B12d), and the Gate 0 + Emerging Moat portion of Verifier C (B12c). The valuation half of Verifier C (B10/B11) is deferred to phase 3.

## Confidence delta and acceptance rates

| Verifier | Component | Score | Acceptance rate | CRIT / MAJ / MIN |
|---|---|---|---|---|
| A (B12a) | Numerical acceptance | 95 | 95% (45 clean + 2 plausible-unanchored / 47) | 0 / 0 / 2 |
| B (B12b) | Red flag coverage | 81 | 69% strict (11 caught / 16 found); 81% coverage with partials at 0.5 | 0 / 2 / 3 |
| C (B12c) | Framework adherence (Gate 0 + EM only) | 96 | 96% (47 pass / 49 rules) | 0 / 0 / 4 |
| D (B12d) | Peer utilisation | 100 | 84% (peer_utilisation 1.0, 4/4 substantive) | 0 / 3 / 2 |
| **Overall** | min of four, red flag bound | **81** | band 75-89 normal | REWORK not triggered |

No verifier logged a CRITICAL and no acceptance rate fell below 60%, so REWORK is not triggered. The binding component is Verifier B at 81; its missed and under weighted items both bear on profitability quality.

---

## Findings, sorted by severity

### CRITICAL
None.

### MAJOR

| Verifier | Location anchor | Finding |
|---|---|---|
| B (B12b) | B05 4D / red_flags, Q3 FY26 profitability | Q3 maiden PAT (₹2.71 Cr) is driven by ₹9.72 Cr non operating other income (HelloWorld IndAS lease liability reversal, Jan call p.7-8); ex other income the quarter is an operating loss. B05 attached its one time framing to the Q4 ₹17.72 Cr building gain (which was excluded from reported profit) rather than to the reversal that produced the reported PAT milestone. Under weighted / misclassified. |
| B (B12b) | B05 / B06 omission | Integrow subsidiary to associate deconsolidation (1-Jul-2025, control "in abeyance") removes a lossmaker from line by line consolidation and flatters profitability; the Capital/SM-REIT segment contracted FY25 ₹15.94 Cr to FY26 ₹7.84 Cr while promoted as optionality. Absent from both reports; profit flattering plus contracting optionality is thesis relevant. |
| D (B12d) | B06 peer_coverage_map ZAGGLE baseline row | Coverage map credits the Nov-2024 baseline transcript for the "16% at IPO" cross sell figure; the 16/20/21% points actually come from the Nov-2025 Q2 FY26 call (correctly credited elsewhere in the same table). Attribution error, not fabrication; no verdict changes. |
| D (B12d) | 06-peers.md Claim 9 | RATEGAIN Sojern $12M cost savings stated as "within 100 days"; transcript says "first 90 days" twice. Figure otherwise accurate. |
| D (B12d) | 06-peers.md Part 2E / risks_peers_raise | ZAGGLE OCF flag conflates a YoY delta (~₹33 Cr) with a later absolute reading; the actual May-2026 data point shows OCF improving to -₹6 Cr, reversing the implied deterioration. Underlying point (ZAGGLE OCF scrutiny vs Aurum silence) stands. |

### MINOR

| Verifier | Location anchor | Finding |
|---|---|---|
| A (B12a) | 01-gate0.md, Block B row B2 (Capex FY24-FY26) | FY24 capex ₹104.45 Cr / FY25 ₹19.38 Cr / FY26 ₹15.85 Cr not rendered in accessible text; cited from AR FY25 p.215 and Q4 FY26 PDF p.17. Gate 0 discloses the boundary (FY22-23 marked N/A); plausibility verified against the ₹155.13 Cr investing outflow. Data limitation, not analysis error. |
| A (B12a) | 01-gate0.md, Block D one time item caveat | FY26 building sale gain ~₹17.72 Cr note 5 anchor not verifiable in rendered results PDF text; Q4 other income is ₹21.22 Cr in screener and ₹17.72 Cr is a consistent component. Gate 0 uses it only to caveat D1/D2 and shows both ex gain ratios; methodology sound, specific anchor textually unverified. |
| B (B12b) | B05 2A#6 / timeline_slippages, PropTiger | The promised PropTiger turnaround is framed on removing REA related party charges (royalty, marketing fee, business support; Jul call p.9); the related party cost basis of the margin promise is not weighted. |
| B (B12b) | B05 2E repeated question tracker | Synergy/AI benefit quantification dodge recurs Q3 (Jimit p.18, Dipesh p.21) and Q4 (Jimit p.15-16, Dipesh p.18); B05 declined to log it as repeated. Not CRITICAL as the ecosystem revenue evasion is documented. |
| B (B12b) | B05 3A REA/Housing.com | Ongoing related party lead purchase contract with REA owned Housing.com (REA also 5.5% holder; Q2 call p.17) presented only as a positive, not flagged as a related party dependency. |
| C (B12c) | B01 YAML history_downgrade / report Data-window | history_downgrade=true set outside the 3-4yr LIMITED band; field repurposed as a qualitative caveat, no tier downgrade applied. AVOID is the Core<40 floor, so zero decision impact. |
| C (B12c) | B01 Block B, B3 | cum FCF/PAT 0.33 scored 1 on a ratio positive only because both FCF and PAT are negative; literal band application, flagged by maker. B3=0 would give Core 35, still AVOID. |
| C (B12c) | B07 scorecard row 6 (B2) vs Section 3 summary | Summary labels B2 evidence 📄 but scorecard applies the 🎙️ 0.7 multiplier; runs in the conservative (understating) direction. Would add +0.3 if corrected; band unchanged. |
| C (B12c) | B07 scorecard row 21 (R1) / classification | em_score 25.2 sits 0.2 above the 25.0 STRENGTHENING/MODEST boundary; R1 raw HH=4 is generous vs the report's own "wait and watch, ~2% loss making segment" narrative. R1 at HM(3) gives 24.2 to MODEST. Discretionary judgment, surfaced not rescored; potential band flip. |
| D (B12d) | 06-peers.md Claim 6 | CARTRADE CarDekho deal described as "declining"; management said "put it on hold". Directionally consistent. |
| D (B12d) | 06-peers.md Part 3 | "WCC4" vs "WCC 4" cosmetic spacing. |
