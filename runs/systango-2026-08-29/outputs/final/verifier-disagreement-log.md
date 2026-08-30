# Verifier Disagreement Log — SYSTANGO

One row per point where a downstream step's conclusion conflicted with a Verifier A source-fidelity finding.

| Date | Run | Number / claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-08-29 | SYSTANGO-2026-08-29 | DBX Holdings (Rs 166.11 L) and GreenLeaf TDG (Rs 35.88 L) equity stakes: present in AR Note 8 or not | MISMATCH / source-fidelity: both unquoted equity instruments ARE listed in Consolidated Note 8, p.112, Section B (B12a, MAJOR, source_fidelity: true) | Stage 7 (07-emoat) said "DBX Holdings and GreenLeaf NOT FOUND in AR Note 8" and "GreenLeaf NOT FOUND anywhere in the AR"; Stage 3 (03-ardeep) read them present at Note 8 p.112 | GATE HELD — corrected at source. Stage 3's Rs 166.11 L DBX / Rs 35.88 L GreenLeaf figures stand; Stage 7's NOT FOUND removed. Non-overridable; only the source PDF can clear it, and it confirms Stage 3. Re-checked by Verifier A (B12a). | No verdict-card figure carried the flagged NOT FOUND. The corrected stakes feed FLAG-PROMOTER (DBX customer-to-equity conversion) and the optionality register. Not a fabrication in a verdict input, so not a forced REWORK. |
