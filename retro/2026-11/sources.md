# Sources: results census 2026-11 (cloud session)

Run date: 2026-11-16. Where it ran: a cloud container, not a laptop. Branch name uses `cloud` in place of a laptop name.

## Counts

| source | count |
|---|---|
| Remote branches fetched (tip of each) | 315 |
| of which `run/*` | 58 |
| of which `claude/*` | 229 |
| of which other prefixes (companies 1, feat 1, framework 8, handover 1, job 1, main 1, maint 2, retire-quarterly-review-skill 1, screens 2, tools 5, video 3, wip 2) | 28 |
| Run folders found across all branches | 306 |
| of which on main | 106 |
| of which on other branches only | 200 |
| of which quarterly folders (-q4fy26, -q1fy27, -q2fy27, -h1fy27, -q2cy26) | 154 |
| Company memory files (`companies/<TICKER>.md`) found | 117 |
| of which on main | 43 |
| Versions of `LESSONS_ARCHIVE.md` across branches | 85 |
| Report files read from run folders | 3486 (70 MB of text) |
| Companies in the census | 242 |
| Census rows | 726 |
| Claude Code sessions read (source B) | 0 |
| Local files read (source C) | 0 |

## How source A was read

- `git fetch` of every branch tip, without file contents. Files were then read with `git cat-file` on the blob that `origin/<branch>:<path>` names. No run folder was checked out.
- Per run folder, the version read is the one with the most non-input files; main wins a tie. `census.csv` names the branch per folder in `run_folders`.
- Read per run folder: `manifest.yaml`, `outputs/final/*`, valuation (stage 10, 11), thesis (14), devil's advocate (15), synthesis (13), concall analysis (05), verifier C, the Halt 1 dossier, the step 1 brief, and for quarterly folders the merged review, the adversary audit, the A4 and A5 blocks, the operator brief and the Notion payload.
- Not read: `inputs/` (source PDFs), raw extracted corpus text, stage reports 01 to 04 and 06 to 09, verifier A, B and D reports, ledgers, forensics files, superseded loop drafts, and any file over 260 KB.
- `LESSONS_ARCHIVE.md`: the main version, plus every line that exists on another branch and not on main.
- Extraction ran in 35 batches under the rules in `extraction_rules.md`. Each batch wrote its rows and one excerpts file per company. The rows were merged by script.

## Sources B and C

- B: no laptop was connected to this session. `extract_sessions.py` and `aliases.json` are in this folder. On a laptop, from the repo root:

```bash
python retro/2026-11/extract_sessions.py
```

  It reads `%USERPROFILE%\.claude\projects\**\*.jsonl`, keeps user and assistant text only, and writes `retro/2026-11/session_excerpts/<TICKER>.md`, `sessions.csv` and `summary.txt`. It sends nothing anywhere.
- C: the Quarterly Reviewer output folder and `C:\ConcallPipeline\Daily Concall Intelligence` were searched for in the container. Neither exists there.

## Every `run/*` branch

| branch | last commit date |
|---|---|
| run/accord-2026-10-06 | 2026-10-06 |
| run/anawil-2026-11-12 | 2026-11-15 |
| run/astramicro-2026-11-15 | 2026-11-16 |
| run/avana-2026-10-05 | 2026-10-05 |
| run/avience-2026-09-26 | 2026-09-26 |
| run/awfis-2026-09-19 | 2026-09-19 |
| run/azad-2026-11-15 | 2026-11-16 |
| run/capillary-2026-09-19 | 2026-10-10 |
| run/cnl-2026-11-11 | 2026-11-11 |
| run/credent-2026-11-12 | 2026-11-12 |
| run/deedev-2026-11-15 | 2026-11-16 |
| run/dpabhushan-2026-09-19 | 2026-09-24 |
| run/emudhra-2026-09-19 | 2026-09-19 |
| run/esconet-2026-10-05 | 2026-10-05 |
| run/fabtech-2026-09-26 | 2026-09-26 |
| run/goodluck-2026-09-19 | 2026-10-13 |
| run/gvpil-2026-11-15 | 2026-11-16 |
| run/iex-2026-09-08 | 2026-09-19 |
| run/indnippon-2026-09-10 | 2026-09-29 |
| run/invprecq-2026-11-15 | 2026-11-16 |
| run/iolcp-2026-09-19 | 2026-10-04 |
| run/jlhl-2026-11-12 | 2026-11-12 |
| run/keltech-2026-11-15 | 2026-11-16 |
| run/kissht-2026-09-19 | 2026-10-04 |
| run/kpl-2026-11-15 | 2026-11-16 |
| run/kross-2026-09-27 | 2026-10-19 |
| run/kusumgar-2026-11-12 | 2026-11-12 |
| run/kwick-2026-10-04 | 2026-10-04 |
| run/mideast-2026-10-25 | 2026-10-25 |
| run/mmp-2026-10-04 | 2026-10-05 |
| run/onwardtec-2026-11-12 | 2026-11-12 |
| run/premexpln-2026-11-15 | 2026-11-16 |
| run/pvrinox-2026-11-12 | 2026-11-12 |
| run/qll-2026-11-15 | 2026-11-16 |
| run/qmsmedi-2026-09-26 | 2026-10-11 |
| run/qualitek-2026-09-26 | 2026-09-26 |
| run/quarterly-q2fy27-2026-10-17 | 2026-10-20 |
| run/quarterly-q2fy27-2026-10-19 | 2026-10-20 |
| run/quarterly-q2fy27-2026-10-28 | 2026-10-29 |
| run/quarterly-q2fy27-2026-10-30 | 2026-10-30 |
| run/rappid-2026-09-19 | 2026-09-19 |
| run/rkforge-2026-11-12 | 2026-11-12 |
| run/shareindia-2026-09-19 | 2026-09-19 |
| run/shawgeltin-2026-11-12 | 2026-11-12 |
| run/southwest-2026-11-09 | 2026-11-10 |
| run/sswl-2026-09-19 | 2026-10-05 |
| run/sudarcolor-2026-11-12 | 2026-11-12 |
| run/supremepwr-2026-10-06 | 2026-10-06 |
| run/susan-2026-09-19 | 2026-09-29 |
| run/taaltech-2026-09-10 | 2026-09-21 |
| run/tdpowersys-2026-11-15 | 2026-11-16 |
| run/titanbio-phase1-2026-09-16 | 2026-10-04 |
| run/tll-2026-09-26 | 2026-09-26 |
| run/totem-fttcp-2026-09-16b | 2026-09-16 |
| run/trualt-2026-09-18 | 2026-10-02 |
| run/vrllog-2026-11-12 | 2026-11-12 |
| run/walchannag-2026-11-12 | 2026-11-12 |
| run/yashhv-2026-09-26 | 2026-10-21 |

## Every `claude/*` branch

| branch | last commit date |
|---|---|
| claude/aartisurf-pipeline-run-3wqmjl | 2026-08-04 |
| claude/aartisurf-pipeline-run-811pku | 2026-08-04 |
| claude/adf-food-quarterly-analysis-b8cygp | 2026-07-30 |
| claude/aequs-step-one-42trpa | 2026-09-05 |
| claude/aeroflex-results-analysis-x9xrqs | 2026-07-29 |
| claude/anoop-engineering-quarterly-8lr5l1 | 2026-08-06 |
| claude/apexeco-pipeline-run-gkdm6t | 2026-07-10 |
| claude/aspara-quarterly-results-7k23p1 | 2026-07-30 |
| claude/aurob-proptech-investor-analysis-cqrz1p | 2026-07-21 |
| claude/australian-india-quarterly-results-wiv2a8 | 2026-08-12 |
| claude/auto-compact-threshold-lcb3a2 | 2026-07-25 |
| claude/availability-check-oyrf2l | 2026-08-04 |
| claude/avana-pipeline-run-jq6rz4 | 2026-07-17 |
| claude/balaji-mines-quarterly-analysis-ygfira | 2026-07-28 |
| claude/baluforge-2026-09-06-runs-ah784w | 2026-09-11 |
| claude/birlacable-pipeline-4rln8o | 2026-08-20 |
| claude/birlanu-quarterly-results-2zbr6l | 2026-08-06 |
| claude/black-rose-quarterly-analysis-a9u9a4 | 2026-07-31 |
| claude/borana-2026-09-07-vpvzja | 2026-09-08 |
| claude/bundan-bank-q1-fy27-lo837s | 2026-07-22 |
| claude/ceigall-runs-2026-09-06-67mi8o | 2026-09-06 |
| claude/cmsinfo-spear-pass-9v2yyz | 2026-08-31 |
| claude/company-analysis-five-firms-48nqeu | 2026-09-07 |
| claude/conference-call-analysis-a2myie | 2026-07-30 |
| claude/cool-euler-1on89m | 2026-07-30 |
| claude/credo-quarterly-analysis-r7tbey | 2026-08-11 |
| claude/d-dev-quarterly-analysis-jnyqb1 | 2026-08-05 |
| claude/deccan-gold-concall-analysis-5eyww0 | 2026-08-12 |
| claude/dhanbank-pipeline-run-bi3wv6 | 2026-07-29 |
| claude/digitite-results-analysis-yek08v | 2026-07-28 |
| claude/digvi-quarterly-analysis-o97k0v | 2026-08-12 |
| claude/divgiitts-pipeline-run-9hokoy | 2026-08-30 |
| claude/dssl-pipeline-run-onx7hd | 2026-07-28 |
| claude/e2e-quarterly-analysis-j6j65r | 2026-07-23 |
| claude/ebgng-pipeline-run-e7jis5 | 2026-07-13 |
| claude/ecos-mobility-quarterly-analysis-1gxkan | 2026-08-12 |
| claude/emvdl-quarterly-analysis-1eikkc | 2026-08-11 |
| claude/entero-pipeline-run-ndqp3v | 2026-07-28 |
| claude/exicom-q1-fy27-analysis-0bxvcc | 2026-08-11 |
| claude/extra-light-quarterly-analysis-befw6c | 2026-07-25 |
| claude/fabtech-pipeline-run-2ap5pp | 2026-08-05 |
| claude/fedfina-call-analysis-ggpjgq | 2026-07-22 |
| claude/fedfina-pipeline-run-3mq2uj | 2026-07-16 |
| claude/festive-bardeen-ne846x | 2026-07-11 |
| claude/fincables-pipeline-9mrge1 | 2026-08-12 |
| claude/fluidomat-pipeline-ngoubg | 2026-07-17 |
| claude/fratelli-2026-09-07-71euee | 2026-09-08 |
| claude/g-limited-results-analysis-q4cm3w | 2026-08-06 |
| claude/ganesha-quarterly-analysis-rsgtf3 | 2026-07-30 |
| claude/gargi-quarterly-analysis-11fbsc | 2026-08-01 |
| claude/gaudiumivf-pipeline-tvrgn0 | 2026-07-17 |
| claude/ghv-infra-quarterly-analysis-z6m8wn | 2026-08-11 |
| claude/gmdc-quarterly-analysis-c3vej5 | 2026-07-31 |
| claude/gmg-electronics-analysis-0owflj | 2026-07-31 |
| claude/gmm-pfaudler-quarterly-analysis-55jc3e | 2026-08-06 |
| claude/goldium-q1-fy27-earnings-8csvi8 | 2026-08-11 |
| claude/gsmfoils-pipeline-nc36ie | 2026-07-24 |
| claude/hfca-quarterly-analysis-4a6fod | 2026-07-22 |
| claude/india-mart-quarterly-analysis-nujr2m | 2026-07-22 |
| claude/indiaglyco-docreview-run | 2026-09-02 |
| claude/indiaglyco-pipeline-run-nv2zsl | 2026-08-25 |
| claude/indoborax-investment-thesis-curszr | 2026-08-30 |
| claude/inflection-opus-5.5-audit-102xpl | 2026-10-03 |
| claude/jaykay-corpus-extraction-vkjw6a | 2026-08-26 |
| claude/jk-india-quarterly-analysis-xulrvt | 2026-08-12 |
| claude/k-solve-quarterly-analysis-23wdwl | 2026-07-23 |
| claude/kids-game-repair-ylpv03 | 2026-10-14 |
| claude/kronox-lab-sciences-bjc54f | 2026-08-30 |
| claude/laxmi-quarterly-results-nk7iej | 2026-08-12 |
| claude/laxmiindia-pipeline-run-apfp2a | 2026-07-22 |
| claude/macpower-pipeline-g9ouq4 | 2026-07-31 |
| claude/map-my-india-quarterly-analysis-43nbwc | 2026-08-04 |
| claude/mapmyindia-pipeline-run-qj742m | 2026-07-19 |
| claude/max-india-earnings-analysis-2pm9im | 2026-08-12 |
| claude/maxind-pipeline-run-63lhar | 2026-07-24 |
| claude/mcfos-quarterly-analysis-n1t1pq | 2026-08-12 |
| claude/menonbe-pipeline-run-bs4dq5 | 2026-07-17 |
| claude/millworks-pipeline-run-xl204h | 2026-08-22 |
| claude/modisonltd-pipeline-run-e5lytf | 2026-09-09 |
| claude/mtar-annual-reports-qo0c39 | 2026-07-30 |
| claude/nephro-plus-quarterly-analysis-vqj5xc | 2026-08-12 |
| claude/netweb-results-analysis-qb5mas | 2026-07-30 |
| claude/nrail-pipeline-run-k3gtja | 2026-07-23 |
| claude/orchpharma-2026-09-06-runs-bx6lcr | 2026-09-28 |
| claude/oswal-pumps-q1-analysis-si2lg8 | 2026-08-11 |
| claude/paushak-quarterly-analysis-1lg8ur | 2026-07-31 |
| claude/pi-value-annual-report-4pq7qr | 2026-07-27 |
| claude/pipeline-526717-n61a68 | 2026-07-16 |
| claude/pipeline-544332-upvab5 | 2026-08-04 |
| claude/pipeline-544516-8t948a | 2026-07-16 |
| claude/pipeline-544555-o9qto2 | 2026-07-30 |
| claude/pipeline-run-aequs-171qf0 | 2026-09-05 |
| claude/pipeline-run-kabraextru-t0dwrv | 2026-09-09 |
| claude/pipeline-run-pittieng-1u15zn | 2026-09-08 |
| claude/pipeline-run-shharich-q9d0gj | 2026-09-09 |
| claude/pipeline-run-visakaind-41w19l | 2026-09-05 |
| claude/presentation-analysis-3onxgk | 2026-09-07 |
| claude/presentation-analysis-hw7bol | 2026-09-07 |
| claude/qpower-q1-fy27-notion-6lgxlt | 2026-08-11 |
| claude/qr-aequs-q2fy27-f2613d | 2026-10-29 |
| claude/qr-dycl-q2fy27-766ddd | 2026-10-29 |
| claude/qr-indiamart-q2fy27-acb6b5 | 2026-10-28 |
| claude/qr-knack-q2fy27-0febb1 | 2026-10-29 |
| claude/qr-lt-q2fy27-6d55c1 | 2026-10-29 |
| claude/qr-neochem-q2fy27-76041a | 2026-10-29 |
| claude/qr-netweb-q2fy27-a60c5c | 2026-10-29 |
| claude/qr-paracables-q2fy27-a220cd | 2026-10-29 |
| claude/qr-puretrop-q2fy27-888061 | 2026-10-29 |
| claude/qr-raymondrel-q2fy27-f76d61 | 2026-10-28 |
| claude/qr-route-q2fy27-fb3514 | 2026-10-29 |
| claude/qr-skygold-q2fy27-7e1298 | 2026-10-29 |
| claude/qr-sonacoms-q2fy27-c7173c | 2026-10-29 |
| claude/qr-syngene-q2fy27-f49780 | 2026-10-28 |
| claude/qr-unimech-q2fy27-1b1895 | 2026-10-29 |
| claude/qr-wework-q2fy27-97d635 | 2026-10-29 |
| claude/quarterly-ador-q2fy27-97aedb | 2026-10-24 |
| claude/quarterly-ador-q2fy27-fcdfe8 | 2026-10-22 |
| claude/quarterly-analysis-agent-z2p3ps | 2026-07-21 |
| claude/quarterly-ayefin-q2fy27-982ab0 | 2026-10-23 |
| claude/quarterly-credit-care-analysis-pjrg9x | 2026-07-31 |
| claude/quarterly-cybertech-q2fy27-0cb6fb | 2026-10-23 |
| claude/quarterly-cybertech-q2fy27-7a30de | 2026-10-22 |
| claude/quarterly-cybertech-q2fy27-920b89 | 2026-10-24 |
| claude/quarterly-data-pattern-analysis-7vzvt2 | 2026-07-31 |
| claude/quarterly-fairchem-q2fy27-061624 | 2026-10-22 |
| claude/quarterly-fairchem-q2fy27-72a096 | 2026-10-22 |
| claude/quarterly-fairchem-q2fy27-83430a | 2026-10-23 |
| claude/quarterly-fairchem-q2fy27-bcfbf0 | 2026-10-24 |
| claude/quarterly-gallantt-call-q2fy27-7b3ed0 | 2026-10-23 |
| claude/quarterly-gallantt-q2fy27-3b5cf9 | 2026-10-22 |
| claude/quarterly-gallantt-q2fy27-3e941e | 2026-10-22 |
| claude/quarterly-gallantt-q2fy27-e09215 | 2026-10-23 |
| claude/quarterly-garware-q2fy27-1ec041 | 2026-10-23 |
| claude/quarterly-ghv-q2fy27-3cf5aa | 2026-10-23 |
| claude/quarterly-indosolar-q2fy27-2614ff | 2026-10-23 |
| claude/quarterly-indosolar-q2fy27-94b089 | 2026-10-22 |
| claude/quarterly-indosolar-q2fy27-9e8245 | 2026-10-23 |
| claude/quarterly-paisalo-q2fy27-095262 | 2026-10-23 |
| claude/quarterly-pittieng-q2fy27-3ad60d | 2026-10-22 |
| claude/quarterly-pittieng-q2fy27-3fc1e6 | 2026-10-24 |
| claude/quarterly-pittieng-q2fy27-53e90d | 2026-10-22 |
| claude/quarterly-results-analysis-01wssj | 2026-08-12 |
| claude/quarterly-results-analysis-06y8qn | 2026-07-27 |
| claude/quarterly-results-analysis-0ffwkb | 2026-08-12 |
| claude/quarterly-results-analysis-324riy | 2026-08-13 |
| claude/quarterly-results-analysis-3y7lxn | 2026-08-13 |
| claude/quarterly-results-analysis-53w4to | 2026-08-12 |
| claude/quarterly-results-analysis-7dqyyn | 2026-08-14 |
| claude/quarterly-results-analysis-91a9t7 | 2026-08-13 |
| claude/quarterly-results-analysis-9ef8ys | 2026-08-06 |
| claude/quarterly-results-analysis-ag4rkl | 2026-08-04 |
| claude/quarterly-results-analysis-b1d9jd | 2026-08-13 |
| claude/quarterly-results-analysis-b66fgh | 2026-08-04 |
| claude/quarterly-results-analysis-bjv3ft | 2026-08-13 |
| claude/quarterly-results-analysis-c8fsiv | 2026-08-14 |
| claude/quarterly-results-analysis-d723ow | 2026-08-13 |
| claude/quarterly-results-analysis-dwprvc | 2026-08-13 |
| claude/quarterly-results-analysis-ffii20 | 2026-08-04 |
| claude/quarterly-results-analysis-h2f1ss | 2026-08-05 |
| claude/quarterly-results-analysis-h4n2ul | 2026-08-06 |
| claude/quarterly-results-analysis-i1ji43 | 2026-08-12 |
| claude/quarterly-results-analysis-ixhbmx | 2026-08-14 |
| claude/quarterly-results-analysis-j2wrxj | 2026-08-05 |
| claude/quarterly-results-analysis-jz50z8 | 2026-08-13 |
| claude/quarterly-results-analysis-lft8iz | 2026-08-13 |
| claude/quarterly-results-analysis-mk45d6 | 2026-08-12 |
| claude/quarterly-results-analysis-o83a25 | 2026-08-06 |
| claude/quarterly-results-analysis-oxt7o0 | 2026-08-13 |
| claude/quarterly-results-analysis-qhuohq | 2026-08-13 |
| claude/quarterly-results-analysis-qj2kqr | 2026-08-04 |
| claude/quarterly-results-analysis-rnbvw5 | 2026-08-13 |
| claude/quarterly-results-analysis-u9lgke | 2026-08-14 |
| claude/quarterly-results-analysis-vx8dc4 | 2026-08-06 |
| claude/quarterly-results-protocol-dlltuf | 2026-08-06 |
| claude/quarterly-supremepower-q2fy27-7e9233 | 2026-10-24 |
| claude/quarterly-supremepower-q2fy27-f067e1 | 2026-10-23 |
| claude/quarterly-supremepower-q2fy27-fd3ab0 | 2026-10-22 |
| claude/quarterly-tejas-q2fy27-18d4de | 2026-10-23 |
| claude/quarterly-tejas-q2fy27-a6fb62 | 2026-10-22 |
| claude/quarterly-tejas-q2fy27-f91c3c | 2026-10-24 |
| claude/quarterly-tejas-q2fy27-fb40f4 | 2026-10-22 |
| claude/quarterly-tinna-q2fy27-d4fe1d | 2026-10-23 |
| claude/quarterly-yashhv-q2fy27-642505 | 2026-10-22 |
| claude/ram-ratna-quarterly-analysis-0161le | 2026-07-31 |
| claude/ramrat-pipeline-run-e5xukv | 2026-07-30 |
| claude/rathist-pipeline-ml8nfh | 2026-07-20 |
| claude/raymond-realty-q1-fy27-h5wmo2 | 2026-08-11 |
| claude/red-grain-quarterly-results-1xrd0f | 2026-08-06 |
| claude/route-mobile-quarterly-pkqpxv | 2026-07-25 |
| claude/run-diffnkg-pipeline-8n6qp1 | 2026-09-07 |
| claude/run-jitfinfra-pipeline-iobgub | 2026-08-12 |
| claude/run-pipeline-aye-adnmeu | 2026-07-23 |
| claude/run-pipeline-ddevplstik-405lmq | 2026-07-24 |
| claude/run-pipeline-indgn-6wej1t | 2026-08-06 |
| claude/run-pipeline-mpsltd-nmmtdo | 2026-09-04 |
| claude/runs-cyientdlm-2026-09-06-w70pyd | 2026-09-06 |
| claude/runs-ina-2026-09-06-kav2sw | 2026-09-11 |
| claude/sasken-quarterly-analysis-xgjg0m | 2026-08-04 |
| claude/sedemac-quarterly-analysis-4k2otx | 2026-07-29 |
| claude/sesha-sai-analysis-t7sqgg | 2026-07-25 |
| claude/sfl-pipeline-run-lya9nj | 2026-07-14 |
| claude/sheela-quarterly-results-zxbbvj | 2026-08-04 |
| claude/shriram-properties-quarterly-8swem6 | 2026-08-12 |
| claude/shyammetl-pipeline-run-x08gtb | 2026-07-19 |
| claude/sicallog-pipeline-pwftth | 2026-07-29 |
| claude/southrest-quarterly-results-wo3ltt | 2026-07-22 |
| claude/sp-apparel-quarterly-analysis-q2eld6 | 2026-08-11 |
| claude/spear-override-2026-09-02-oecn2r | 2026-09-04 |
| claude/spra-quarterly-results-analysis-ctlfwb | 2026-08-06 |
| claude/sugs-lyod-results-analysis-sa8wi5 | 2026-07-29 |
| claude/sweet-gates-5ozcc6 | 2026-10-04 |
| claude/tata-power-analysis-2x2wx8 | 2026-07-27 |
| claude/tatva-pipeline-run-kl58kw | 2026-07-21 |
| claude/tejas-network-quarterly-analysis-4mzxz3 | 2026-07-28 |
| claude/token-consumption-analysis-6tl0ko | 2026-08-03 |
| claude/token-consumption-spike-f1tz7x | 2026-07-29 |
| claude/transcript-indigene-analysis-5zmus0 | 2026-08-17 |
| claude/transrail-quarterly-analysis-f7kqqf | 2026-08-06 |
| claude/truevault-quarterly-analysis-27abp5 | 2026-07-29 |
| claude/trusting-einstein-qap7vj | 2026-09-15 |
| claude/unipart-quarterly-analysis-5ky0ug | 2026-08-11 |
| claude/united-food-investor-analysis-fdzhmr | 2026-08-18 |
| claude/urban-company-quarterly-analysis-ib51ci | 2026-08-01 |
| claude/venus-pipes-q1-fy27-jtc505 | 2026-08-11 |
| claude/vilas-equity-research-tuuvfi | 2026-09-03 |
| claude/voepl-pipeline-run-ppnypi | 2026-07-18 |
| claude/yasho-industries-step-one-iuo5ii | 2026-09-05 |
| claude/zealous-sagan-i3nyzq | 2026-11-13 |
| claude/zeel-quarterly-analysis-9i2r1v | 2026-08-11 |

## Other branches

companies/taaltech-integrity-pending, feat/shallow-agents, framework/ar-section-index, framework/downstream-guardrail-2026-10-19, framework/master-fttcp-stop-conflict, framework/oct-11-housekeeping, framework/oct-2026-open-rulings, framework/or-14-promoter-concern, framework/project-instructions-v4-1, framework/verticals-guardrail-2026-10-20, handover/2026-10-29, job/brief-2026-10-11-2026-10-11, main, maint/oct-2026-corpus-and-or14, maint/post-kwick-run-fixes, retire-quarterly-review-skill, screens/shallow-2026-10-26, screens/shallow-2026-10-27, tools/chartink-push-main, tools/liquidity-smallcap, tools/macro-direction, tools/macro-regime, tools/macro-regime-metals, video/capillary-2026-10-11, video/capillary-bd06, video/mideast-2026-10-25, wip/gate0-prompt-edit-2026-10-04, wip/laptop-save-2026-10-04

