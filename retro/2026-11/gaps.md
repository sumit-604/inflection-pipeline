# Gaps: results census 2026-11 (cloud session)

Facts only. Every list below is generated from `census.csv` and the branch inventory.

## 1. Sources not read

- Source B (Claude Code session history on the laptop): NOT READ. This census ran in a cloud container. No laptop was connected. The container holds only this session's own transcript. Run `extract_sessions.py` on each laptop.
- Source C (Quarterly Reviewer output folder; `C:\ConcallPipeline\Daily Concall Intelligence`): NOT READ. Neither folder exists in the container.
- Notion pages: NOT READ. Where a row cites a Notion thesis, the text is the copy saved inside a run folder.

## 2. Companies with no baseline (186 of 242)

### 2a. No base case of ours in any file (132)

526717, 544516, ADOR, AEROFLEX, AKUMS, ANAWIL, APEXECO, ARIS, ASTRAMICRO, AVIENCE, AWFIS, BALAJITELE, BALUFORGE, BIRLANU, BLACKROSE, BORANA, CEIGALL, CLEANMAX, CNL, CREDENT, CREDO, CYBERTECH, CYIENTDLM, DECCANGOLD, DHANBANK, DIFFNKG, DIGITIDE, DPABHUSHAN, DYCL, EIMCOELECO, EMUDHRA, ESCONET, FABCLEAN, FAIRCHEMOR, FEDFINA, FRATELLI, GALLANTT, GEE, GEMAROMA, GHVINFRA, GMBREW, GMDC, GMMPFAUDLER, GOCLCORP, GOLDIAM, GOODLUCK, GRPLTD, HERITGFOOD, IEX, IKS, INA, INDIQUBE, INDNIPPON, INDOBORAX, INDORAMA, INDOSOLAR, INOXINDIA, INVPRECQ, IOLCP, JAYKAY, JLHL, KABRAEXTRU, KARNIKA, KECL, KELTECH, KNACK, KOPRAN, KPL, KRONOX, KUSUMGAR, LT, LTELEVATOR, MCFOS, MILLWORKS, MMP, MODISONLTD, MPSLTD, NEOCHEM, OBSCP, ONWARDTEC, ORCHPHARMA, PACEDIGITK, PARACABLES, PAUSHAK, PITTIENG, POONAWALLA, PREMEXPLN, PREMIERPOL, PRIZOR, PVRINOX, QMSMEDI, QUALITEK, RAPPID, RATEGAIN, RKFORGE, SAMHI, SAMMAANCAP, SEDEMAC, SHAREINDIA, SHARIKA, SHAWGELTIN, SHHARICH, SKYGOLD, SONACOMS, SPROP, SSWL, STALLION, SUDARCOLOR, SUGSLLOYD, SUSAN, TATACOMM, TATAPOWER, TATVA, TDPOWERSYS, TINNARUBR, TIPCO, TITANBIO, TLL, UNIABEX, UNIPARTS, VAIBHAVGBL, VILAS, VISAKAIND, VIVIDEL, VOEPL, VRLLOG, WALCHANNAG, WEWORK, WORKMATES, YASHHV, YASHO, ZEEL

### 2b. A base case exists but no period is comparable (54)

The base starts at a later year, was written after the result, or is a full-year number against a part-year result. See `comparison_note` in the census.

AARTISURF, ACCORD, AIMTRON, AMEENJI, ATLANTAELEC, AVANA, AZAD, BIRLACABLE, CAPILLARY, CMSINFO, DATAPATTNS, DDEVPLSTIK, DIVGIITTS, DSSL, ENTERO, FABTECH, FINCABLES, FINKURVE, FLUIDOMAT, GANECOS, GAUDIUMIVF, GSMFOILS, INDIAGLYCO, JITFINFRA, JUBLCPL, KISSHT, KWICK, LAXMIINDIA, MACPOWER, MANINDS, MAPMYINDIA, MAXIND, MENONBE, MTAR, NORTHARC, NRAIL, PERMAGNET, PURETROP, RAMRAT, RATHIST, SHYAMMETL, SICALLOG, SMRUTHI, STYL, SUPREMEPWR, SYSTANGO, TAALTECH, TOTEM, TRUALT, UFBL, VENUSREM, VINYAS, WELCORP, ZAGGLE

## 3. Companies with no actuals

### 3a. No reported number in any of the three periods (2)

KOPRAN, TIPCO

### 3b. No actuals for Q4FY26 (5)

DECCANGOLD, GOLDIAM, KOPRAN, TIPCO, VRLLOG

### 3b. No actuals for Q1FY27 (36)

ACCORD, AIMTRON, AKUMS, AMEENJI, ANAWIL, APEXECO, AVANA, AVIENCE, BALUFORGE, CREDENT, DDEVPLSTIK, FLUIDOMAT, JITFINFRA, KABRAEXTRU, KOPRAN, KWICK, LTELEVATOR, MILLWORKS, NEOCHEM, NORTHARC, NRAIL, OBSCP, PRIZOR, QUALITEK, SHYAMMETL, SICALLOG, SMRUTHI, SYSTANGO, TIPCO, VILAS, VINYAS, VIVIDEL, VOEPL, WORKMATES, YASHHV, ZAGGLE

### 3b. No actuals for Q2FY27 (175)

526717, 544516, AARTISURF, ADFFOODS, AEROFLEX, AIMTRON, AKUMS, AMAGI, AMEENJI, ANUP, APEXECO, ARIS, ASIANENE, ATLANTAELEC, AVANA, AVIENCE, AWFIS, BALAJITELE, BALAMINES, BALUFORGE, BANDHAN, BIRLACABLE, BIRLANU, BLACKROSE, BORANA, CAPILLARY, CEIGALL, CLEANMAX, CMSINFO, CREDO, DATAPATTNS, DDEVPLSTIK, DECCANGOLD, DHANBANK, DIFFNKG, DIGITIDE, DIVGIITTS, DPABHUSHAN, DSSL, E2ENETWORKS, EBGNG, ECOSMOBLTY, EMUDHRA, EMVDL, ENTERO, ESCONET, EXICOM, FABCLEAN, FABTECH, FINCABLES, FINKURVE, FLUIDOMAT, FRATELLI, GANECOS, GARGI, GAUDIUMIVF, GEE, GEMAROMA, GMDC, GMMPFAUDLER, GOLDIAM, GOODLUCK, GRPLTD, GSMFOILS, IEX, IKS, INA, INDGN, INDIAGLYCO, INDIQUBE, INDNIPPON, INDOBORAX, INOXINDIA, IOLCP, IPCL, IVALUE, JAYKAY, JITFINFRA, JNKINDIA, JUBLCPL, KABRAEXTRU, KCPSUGIND, KECL, KERNEX, KISSHT, KOPRAN, KRN, KRONOX, KSOLVES, KWICK, LAXMIINDIA, LTELEVATOR, MACPOWER, MANINDS, MAPMYINDIA, MAXIND, MCFOS, MENONBE, MILLWORKS, MMP, MODISONLTD, MPSLTD, MTAR, NEPHROPLUS, NORTHARC, NRAIL, OBSCP, ORCHPHARMA, OSWAL, PACEDIGITK, PARKHOSPS, PAUSHAK, PERMAGNET, PNGSREVA, PRIZOR, QMSMEDI, QPOWER, RAMRAT, RAPPID, RATEGAIN, RATHIST, RPTECH, RSYSTEMS, SAMBHV, SAMHI, SAMMAANCAP, SASKEN, SATIN, SCODATUBES, SEDEMAC, SFL, SHAREINDIA, SHARIKA, SHAWGELTIN, SHHARICH, SHYAMMETL, SICALLOG, SMRUTHI, SPAPPAREL, SPROP, SRM, SSWL, STALLION, STLTECH, STYL, SUGSLLOYD, SUSAN, SYSTANGO, TAALTECH, TATAPOWER, TIPCO, TITANBIO, TLL, TOTEM, TRANSRAIL, TRUALT, UFBL, UNIABEX, UNIPARTS, URBANCO, UTLSOLAR, VAIBHAVGBL, VENUSPIPES, VENUSREM, VILAS, VINYAS, VISAKAIND, VIVIDEL, VOEPL, WELCORP, WORKMATES, YASHHV, YASHO, ZAGGLE, ZEEL

## 4. Companies whose files sit on one branch only (124)

Every run folder and the company file of these names exist on exactly one branch.

| ticker | branch |
|---|---|
| ACCORD | origin/run/accord-2026-10-06 |
| ADFFOODS | origin/claude/adf-food-quarterly-analysis-b8cygp |
| ADOR | origin/claude/quarterly-ador-q2fy27-97aedb |
| AEROFLEX | origin/claude/aeroflex-results-analysis-x9xrqs |
| ANAWIL | origin/run/anawil-2026-11-12 |
| ANUP | origin/claude/anoop-engineering-quarterly-8lr5l1 |
| ARIS | origin/claude/spra-quarterly-results-analysis-ctlfwb |
| ASTRAMICRO | origin/run/astramicro-2026-11-15 |
| AVIENCE | origin/run/avience-2026-09-26 |
| AWFIS | origin/run/awfis-2026-09-19 |
| BALAJITELE | origin/claude/trusting-einstein-qap7vj |
| BALAMINES | origin/claude/balaji-mines-quarterly-analysis-ygfira |
| BANDHAN | origin/claude/bundan-bank-q1-fy27-lo837s |
| BIRLANU | origin/claude/birlanu-quarterly-results-2zbr6l |
| BLACKROSE | origin/claude/black-rose-quarterly-analysis-a9u9a4 |
| CNL | origin/run/cnl-2026-11-11 |
| CREDENT | origin/run/credent-2026-11-12 |
| CREDO | origin/claude/credo-quarterly-analysis-r7tbey |
| DATAPATTNS | origin/claude/quarterly-data-pattern-analysis-7vzvt2 |
| DECCANGOLD | origin/claude/deccan-gold-concall-analysis-5eyww0 |
| DEEDEV | origin/claude/d-dev-quarterly-analysis-jnyqb1, origin/run/deedev-2026-11-15 |
| DIGITIDE | origin/claude/digitite-results-analysis-yek08v |
| E2ENETWORKS | origin/claude/e2e-quarterly-analysis-j6j65r |
| ECOSMOBLTY | origin/claude/ecos-mobility-quarterly-analysis-1gxkan |
| EIMCOELECO | origin/run/quarterly-q2fy27-2026-10-17 |
| EMVDL | origin/claude/emvdl-quarterly-analysis-1eikkc |
| ESCONET | origin/run/esconet-2026-10-05 |
| EXICOM | origin/claude/exicom-q1-fy27-analysis-0bxvcc |
| FINKURVE | origin/claude/quarterly-results-analysis-bjv3ft |
| GARGI | origin/claude/gargi-quarterly-analysis-11fbsc |
| GEE | origin/claude/g-limited-results-analysis-q4cm3w |
| GEMAROMA | origin/claude/quarterly-results-analysis-jz50z8 |
| GHVINFRA | origin/claude/ghv-infra-quarterly-analysis-z6m8wn, origin/claude/quarterly-ghv-q2fy27-3cf5aa |
| GMBREW | origin/run/quarterly-q2fy27-2026-10-17 |
| GMDC | origin/claude/gmdc-quarterly-analysis-c3vej5 |
| GMMPFAUDLER | origin/claude/gmm-pfaudler-quarterly-analysis-55jc3e |
| GOCLCORP | origin/claude/quarterly-results-analysis-d723ow, origin/run/quarterly-q2fy27-2026-10-19 |
| GOLDIAM | origin/claude/goldium-q1-fy27-earnings-8csvi8 |
| GOODLUCK | origin/run/goodluck-2026-09-19 |
| GRPLTD | origin/claude/trusting-einstein-qap7vj |
| GRWRHITECH | origin/claude/quarterly-garware-q2fy27-1ec041 |
| GVPIL | origin/claude/quarterly-results-analysis-qhuohq, origin/run/gvpil-2026-11-15 |
| HERITGFOOD | origin/run/quarterly-q2fy27-2026-10-17 |
| IEX | origin/run/iex-2026-09-08 |
| INDIQUBE | origin/claude/quarterly-results-analysis-i1ji43 |
| INDORAMA | origin/run/quarterly-q2fy27-2026-10-17 |
| INDOSOLAR | origin/claude/quarterly-indosolar-q2fy27-2614ff |
| INVPRECQ | origin/run/invprecq-2026-11-15 |
| IOLCP | origin/run/iolcp-2026-09-19 |
| IPCL | origin/claude/quarterly-results-analysis-dwprvc |
| IVALUE | origin/claude/aspara-quarterly-results-7k23p1 |
| JAYKAY | origin/claude/jaykay-corpus-extraction-vkjw6a |
| JLHL | origin/run/jlhl-2026-11-12 |
| JNKINDIA | origin/claude/jk-india-quarterly-analysis-xulrvt |
| KELTECH | origin/run/keltech-2026-11-15 |
| KERNEX | origin/claude/quarterly-results-analysis-ixhbmx |
| KPL | origin/run/kpl-2026-11-15 |
| KRN | origin/claude/quarterly-results-analysis-0ffwkb |
| KROSS | origin/run/kross-2026-09-27, origin/run/quarterly-q2fy27-2026-10-19 |
| KSOLVES | origin/claude/k-solve-quarterly-analysis-23wdwl |
| KUSUMGAR | origin/run/kusumgar-2026-11-12 |
| KWICK | origin/run/kwick-2026-10-04 |
| LTELEVATOR | origin/wip/laptop-save-2026-10-04 |
| MCFOS | origin/claude/mcfos-quarterly-analysis-n1t1pq |
| MMP | origin/run/mmp-2026-10-04 |
| MTAR | origin/claude/mtar-annual-reports-qo0c39 |
| NEPHROPLUS | origin/claude/nephro-plus-quarterly-analysis-vqj5xc |
| ONWARDTEC | origin/run/onwardtec-2026-11-12 |
| OSWAL | origin/claude/oswal-pumps-q1-analysis-si2lg8 |
| PACEDIGITK | origin/claude/quarterly-results-analysis-vx8dc4 |
| PAISALO | origin/claude/quarterly-paisalo-q2fy27-095262, origin/claude/quarterly-results-protocol-dlltuf |
| PAUSHAK | origin/claude/paushak-quarterly-analysis-1lg8ur |
| PNGSREVA | origin/claude/cool-euler-1on89m |
| POONAWALLA | origin/run/quarterly-q2fy27-2026-10-17 |
| PREMEXPLN | origin/run/premexpln-2026-11-15 |
| PREMIERPOL | origin/run/quarterly-q2fy27-2026-10-17 |
| PVRINOX | origin/run/pvrinox-2026-11-12 |
| QMSMEDI | origin/run/qmsmedi-2026-09-26 |
| QPOWER | origin/claude/qpower-q1-fy27-notion-6lgxlt, origin/run/quarterly-q2fy27-2026-10-19 |
| QUALITEK | origin/run/qll-2026-11-15, origin/run/qualitek-2026-09-26 |
| RAPPID | origin/run/rappid-2026-09-19 |
| RATEGAIN | origin/claude/red-grain-quarterly-results-1xrd0f |
| RKFORGE | origin/run/rkforge-2026-11-12 |
| ROUTE | origin/claude/qr-route-q2fy27-fb3514, origin/claude/route-mobile-quarterly-pkqpxv |
| RSYSTEMS | origin/claude/quarterly-results-analysis-j2wrxj |
| SAMMAANCAP | origin/claude/quarterly-results-analysis-b1d9jd |
| SASKEN | origin/claude/sasken-quarterly-analysis-xgjg0m |
| SATIN | origin/claude/quarterly-credit-care-analysis-pjrg9x |
| SCODATUBES | origin/claude/quarterly-results-analysis-91a9t7 |
| SEDEMAC | origin/claude/sedemac-quarterly-analysis-4k2otx |
| SHAREINDIA | origin/run/shareindia-2026-09-19 |
| SHARIKA | origin/claude/quarterly-results-analysis-01wssj |
| SHAWGELTIN | origin/run/shawgeltin-2026-11-12 |
| SOUTHWEST | origin/claude/southrest-quarterly-results-wo3ltt, origin/run/southwest-2026-11-09 |
| SPAPPAREL | origin/claude/sp-apparel-quarterly-analysis-q2eld6 |
| SPROP | origin/claude/shriram-properties-quarterly-8swem6 |
| SRM | origin/claude/quarterly-results-analysis-u9lgke |
| SSWL | origin/run/sswl-2026-09-19 |
| STALLION | origin/claude/australian-india-quarterly-results-wiv2a8 |
| STYL | origin/claude/sesha-sai-analysis-t7sqgg |
| SUDARCOLOR | origin/run/sudarcolor-2026-11-12 |
| SUGSLLOYD | origin/claude/sugs-lyod-results-analysis-sa8wi5 |
| SUSAN | origin/run/susan-2026-09-19 |
| TATACOMM | origin/run/quarterly-q2fy27-2026-10-17 |
| TATAPOWER | origin/claude/tata-power-analysis-2x2wx8 |
| TDPOWERSYS | origin/run/tdpowersys-2026-11-15 |
| TEJASNET | origin/claude/quarterly-tejas-q2fy27-f91c3c, origin/claude/tejas-network-quarterly-analysis-4mzxz3 |
| TINNARUBR | origin/claude/quarterly-tinna-q2fy27-d4fe1d |
| TLL | origin/run/tll-2026-09-26 |
| TRANSRAIL | origin/claude/transrail-quarterly-analysis-f7kqqf |
| TRUALT | origin/claude/truevault-quarterly-analysis-27abp5, origin/run/trualt-2026-09-18 |
| UNIABEX | origin/claude/unipart-quarterly-analysis-5ky0ug |
| UNIPARTS | origin/claude/quarterly-results-analysis-9ef8ys |
| URBANCO | origin/claude/urban-company-quarterly-analysis-ib51ci |
| UTLSOLAR | origin/claude/quarterly-results-analysis-324riy |
| VAIBHAVGBL | origin/claude/quarterly-results-analysis-h2f1ss |
| VENUSPIPES | origin/claude/venus-pipes-q1-fy27-jtc505 |
| VIVIDEL | origin/claude/presentation-analysis-hw7bol |
| VRLLOG | origin/run/vrllog-2026-11-12 |
| WALCHANNAG | origin/run/walchannag-2026-11-12 |
| WELCORP | origin/claude/quarterly-results-analysis-06y8qn |
| WORKMATES | origin/claude/presentation-analysis-3onxgk |
| YASHHV | origin/run/yashhv-2026-09-26 |
| ZEEL | origin/claude/zeel-quarterly-analysis-9i2r1v |

## 5. Run folders not on main (200 of 306)

| run folder | branches holding it | branch read |
|---|---|---|
| runs/526717-q1fy27 | 1 | origin/claude/quarterly-results-analysis-53w4to |
| runs/530077-q2fy27 | 2 | origin/claude/qr-puretrop-q2fy27-888061 |
| runs/accord-2026-10-06 | 1 | origin/run/accord-2026-10-06 |
| runs/adffoods-q1fy27 | 1 | origin/claude/adf-food-quarterly-analysis-b8cygp |
| runs/ador-q2fy27 | 1 | origin/claude/quarterly-ador-q2fy27-97aedb |
| runs/aequs-q2fy27 | 10 | origin/claude/qr-dycl-q2fy27-766ddd |
| runs/aeroflex-q1fy27 | 1 | origin/claude/aeroflex-results-analysis-x9xrqs |
| runs/amagi-q1fy27 | 1 | origin/claude/quarterly-results-analysis-rnbvw5 |
| runs/anawil-2026-11-12 | 1 | origin/run/anawil-2026-11-12 |
| runs/anup-q1fy27 | 1 | origin/claude/anoop-engineering-quarterly-8lr5l1 |
| runs/aris-q1fy27 | 1 | origin/claude/spra-quarterly-results-analysis-ctlfwb |
| runs/asianene-q1fy27 | 1 | origin/claude/quarterly-results-analysis-c8fsiv |
| runs/astramicro-2026-11-15 | 1 | origin/run/astramicro-2026-11-15 |
| runs/aurum-q1fy27 | 1 | origin/claude/aurob-proptech-investor-analysis-cqrz1p |
| runs/aurum-q2fy27 | 1 | origin/run/quarterly-q2fy27-2026-10-17 |
| runs/avana-2026-10-05 | 1 | origin/run/avana-2026-10-05 |
| runs/avience-2026-09-26 | 1 | origin/run/avience-2026-09-26 |
| runs/awfis-2026-09-19 | 1 | origin/run/awfis-2026-09-19 |
| runs/aye-q1fy27 | 2 | origin/claude/run-pipeline-aye-adnmeu |
| runs/aye-q2fy27 | 1 | origin/claude/quarterly-ayefin-q2fy27-982ab0 |
| runs/azad-2026-11-15 | 1 | origin/run/azad-2026-11-15 |
| runs/balajitele-2026-09-15 | 1 | origin/claude/trusting-einstein-qap7vj |
| runs/balamines-q1fy27 | 1 | origin/claude/balaji-mines-quarterly-analysis-ygfira |
| runs/bandhan-q1fy27 | 1 | origin/claude/bundan-bank-q1-fy27-lo837s |
| runs/birlanu-q1fy27 | 1 | origin/claude/birlanu-quarterly-results-2zbr6l |
| runs/blackrose-q1fy27 | 1 | origin/claude/black-rose-quarterly-analysis-a9u9a4 |
| runs/cnl-2026-11-11 | 1 | origin/run/cnl-2026-11-11 |
| runs/credent-2026-11-12 | 1 | origin/run/credent-2026-11-12 |
| runs/credo-q1fy27 | 1 | origin/claude/credo-quarterly-analysis-r7tbey |
| runs/cybertech-q2fy27 | 2 | origin/claude/quarterly-cybertech-q2fy27-920b89 |
| runs/cyientdlm-q2fy27 | 1 | origin/run/quarterly-q2fy27-2026-10-17 |
| runs/d-dev-q1fy27 | 1 | origin/claude/d-dev-quarterly-analysis-jnyqb1 |
| runs/datapattns-q1fy27 | 1 | origin/claude/quarterly-data-pattern-analysis-7vzvt2 |
| runs/deccangold-q1fy27 | 1 | origin/claude/deccan-gold-concall-analysis-5eyww0 |
| runs/deedev-2026-11-15 | 1 | origin/run/deedev-2026-11-15 |
| runs/dhanbank-q1fy27 | 1 | origin/claude/dhanbank-pipeline-run-bi3wv6 |
| runs/digitide-q1fy27 | 1 | origin/claude/digitite-results-analysis-yek08v |
| runs/divgi-q1fy27 | 1 | origin/claude/digvi-quarterly-analysis-o97k0v |
| runs/dpabhushan-2026-09-19 | 2 | origin/wip/laptop-save-2026-10-04 |
| runs/dssl-q1fy27 | 1 | origin/claude/quarterly-results-analysis-3y7lxn |
| runs/dycl-q2fy27 | 2 | origin/claude/qr-dycl-q2fy27-766ddd |
| runs/e2e-q1fy27 | 1 | origin/claude/e2e-quarterly-analysis-j6j65r |
| runs/ebgng-q1fy27 | 1 | origin/claude/gmg-electronics-analysis-0owflj |
| runs/ecosmobility-q1fy27 | 1 | origin/claude/ecos-mobility-quarterly-analysis-1gxkan |
| runs/eimcoeleco-q2fy27 | 1 | origin/run/quarterly-q2fy27-2026-10-17 |
| runs/emudhra-2026-09-15 | 1 | origin/claude/trusting-einstein-qap7vj |
| runs/emudhra-2026-09-19 | 1 | origin/run/emudhra-2026-09-19 |
| runs/emvdl-q1fy27 | 1 | origin/claude/emvdl-quarterly-analysis-1eikkc |
| runs/esconet-2026-10-05 | 1 | origin/run/esconet-2026-10-05 |
| runs/exicom-q1fy27 | 1 | origin/claude/exicom-q1-fy27-analysis-0bxvcc |
| runs/fabtech-2026-09-26 | 1 | origin/run/fabtech-2026-09-26 |
| runs/fairchemor-q2fy27 | 2 | origin/claude/quarterly-fairchem-q2fy27-bcfbf0 |
| runs/fedfina-q1fy27 | 1 | origin/claude/fedfina-call-analysis-ggpjgq |
| runs/fedfina-q2fy27 | 1 | origin/run/quarterly-q2fy27-2026-10-17 |
| runs/finkurve-q1fy27 | 1 | origin/claude/quarterly-results-analysis-bjv3ft |
| runs/gallantt-q2fy27 | 2 | origin/claude/quarterly-gallantt-call-q2fy27-7b3ed0 |
| runs/gargi-q1fy27 | 1 | origin/claude/gargi-quarterly-analysis-11fbsc |
| runs/gaudiumivf-q1fy27 | 1 | origin/claude/quarterly-results-analysis-7dqyyn |
| runs/gee-q1fy27 | 1 | origin/claude/g-limited-results-analysis-q4cm3w |
| runs/gemaroma-q1fy27 | 1 | origin/claude/quarterly-results-analysis-jz50z8 |
| runs/ghvinfra-q1fy27 | 1 | origin/claude/ghv-infra-quarterly-analysis-z6m8wn |
| runs/ghvinfra-q2fy27 | 1 | origin/claude/quarterly-ghv-q2fy27-3cf5aa |
| runs/gmbrew-q2fy27 | 1 | origin/run/quarterly-q2fy27-2026-10-17 |
| runs/gmdc-q1fy27 | 1 | origin/claude/gmdc-quarterly-analysis-c3vej5 |
| runs/gmmpfaudler-q1fy27 | 1 | origin/claude/gmm-pfaudler-quarterly-analysis-55jc3e |
| runs/gocl-q2fy27 | 1 | origin/run/quarterly-q2fy27-2026-10-19 |
| runs/goclcorp-q1fy27 | 1 | origin/claude/quarterly-results-analysis-d723ow |
| runs/goldium-q1fy27 | 1 | origin/claude/goldium-q1-fy27-earnings-8csvi8 |
| runs/goodluck-2026-09-19 | 1 | origin/run/goodluck-2026-09-19 |
| runs/grpltd-2026-09-15 | 1 | origin/claude/trusting-einstein-qap7vj |
| runs/grwrhitech-q2fy27 | 1 | origin/claude/quarterly-garware-q2fy27-1ec041 |
| runs/gvpil-2026-11-15 | 1 | origin/run/gvpil-2026-11-15 |
| runs/gvpil-q1fy27 | 1 | origin/claude/quarterly-results-analysis-qhuohq |
| runs/heritgfood-q2fy27 | 1 | origin/run/quarterly-q2fy27-2026-10-17 |
| runs/hfcl-q2fy27 | 1 | origin/run/quarterly-q2fy27-2026-10-19 |
| runs/iex-2026-09-08 | 1 | origin/run/iex-2026-09-08 |
| runs/indgn-agm-2026-08-13 | 1 | origin/claude/transcript-indigene-analysis-5zmus0 |
| runs/indgn-q1fy27 | 1 | origin/claude/run-pipeline-indgn-6wej1t |
| runs/indiaglyco-2026-09-02 | 1 | origin/claude/indiaglyco-docreview-run |
| runs/indiamart-q1fy27 | 1 | origin/claude/india-mart-quarterly-analysis-nujr2m |
| runs/indiamart-q2fy27 | 10 | origin/claude/qr-dycl-q2fy27-766ddd |
| runs/indiqube-q1fy27 | 1 | origin/claude/quarterly-results-analysis-i1ji43 |
| runs/indnippon-2026-09-10 | 2 | origin/run/indnippon-2026-09-10 |
| runs/indorama-q2fy27 | 1 | origin/run/quarterly-q2fy27-2026-10-17 |
| runs/indosolar-q2fy27 | 1 | origin/claude/quarterly-indosolar-q2fy27-2614ff |
| runs/invprecq-2026-11-15 | 1 | origin/run/invprecq-2026-11-15 |
| runs/iolcp-2026-09-19 | 1 | origin/run/iolcp-2026-09-19 |
| runs/ipcl-q1fy27 | 1 | origin/claude/quarterly-results-analysis-dwprvc |
| runs/ivalue-q1fy27 | 1 | origin/claude/aspara-quarterly-results-7k23p1 |
| runs/jaykay-2026-08-26 | 1 | origin/claude/jaykay-corpus-extraction-vkjw6a |
| runs/jlhl-2026-11-12 | 1 | origin/run/jlhl-2026-11-12 |
| runs/jnkindia-q1fy27 | 1 | origin/claude/jk-india-quarterly-analysis-xulrvt |
| runs/karnika-h1fy27 | 1 | origin/run/quarterly-q2fy27-2026-10-17 |
| runs/kcpsugind-q1fy27 | 1 | origin/claude/quarterly-results-analysis-mk45d6 |
| runs/kecl-q1fy27 | 1 | origin/claude/quarterly-results-analysis-oxt7o0 |
| runs/keltech-2026-11-15 | 1 | origin/run/keltech-2026-11-15 |
| runs/kernex-q1fy27 | 1 | origin/claude/quarterly-results-analysis-ixhbmx |
| runs/knack-q2fy27 | 4 | origin/claude/qr-dycl-q2fy27-766ddd |
| runs/kpl-2026-11-15 | 1 | origin/run/kpl-2026-11-15 |
| runs/krn-q1fy27 | 1 | origin/claude/quarterly-results-analysis-0ffwkb |
| runs/kross-2026-09-27 | 1 | origin/run/kross-2026-09-27 |
| runs/kross-q2fy27 | 1 | origin/run/quarterly-q2fy27-2026-10-19 |
| runs/ksolves-q1fy27 | 1 | origin/claude/k-solve-quarterly-analysis-23wdwl |
| runs/kusumgar-2026-11-12 | 1 | origin/run/kusumgar-2026-11-12 |
| runs/kwick-2026-10-04 | 1 | origin/run/kwick-2026-10-04 |
| runs/laxmiindia-q1fy27 | 1 | origin/claude/laxmi-quarterly-results-nk7iej |
| runs/lt-q2fy27 | 2 | origin/claude/qr-lt-q2fy27-6d55c1 |
| runs/ltelevator-corppres-2026-09 | 1 | origin/wip/laptop-save-2026-10-04 |
| runs/mapmyindia-q1fy27 | 1 | origin/claude/map-my-india-quarterly-analysis-43nbwc |
| runs/maxind-q1fy27 | 1 | origin/claude/max-india-earnings-analysis-2pm9im |
| runs/mcfos-q1fy27 | 1 | origin/claude/mcfos-quarterly-analysis-n1t1pq |
| runs/mideast-2026-10-25 | 2 | origin/run/mideast-2026-10-25 |
| runs/mmp-2026-10-04 | 1 | origin/run/mmp-2026-10-04 |
| runs/mtar-q1fy27 | 1 | origin/claude/mtar-annual-reports-qo0c39 |
| runs/neochem-q2fy27 | 2 | origin/claude/qr-neochem-q2fy27-76041a |
| runs/nephroplus-q1fy27 | 1 | origin/claude/nephro-plus-quarterly-analysis-vqj5xc |
| runs/netweb-q1fy27 | 1 | origin/claude/netweb-results-analysis-qb5mas |
| runs/netweb-q2fy27 | 10 | origin/claude/qr-netweb-q2fy27-a60c5c |
| runs/onwardtec-2026-11-12 | 1 | origin/run/onwardtec-2026-11-12 |
| runs/oswal-q1fy27 | 1 | origin/claude/oswal-pumps-q1-analysis-si2lg8 |
| runs/pacedigitk-q1fy27 | 1 | origin/claude/quarterly-results-analysis-vx8dc4 |
| runs/paisalo-q1fy27 | 1 | origin/claude/quarterly-results-protocol-dlltuf |
| runs/paisalo-q2fy27 | 1 | origin/claude/quarterly-paisalo-q2fy27-095262 |
| runs/paracables-q2fy27 | 10 | origin/claude/qr-dycl-q2fy27-766ddd |
| runs/paushak-q1fy27 | 1 | origin/claude/paushak-quarterly-analysis-1lg8ur |
| runs/pittieng-q2fy27 | 1 | origin/claude/quarterly-pittieng-q2fy27-3fc1e6 |
| runs/pngs-q1fy27 | 1 | origin/claude/cool-euler-1on89m |
| runs/poonawalla-q2fy27 | 1 | origin/run/quarterly-q2fy27-2026-10-17 |
| runs/premexpln-2026-11-15 | 1 | origin/run/premexpln-2026-11-15 |
| runs/premierpol-q2fy27 | 1 | origin/run/quarterly-q2fy27-2026-10-17 |
| runs/pvrinox-2026-11-12 | 1 | origin/run/pvrinox-2026-11-12 |
| runs/qll-2026-11-15 | 1 | origin/run/qll-2026-11-15 |
| runs/qmsmedi-2026-09-26 | 1 | origin/run/qmsmedi-2026-09-26 |
| runs/qpower-q1fy27 | 1 | origin/claude/qpower-q1-fy27-notion-6lgxlt |
| runs/qpower-q2fy27 | 1 | origin/run/quarterly-q2fy27-2026-10-19 |
| runs/qualitek-2026-09-26 | 1 | origin/run/qualitek-2026-09-26 |
| runs/ramrat-q1fy27 | 1 | origin/claude/ram-ratna-quarterly-analysis-0161le |
| runs/rappid-2026-09-19 | 1 | origin/run/rappid-2026-09-19 |
| runs/rategain-q1fy27 | 1 | origin/claude/red-grain-quarterly-results-1xrd0f |
| runs/rathist-q1fy27 | 1 | origin/claude/quarterly-results-analysis-lft8iz |
| runs/raymondrealty-q1fy27 | 1 | origin/claude/raymond-realty-q1-fy27-h5wmo2 |
| runs/raymondrel-q2fy27 | 10 | origin/claude/qr-dycl-q2fy27-766ddd |
| runs/rkforge-2026-11-12 | 1 | origin/run/rkforge-2026-11-12 |
| runs/route-q1fy27 | 1 | origin/claude/route-mobile-quarterly-pkqpxv |
| runs/route-q2fy27 | 1 | origin/claude/qr-route-q2fy27-fb3514 |
| runs/rsystems-q2cy26 | 1 | origin/claude/quarterly-results-analysis-j2wrxj |
| runs/sammaancap-q1fy27 | 1 | origin/claude/quarterly-results-analysis-b1d9jd |
| runs/sasken-q1fy27 | 1 | origin/claude/sasken-quarterly-analysis-xgjg0m |
| runs/satin-q1fy27 | 1 | origin/claude/quarterly-credit-care-analysis-pjrg9x |
| runs/scodatubes-q1fy27 | 1 | origin/claude/quarterly-results-analysis-91a9t7 |
| runs/sedemac-q1fy27 | 1 | origin/claude/sedemac-quarterly-analysis-4k2otx |
| runs/sfl-q1fy27 | 1 | origin/claude/sheela-quarterly-results-zxbbvj |
| runs/shareindia-2026-09-19 | 1 | origin/run/shareindia-2026-09-19 |
| runs/sharika-q1fy27 | 1 | origin/claude/quarterly-results-analysis-01wssj |
| runs/shawgeltin-2026-11-12 | 1 | origin/run/shawgeltin-2026-11-12 |
| runs/skygold-q2fy27 | 2 | origin/claude/qr-skygold-q2fy27-7e1298 |
| runs/sonacoms-q2fy27 | 10 | origin/claude/qr-dycl-q2fy27-766ddd |
| runs/southwest-2026-11-09 | 1 | origin/run/southwest-2026-11-09 |
| runs/southwest-q1fy27 | 1 | origin/claude/southrest-quarterly-results-wo3ltt |
| runs/spapparel-q1fy27 | 1 | origin/claude/sp-apparel-quarterly-analysis-q2eld6 |
| runs/sprop-q1fy27 | 1 | origin/claude/shriram-properties-quarterly-8swem6 |
| runs/srm-q1fy27 | 1 | origin/claude/quarterly-results-analysis-u9lgke |
| runs/sswl-2026-09-19 | 1 | origin/run/sswl-2026-09-19 |
| runs/stallion-q1fy27 | 1 | origin/claude/australian-india-quarterly-results-wiv2a8 |
| runs/styl-q1fy27 | 1 | origin/claude/sesha-sai-analysis-t7sqgg |
| runs/sudarcolor-2026-11-12 | 1 | origin/run/sudarcolor-2026-11-12 |
| runs/sugslloyd-q1fy27 | 1 | origin/claude/sugs-lyod-results-analysis-sa8wi5 |
| runs/supremepwr-2026-10-06 | 2 | origin/run/accord-2026-10-06 |
| runs/supremepwr-h1fy27 | 2 | origin/claude/quarterly-supremepower-q2fy27-7e9233 |
| runs/susan-2026-09-19 | 1 | origin/run/susan-2026-09-19 |
| runs/syngene-q2fy27 | 10 | origin/claude/qr-dycl-q2fy27-766ddd |
| runs/tatacomm-q2fy27 | 1 | origin/run/quarterly-q2fy27-2026-10-17 |
| runs/tatapower-q1fy27 | 1 | origin/claude/tata-power-analysis-2x2wx8 |
| runs/tatva-q1fy27 | 1 | origin/claude/quarterly-analysis-agent-z2p3ps |
| runs/tatva-q2fy27 | 1 | origin/run/quarterly-q2fy27-2026-10-19 |
| runs/tdpowersys-2026-11-15 | 1 | origin/run/tdpowersys-2026-11-15 |
| runs/tejasnet-q1fy27 | 1 | origin/claude/tejas-network-quarterly-analysis-4mzxz3 |
| runs/tejasnet-q2fy27 | 1 | origin/claude/quarterly-tejas-q2fy27-f91c3c |
| runs/tinnarubr-q2fy27 | 1 | origin/claude/quarterly-tinna-q2fy27-d4fe1d |
| runs/tll-2026-09-26 | 1 | origin/run/tll-2026-09-26 |
| runs/transrail-q1fy27 | 1 | origin/claude/transrail-quarterly-analysis-f7kqqf |
| runs/trualt-2026-09-18 | 1 | origin/run/trualt-2026-09-18 |
| runs/trualt-q1fy27 | 1 | origin/claude/truevault-quarterly-analysis-27abp5 |
| runs/uniabex-q1fy27 | 1 | origin/claude/unipart-quarterly-analysis-5ky0ug |
| runs/unimech-q1fy27 | 1 | origin/claude/quarterly-results-analysis-ffii20 |
| runs/unimech-q2fy27 | 2 | origin/claude/qr-unimech-q2fy27-1b1895 |
| runs/uniparts-q1fy27 | 1 | origin/claude/quarterly-results-analysis-9ef8ys |
| runs/urbanco-q1fy27 | 1 | origin/claude/urban-company-quarterly-analysis-ib51ci |
| runs/utlsolar-q1fy27 | 1 | origin/claude/quarterly-results-analysis-324riy |
| runs/vaibhavgbl-q1fy27 | 1 | origin/claude/quarterly-results-analysis-h2f1ss |
| runs/venuspipes-q1fy27 | 1 | origin/claude/venus-pipes-q1-fy27-jtc505 |
| runs/venusrem-2026-07-24 | 120 | origin/claude/cmsinfo-spear-pass-9v2yyz |
| runs/vividel-2026-09-07 | 1 | origin/claude/presentation-analysis-hw7bol |
| runs/vrllog-2026-11-12 | 1 | origin/run/vrllog-2026-11-12 |
| runs/walchannag-2026-11-12 | 1 | origin/run/walchannag-2026-11-12 |
| runs/welcorp-q1fy27 | 1 | origin/claude/quarterly-results-analysis-06y8qn |
| runs/wework-q2fy27 | 10 | origin/claude/qr-wework-q2fy27-97d635 |
| runs/workmates-2026-09-07-presentation | 1 | origin/claude/presentation-analysis-3onxgk |
| runs/yashhv-2026-09-26 | 1 | origin/run/yashhv-2026-09-26 |
| runs/zeel-q1fy27 | 1 | origin/claude/zeel-quarterly-analysis-9i2r1v |

## 6. Company memory files not on main (74 of 117)

526717 (claude/pipeline-526717-n61a68), 544516 (claude/pipeline-544516-8t948a), AARTISURF (claude/aartisurf-pipeline-run-3wqmjl), ACCORD (run/accord-2026-10-06), ANAWIL (run/anawil-2026-11-12), ASTRAMICRO (run/astramicro-2026-11-15), AVANA (claude/avana-pipeline-run-jq6rz4), AVIENCE (run/avience-2026-09-26), AWFIS (run/awfis-2026-09-19), AYE (claude/run-pipeline-aye-adnmeu), BALAJITELE (claude/trusting-einstein-qap7vj), BALUFORGE (claude/baluforge-2026-09-06-runs-ah784w), CEIGALL (claude/baluforge-2026-09-06-runs-ah784w), CNL (run/cnl-2026-11-11), CREDENT (run/credent-2026-11-12), CYIENTDLM (claude/baluforge-2026-09-06-runs-ah784w), DDEVPLSTIK (claude/run-pipeline-ddevplstik-405lmq), DEEDEV (run/deedev-2026-11-15), DIFFNKG (claude/run-diffnkg-pipeline-8n6qp1), DPABHUSHAN (wip/laptop-save-2026-10-04), DSSL (claude/dssl-pipeline-run-onx7hd), EBGNG (claude/ebgng-pipeline-run-e7jis5), EMUDHRA (claude/trusting-einstein-qap7vj), ESCONET (run/esconet-2026-10-05), FABTECH (claude/fabtech-pipeline-run-2ap5pp), FEDFINA (claude/fedfina-pipeline-run-3mq2uj), GAUDIUMIVF (claude/gaudiumivf-pipeline-tvrgn0), GOODLUCK (run/goodluck-2026-09-19), GRPLTD (claude/trusting-einstein-qap7vj), GVPIL (run/gvpil-2026-11-15), IEX (run/iex-2026-09-08), IKS (claude/quarterly-results-analysis-h4n2ul), INA (claude/baluforge-2026-09-06-runs-ah784w), INDIAGLYCO (claude/indiaglyco-pipeline-run-nv2zsl), INDNIPPON (run/indnippon-2026-09-10), INVPRECQ (run/invprecq-2026-11-15), IOLCP (run/iolcp-2026-09-19), JLHL (run/jlhl-2026-11-12), KECL (claude/baluforge-2026-09-06-runs-ah784w), KELTECH (run/keltech-2026-11-15), KPL (run/kpl-2026-11-15), KROSS (run/kross-2026-09-27), KUSUMGAR (run/kusumgar-2026-11-12), KWICK (run/kwick-2026-10-04), MACPOWER (claude/macpower-pipeline-g9ouq4), MENONBE (claude/menonbe-pipeline-run-bs4dq5), MMP (run/mmp-2026-10-04), MODISONLTD (claude/modisonltd-pipeline-run-e5lytf), ONWARDTEC (run/onwardtec-2026-11-12), PREMEXPLN (run/premexpln-2026-11-15), PVRINOX (run/pvrinox-2026-11-12), QLL (run/qll-2026-11-15), QMSMEDI (run/qmsmedi-2026-09-26), QUALITEK (run/qualitek-2026-09-26), RAMRAT (claude/ramrat-pipeline-run-e5xukv), RAPPID (run/rappid-2026-09-19), RKFORGE (run/rkforge-2026-11-12), SHAREINDIA (run/shareindia-2026-09-19), SHAWGELTIN (run/shawgeltin-2026-11-12), SICALLOG (claude/sicallog-pipeline-pwftth), SOUTHWEST (run/southwest-2026-11-09), SSWL (run/sswl-2026-09-19), SUDARCOLOR (run/sudarcolor-2026-11-12), SUPREMEPWR (run/supremepwr-2026-10-06), SUSAN (run/susan-2026-09-19), TDPOWERSYS (run/tdpowersys-2026-11-15), TLL (run/tll-2026-09-26), TRUALT (run/trualt-2026-09-18), UNIMECH (claude/quarterly-results-analysis-ffii20), VOEPL (claude/voepl-pipeline-run-ppnypi), VRLLOG (run/vrllog-2026-11-12), WALCHANNAG (run/walchannag-2026-11-12), YASHHV (run/yashhv-2026-09-26), YASHO (claude/yasho-industries-step-one-iuo5ii)

## 7. Companies with no `companies/<TICKER>.md` on any branch (127)

ADFFOODS, ADOR, AEROFLEX, AKUMS, AMEENJI, ANUP, APEXECO, ARIS, ATLANTAELEC, BALAMINES, BANDHAN, BIRLACABLE, BIRLANU, BLACKROSE, CREDO, CYBERTECH, DATAPATTNS, DECCANGOLD, DHANBANK, DIGITIDE, DYCL, E2ENETWORKS, ECOSMOBLTY, EIMCOELECO, EMVDL, EXICOM, FABCLEAN, FAIRCHEMOR, FINCABLES, FINKURVE, FLUIDOMAT, GALLANTT, GANECOS, GARGI, GEE, GEMAROMA, GHVINFRA, GMBREW, GMDC, GMMPFAUDLER, GOCLCORP, GOLDIAM, GRWRHITECH, GSMFOILS, HERITGFOOD, HFCL, INDIAMART, INDIQUBE, INDORAMA, INDOSOLAR, INOXINDIA, IPCL, IVALUE, JAYKAY, JITFINFRA, JNKINDIA, KARNIKA, KERNEX, KNACK, KOPRAN, KRN, KSOLVES, LAXMIINDIA, LT, LTELEVATOR, MAPMYINDIA, MAXIND, MCFOS, MTAR, NEOCHEM, NEPHROPLUS, NETWEB, NRAIL, OSWAL, PACEDIGITK, PAISALO, PARACABLES, PARKHOSPS, PAUSHAK, PNGSREVA, POONAWALLA, PREMIERPOL, PURETROP, QPOWER, RATEGAIN, RATHIST, RAYMONDREL, ROUTE, RPTECH, RSYSTEMS, SAMBHV, SAMHI, SAMMAANCAP, SASKEN, SATIN, SCODATUBES, SEDEMAC, SHARIKA, SKYGOLD, SMRUTHI, SONACOMS, SPAPPAREL, SPROP, SRM, STALLION, STLTECH, STYL, SUGSLLOYD, TATACOMM, TATAPOWER, TEJASNET, TINNARUBR, TIPCO, TRANSRAIL, UNIABEX, UNIPARTS, URBANCO, UTLSOLAR, VAIBHAVGBL, VENUSPIPES, VILAS, VIVIDEL, WELCORP, WEWORK, WORKMATES, ZAGGLE, ZEEL

## 8. Run folders with more than one version across branches (111)

The census read the version with the most non-input files (main on a tie). Other versions were not read.

526717-2026-07-15 (2), 544332-2026-08-04 (2), 544516-2026-07-15 (2), 544555-2026-07-30 (2), aartisurf-2026-08-04 (4), aequs-2026-09-05 (3), aequs-q2fy27 (2), aimtron-2026-07-12 (3), akums-2026-07-10 (3), amagi-2026-07-12 (2), apexeco-2026-07-10 (2), asianene-2026-07-13 (3), aurum-2026-07-14 (2), avana-2026-07-16 (2), aye-2026-07-22 (3), aye-q1fy27 (2), azad-2026-07-12 (2), baluforge-2026-09-06 (2), birlacable-2026-08-20 (2), borana-2026-09-07 (3), capillary-2026-09-19 (2), ceigall-2026-09-06 (3), cleanmax-2026-09-01 (4), cmsinfo-2026-08-29 (4), cybertech-q2fy27 (2), cyientdlm-2026-09-06 (3), ddevplstik-2026-07-23 (2), dhanbank-2026-07-27 (2), diffnkg-2026-09-05 (2), divgiitts-2026-08-29 (2), dssl-2026-07-27 (3), ebgng-2026-07-12 (2), entero-2026-07-27 (5), fabtech-2026-08-04 (2), fairchemor-q2fy27 (2), fedfina-2026-07-15 (3), fincables-2026-08-12 (3), fluidomat-2026-07-16 (2), fratelli-2026-09-07 (3), gallantt-q2fy27 (2), ganecos-q1fy27 (2), ganecos-q4fy26 (2), gaudiumivf-2026-07-16 (3), gsmfoils-2026-07-24 (2), hfcl-q1fy27 (2), iks-q1fy27 (2), ina-2026-09-06 (3), indgn-2026-08-03 (2), indiaglyco-2026-08-24 (2), indnippon-2026-09-10 (2), indoborax-2026-08-30 (3), jitfinfra-2026-08-12 (2), jublcpl-2026-08-18 (2), kabraextru-2026-09-05 (2), karnika-2026-07-11 (2), kcpsugind-2026-07-21 (3), kecl-2026-08-05 (2), kecl-2026-09-06 (2), kissht-2026-09-19 (2), knack-q2fy27 (2), kopran-2026-07-14 (2), kronox-2026-08-30 (4), laxmiindia-2026-07-22 (2), macpower-2026-07-30 (2), maninds-2026-08-21 (4), mapmyindia-2026-07-13 (2), maxind-2026-07-24 (2), menonbe-2026-07-16 (3), millworks-2026-08-22 (2), modisonltd-2026-09-03 (2), mpsltd-2026-09-03 (3), netweb-q2fy27 (2), northarc-2026-07-12 (2), nrail-2026-07-22 (2), obscp-2026-07-12 (2), orchpharma-2026-09-06 (5), paracables-q2fy27 (2), parkhosps-q1fy27 (2), permagnet-2026-08-19 (3), pittieng-2026-09-05 (2), prizor-2026-07-12 (2), ramrat-2026-07-29 (3), rathist-2026-07-20 (4), rptech-q1fy27 (2), sambhv-q1fy27 (2), samhi-q1fy27 (2), sfl-2026-07-14 (3), shharich-2026-09-05 (2), shyammetl-2026-07-19 (3), sicallog-2026-07-28 (2), sonacoms-q2fy27 (2), stltech-q1fy27 (2), supremepwr-h1fy27 (2), syngene-2026-09-15 (3), systango-2026-08-29 (2), taaltech-2026-09-10 (3), tatva-2026-07-12 (2), titanbio-2026-09-10 (3), totem-2026-09-09 (2), ufbl-2026-08-05 (3), ufbl-q1fy27 (2), venusrem-2026-07-23 (2), venusrem-2026-09-02 (4), vilas-2026-09-03 (2), vinyas-2026-09-01 (3), visakaind-2026-09-05 (2), voepl-2026-07-18 (3), voepl-2026-09-06 (2), wework-q2fy27 (2), yasho-2026-09-05 (2), zaggle-2026-07-27 (2)

## 9. Folder and ticker corrections

- Merged as one company: `d-dev-q1fy27` + `deedev-2026-11-15` (DEEDEV); `544555-2026-07-30` + `ameenji-2026-07-24` (AMEENJI); `qualitek-2026-09-26` + `qll-2026-11-15` (QUALITEK); `gocl-q2fy27` + `goclcorp-q1fy27` (GOCLCORP); `raymondrealty-q1fy27` + `raymondrel-q2fy27` (RAYMONDREL); `sona-q1fy27` + `sonacoms-q2fy27` (SONACOMS); `divgi-q1fy27` + `divgiitts-2026-08-29` (DIVGIITTS).
- Ticker differs from folder name: 530077 (PURETROP), 544332 (FABCLEAN), e2e (E2ENETWORKS), ecosmobility (ECOSMOBLTY), goldium (GOLDIAM), pngs (PNGSREVA).
- Left out of the census: `runs/mideast-2026-10-25`. It is a video production run, not a company.
- Kept under the folder code because the files give no ticker: 526717, 544516.

## 10. Every scored row and what the score rests on (67)

Most scores rest on a statement in a review file against a thesis band, tripwire or run-rate, not on a like-for-like number. Read the note before using the score.

| ticker | period | result | basis (comparison_note) |
|---|---|---|---|
| ADFFOODS | Q1FY27 | MISS | Rule 1: file states "Consolidated revenue ... 167.29 (L323) / BELOW RED (below bear)" vs Notion Q1 band Red <180 (Notion bands used as "bear/base/bull proxy"); 167.29 is 7.1% under the Red line of 180 and 14.2% under Green 195. Ex-credit EBITDA margin ~13.4% also "RED" (<17%). vs guidance: "Q1 annualised ~Rs 669 Cr vs ~Rs 900 Cr FY27 guidance". Not a point base case. |
| AEQUS | Q2FY27 | MISS | Rule 1: operator brief says falsification test set by draft model 'Both legs fired' (consumer segment EBITDA loss Rs 40.1 cr vs 36.1 cr line; utilisation 17% vs 23%); review: FY27 run-rate revenue 1,622.8 'Below base by 4.0%', EBITDA 94.9 'Below base by 38%', PAT (210.4) 'Between bear and base, 78% of the way to bear'. Part-year: H1 revenue Rs 804.62 cr = 47.6% of FY27E base Rs 1,690 cr; H1 PAT Rs (105.62) cr = 66.8% |
| AMAGI | Q1FY27 | BEAT | File states: "Actuals land AT/ABOVE base on the one testable key metric (revenue growth +32.4%)" (direction ambiguous; coded BEAT as growth 32.4% exceeds the 25% base CAGR). Ratios, not annualised: Q1 revenue 436.88 = 23.2% of FY27E base 1,882.0; Q1 PAT 33.91 = 30.0% of FY27E base 112.9. No guidance figure stated vs actual in the file. |
| ANUP | Q1FY27 | MISS | File: "Actual lands BELOW BEAR on revenue AND margin" (annualised Q1x4 ~Rs 472 cr vs base 929; margin 7.99% vs base 19.5%). Quarter vs full-year base, so rule 3 ratio: Q1 = 12.7% of FY27E base Rs 929 cr. Pre-committed thesis-broken trigger fired via margin leg. |
| ASIANENE | Q1FY27 | IN LINE | Refresh file: "revenue and PAT track BASE; the one metric tracking toward BEAR is the consolidated margin (7.80% vs 9.5% base blend)". Plain ratio: Q1 rev 271.19 = 28.6% of July FY27E base 949 (not annualised). Margin 7.80% vs July base 12.5% is below. vs guidance: standalone +29.4% "just below the 30-40% guide floor". |
| AURUM | Q1FY27 | MISS | File states against thesis: "Operating profit ex one-times / -4.86 Cr (filing) / BELOW any positive base / Falsification metric FIRED" (review L182). No FY27 numeric base exists to compare. |
| AURUM | Q2FY27 | MISS | File states against thesis: "trigger 1 FIRED (Reading A, pre-named test)" core PBT ex-OI Rs(0.52) Cr after Q1 Rs(4.86) Cr (review L500, L648). Revenue +63.9% YoY and core loss narrowed from Rs(11.47) Cr; no FY27 numeric base to compare. |
| AYE | Q2FY27 | IN LINE | Rule 1: review says PAT "At/above Base on run-rate" and AUM growth "Base (lower half)" (26.03% vs 25-30%); wording ambiguous between in line and beat. Not annualised: H1 PAT 161.22 = 53.7% of FY27E base ~Rs 300 cr. Net thesis impact stated: WEAKENED (no trigger fired). Base FV was revised 11-Aug from Rs 324 to Rs 288. |
| BALAMINES | Q1FY27 | BEAT | Rule 1: review states "The pre-committed Q1 test lands BULL" (25.41% vs bull >=19%). vs guidance: margin ABOVE 22-23% guide; volume -21.7% YoY BELOW +10-15% guide ("BELOW guide (miss)"). |
| BANDHAN | Q1FY27 | MISS | Review §6A: ROA 'Below old base; at low end of revised'; advances, deposits, CASA 'In line'. Metric is ROA vs 1.6-1.8% aspiration; no NII/PAT base grid ('not passed inline'). Actuals 'NOT below bear on 2+ metrics'. |
| DEEDEV | Q1FY27 | MISS | Q1 revenue is the prior-quarter figure in the Q2 print. vs guidance: Q1 deferral of ~Rs 25 cr 'not visible in Q2'. // from runs of group D-DEV: Review: 'Margin path to >19% / Base thesis / +86 bps YoY ... Still 210 bps short; no inflection / DELAYED'; 'Consol EBITDA margin / FY27 guidance >19% / 16.89% / Below guidance by ~210 bps'. Revenue +31.6% YoY 'comfortably ahead of a 25% CAGR pace'. No numeric Q1 base. Model- |
| E2ENETWORKS | Q1FY27 | BEAT | File states result vs our thesis: review L288 'Core operating actuals land AT or ABOVE base on revenue, margin, PAT and Exit MRR level'; valuation_provisional L34 'running ~2 years ahead of the plan'. Q1 Rs156.76 Cr = 31.4% to 52.3% of FY27 roadmap Rs300-500 Cr (plain ratio, not annualised). vs guidance: margin 75.21% vs '64% guide'. |
| EBGNG | Q1FY27 | BEAT | File states vs thesis: 'Actuals at/above base? YES (above the RAISED guide on all testable rails)' and 'a clean operational beat'; it also says no per-quarter Bear/Base/Bull numeric grid was passed. Part-year vs full-year: Q1 revenue Rs 412.46 cr = 17.5% of FY27E base Rs 2,363.9 cr; Q1 PAT Rs 28.93 cr = 16.4% of FY27E base Rs 176.82 cr. vs guidance: +32.1% vs raised 30% rail |
| ECOSMOBLTY | Q4FY26 | MISS | File states: 'scale-up SUSPENDED (FY26 margin recovery failed)'; Q4 FY26 review held recovery leg 'BROKEN as written' (Notion digest L7-8). Margin 11.6% vs thesis 13-15%. |
| ECOSMOBLTY | Q1FY27 | MISS | File states: 'Actuals land BELOW BEAR on operating EBITDA margin (10.34% vs >=12% floor) and PAT margin (6.88% vs ~8%)'. vs guidance: FY27 EBITDA guide 11-13%/13-15%, delivered 10.34%, cut to ~10% = MISSED; revenue 15-18% delivered. |
| EMVDL | Q1FY27 | MISS | Rule 1 (file states result vs our thesis): "Q1 = 868 ... BELOW FLOOR on run-rate; TBD full-year" and monitor #1 "Q1 ₹868 Cr ... RED (Q1 below 1,200)". Full-year thesis break is "NOT YET (armed)". |
| EXICOM | Q1FY27 | MISS | Rule 1: file states "Consolidated quarterly EBITDA / Bull >= 0 / Bear < -Rs20 Cr / -Rs21.9 Cr ... / BELOW BEAR LINE". Revenue/PAT base not available. vs guidance: Q4 FY26 breakeven (+0.27) "reversed"; guidance softened to Q2 or Q3. |
| GARGI | Q1FY27 | MISS | Review states vs thesis: 'Binary test: 1 of 4 legs pass...3 of 4 fail'; 'Four Notion REDs'. Revenue growth +10.64% vs 30% binary; vs guidance: '+10.64% actual vs ~35% guided'. |
| GRWRHITECH | Q2FY27 | BEAT | File states it (6A): revenue "Above Bull on H1 pro-rata"; margin "Above Base (both bases...)"; PAT "Above Base". H1 revenue 1,328.61 vs pro-rata base 1,229.5 = +8.1%; H1 PAT 262.09 vs 198.5 = +32.0%; H1 margin 28.66% (25.70% ex-OI) vs base 24%. About Rs 11 cr of H1 margin is a one-off tariff refund (call, ASR). vs guidance: guide raised to 27% ±2%; TPU not commissioned by 23-Oct. |
| GVPIL | Q1FY27 | IN LINE | Review: revenue 'At/near base path'; op margin 14.5% 'Above base' (FY28E 12%); PAT 'Above base optically; normalise for tax' (4.1% ETR). 'roughly in line with the Notion FY28E implied ~6.5% CAGR path'. Different-year base; file statement used. |
| GVPIL | Q2FY27 | MISS | Our Q1 review set Q2 trajectory test: margin >= ~14% (core PBT >= ~Rs 37 Cr) confirms; < ~10% raises the one-quarter-print concern. Actual 9.8% < 14%. No Q2 revenue base. Q2 run file itself states no result vs base. vs guidance: revenue Rs 311 Cr 'inside the Rs 300 to 320 Cr band'; 11% normalised margin: Q2 9.8% below. |
| HFCL | Q1FY27 | BEAT | File states: "Q1FY27 lands AT or ABOVE base on revenue, margin and PAT run-rate" (L281); caveat: its base column is the 40% aspiration (~Rs 6,929 cr), L270 says no quarterly Notion base. Part-year vs full-year: Q1 revenue = 30.9% of FY27E 6,200; Q1 PAT = 47.2% of FY27E 520. vs guidance: Q1 run-rate ~Rs 7,660 cr ~10% above 40% aspiration. |
| HFCL | Q2FY27 | BEAT | File states H1 "runs far above the old Notion base" (L347) and Step 6A revenue row "ABOVE BASE; AT GUIDE" (L1084); Q2 annualised PAT and TTM PAT each exceed Notion FY27 PAT 520 by more than 25% (L697). Part-year: H1 revenue 4,456.77 = 71.9% of FY27E 6,200; H1 PAT 639.86 = 123.1% of FY27E 520. vs guidance: H1 x 2 = 8,913.54 vs guide floor 8,908.69 (AT guide). |
| INDGN | Q1FY27 | MISS | Rule 1: Q1 review 6A 'Below the recovery glide-path this quarter' (operating margin 16.4% vs base path ~16.4%->20%); 'Net thesis impact: WEAKENED (not broken)'; primary margin tripwire 'FIRED on the underlying basis'. Numeric bands ND in the review. B11 base was built after Q1 actual was known. |
| INDIAMART | Q1FY27 | IN LINE | File (6A L289-L295): standalone revenue +8.5% vs ~13.6% CAGR HOLD path "Below the aspirational base on volume; on-path on realization"; margin 39.7% "At/above base"; PAT "At base"; L365 "Actuals AT or ABOVE BASE on the financial line? Yes on margin, cash and consol PAT; below aspiration on volume-driven revenue growth". Mixed; no numeric base for the quarter. |
| INDIAMART | Q2FY27 | IN LINE | File 6A L371-L374: revenue growth 9.6% "between bear (7%) and base (10%)" (H1 10.5% "at base"); EBITDA margin 37.1% "Above bull on print", mgmt 33% guide equals base; PAT "ND". Revenue 9.6% vs 10% base = 4% below. Thesis-broken #6 (enquiries -14% YoY, 2 quarters) "fired as written" (L418, L486). vs guidance: mgmt revenue band 8-10%, in band. |
| IPCL | Q1FY27 | BEAT | File states vs thesis: "Actuals at/above base? Operationally yes"; triggers 1 (EBITDA Rs 11.21 cr vs >= Rs 9.5 cr) and 3 (P&F 8.17% vs < 9.5%) MET but "low-bar", trigger 2 (A&D order book) NOT DISCLOSED. No numeric base-case comparison. |
| IVALUE | Q1FY27 | MISS | Review L159: "profit metrics land AT-or-ABOVE base ... top-line growth lands BELOW base (gross sales +5.7% vs >18% thesis expectation). Mixed". No numeric FY27E base. vs guidance: guidance maintained, not tested (L51 of concall review). |
| JNKINDIA | Q4FY26 | BEAT | Discussion notes: 'FY26 beat model (consol rev 818 vs 750E; PAT 65 vs 63E)'. Arithmetic: revenue 818/750 = +9.1%; PAT 65/63 = +3.2%. Whether the 750E/63E model predates the FY26 result is not stated in files. |
| JNKINDIA | Q1FY27 | MISS | File states vs our model: 'Q1 tracking: revenue on track/ahead ... Profit light on margin (needs 13.5%, got 11.8% reported / 8.8% operating)'; review 6A: 'Reported EBITDA margin / Base 14-16% band (T2) / 11.8% consol / 14.0% std / Below base band'. Add-back gate: 0 of 5 conditions fired. Full-year base vs one quarter, so no arithmetic test. vs guidance: guidance cut to 12-14% and clean operating margin below it. |
| KCPSUGIND | Q1FY27 | MISS | File states against our thesis: Eimco leg 'WEAKENED -> near DEAD on this filing'; 'Two of six pre-committed thesis-broken triggers FIRED'; Rs 257 Cr order not confirmed, only Rs 153.40 Cr intra-group contract; Eimco margin 11.6% vs ~20% floor. |
| KERNEX | Q1FY27 | BEAT | File: "tracking AT or ABOVE the Notion base case on revenue, margin and PAT pace". Q1 revenue Rs 503.58 cr = 42% of FY27E base Rs 1,200 cr; clean PAT Rs 101.26 cr = 42.4% of Rs 239 cr; margin 32.33% vs base 30%. Order book Rs 3,641 cr incl GST vs thesis ~Rs 6,500 cr: WEAKENED. |
| KRN | Q1FY27 | BEAT | Review 6A: consolidated Q1 revenue 252.32 'Above Bull' (>=185); L497-499 'Actual between BEAR and BASE?... not below base on the thesis-relevant consolidated line'; L500 'Actual at/above BASE? On the consolidated (thesis) line, yes'. Standalone 181.97 'between bear and bull' (neutral). Bull also needs utilisation 50%+ (UNKNOWN). |
| KROSS | Q2FY27 | IN LINE | File states result vs our table (review Step 6A): '0 metrics below Bear; 3 at or above Base (revenue, PAT, EPS)'; revenue 'Base to Bull', PAT 'At Base'. Arithmetic, H1 vs 50% of FY27 base: revenue 419.43 vs 415 = +1.1%; PAT 33.16 vs 32.5 = +2.0%. H1 margin 12.71% between Bear 12.3% and Base 13.0%. Part-year vs full-year base; file's pro-rata test. vs guidance: margin 13.02% below 14-15%. |
| KSOLVES | Q1FY27 | MISS | Review: revenue growth item 'RED (1 of 2 qtrs)' vs green >=18%; 'management's own de-facto FY27 revenue guidance (+4-5% max) lands BELOW the thesis growth expectation'; 'implied FY27 growth ~4-5% is BELOW the thesis base case'. Margin 30.3% GREEN. vs guidance: growth +10% vs prior 18-20%. |
| NEPHROPLUS | Q1FY27 | BEAT | Rule 1: v2 6A table: revenue growth +23.7% vs >15% "Above base"; margin 23.1% adj / 22.7% vs >22% "Above base"; "No metric lands below bear." Bands are monitoring thresholds, not point projections (v1 6A says Notion has no line-item projections). vs guidance: 23.7% vs 15-20% medium-term guide. |
| NETWEB | Q4FY26 | BEAT | Notion page states: 'FY26 (ACTUAL) Rs 36.30 ... Beat base (Rs 33). Bull was Rs 44. Revenue at bull case (Rs 2,183 Cr).' EPS 36.30 vs 33 = +10.0%. |
| NETWEB | Q2FY27 | BEAT | Review: 'Guidance compares above Base on EPS; above Bull only if H2 PAT margin holds at or above about 8.5%'. H1 EPS 38.60 = 75.7% of FY27E base EPS 51 and 59.4% of bull 65 (review). Revenue: no base (ND). Cash goes the other way: thesis-broken #1 'BREACHED ON THE H1 READING'. vs guidance: FY27 Rs 4,000 cr implies H2 Rs 1,857.03 cr, 13.3% below H1. |
| OSWAL | Q1FY27 | MISS | Rule 1 (file statement): "This-quarter readings are below the FY26 base on the key headline metrics (revenue growth -7.9% vs base +44%; margins reset lower)" and "this quarter's guidance is a below-base start" vs Notion EPS path. Base is FY26 actual/Notion path, not a Q1 point estimate. Gate 1 proxy "NEGATIVE / not yet PASS". vs guidance: no prior concall guidance (first tracked run). |
| PAISALO | Q1FY27 | IN LINE | model_variance file: PAT "On Base, almost exactly"; "a slightly-ahead-of-Base quarter". Plain ratio 61.3 / 244 = 25.1% of FY27E base. Gate: C/I ~40% above 35%, trigger (d) fired; fees not disclosed (concall review L27). |
| PARKHOSPS | Q1FY27 | IN LINE | File 6A: revenue 'Below base run-rate' (475.71 x4 = ~1,903 vs 1,990 per file), EBITDA margin 'At base', PAT 'At/above base - but tax-flattered (~21% real)'; Step 8: 'between bear and base on revenue run-rate and at/above base on tax-flattered PAT/EPS'. Mixed wording; classified IN LINE on file statement 'squarely at the +18.5% base pace' (normalized). vs guidance: mgmt FY27 Rs 2,080 Cr / PAT Rs 360 Cr sits above our  |
| PNGSREVA | Q1FY27 | BEAT | Rule 1: merged review 6A: Revenue "At/above Bull (directional)"; EBITDA margin "Above band on Q1 and guided year"; PAT "Above base (directional)"; "actuals at/above base-bull on every metric with data". Q1 Rs117.973 cr = 26.9% of FY26 base and 20.7% of FY27 bull Rs 571 cr (117.973/571, my arithmetic from file numbers). vs guidance: Q1 EBITDA 28.76% vs full-year guide 25-27%. |
| QPOWER | Q4FY26 | MISS | File: "Revenue AT BASE (Rs 947 Cr). Operating EBITDA margin BELOW BEAR (18.6% vs 19% floor)... Total PAT BETWEEN BEAR-BASE (Rs 185.55 Cr vs 160/207)". PAT 185.55 vs base 207 = -10.4%, revenue 947 = base. Variance line is in the 07-Sep-2026 AR deep dive; the date the FY26 base was set is not shown in the files. vs guidance: FY26 "Revenue OVERDELIVERED (+12% vs revised guidance)". |
| QPOWER | Q1FY27 | IN LINE | File: "Q1 revenue Rs 256.4 Cr -> ~Rs 1,136 Cr FY27 at guided 20%, at Notion base Rs 1,140 Cr; adjusted EBITDA margin 28.3% above the ~18-20% base assumption. Operations = at-to-above base." Ratio, not annualised: 256.4 = 22.5% of FY27E base 1,140. Revenue vs checklist: AMBER (below green Rs 290 cr, above red Rs 250 cr). Delays: magnet wire Q3 -> Q4 FY27; Sangli commercial 'DELAYED (schedule maintained)'. |
| RAYMONDREL | Q1FY27 | MISS | File: "Margin 17-19% guide is above the Q1 13% actual, so this quarter is between the thesis bear and base on margin, not yet a base-case confirmation." Full-year base vs one quarter, revenue not comparable. Two margin figures: 13% (call) vs 11.61% (filed derived). |
| RAYMONDREL | Q2FY27 | MISS | File 6A: "actuals land BETWEEN BEAR AND BASE (revenue near base; margin at bear; PAT run-rate at or below bear, 264-309 vs 300)". H1 revenue Rs1,275.19 Cr = 35.4% of FY27E ~Rs3,600 Cr; H1 PAT Rs66.49 Cr = 18.0-19.6% of FY27E base 340-370. Management revenue guide withdrawn. |
| ROUTE | Q4FY26 | MISS | FY26 revenue 4,408.21 vs base 4,427 = -0.4% (in line); FY26 PAT 256.94 vs base 338 = -24.0% (MISS). FY26 PAT includes the Rs 135.87 cr exceptional (SIAC arbitration Rs 107.96 cr + vendor Rs 27.91 cr); files disagree on its quarter (digest L55-56 says Q4 FY26; Q2 review says Q2 FY26 carried it). Op EBITDA margin 12.19% vs base 12.0%. No file states the Q4 result against base. |
| ROUTE | Q1FY27 | MISS | Mixed. Files: Q1 binary "reads BULL (revenue +9.58% >= +1.8%)"; Cap-5% gate "FAILS on GM leg" (GM 20.88% vs 23%); thesis-broken trigger 1 "1 of 2"; "margin guidance BELOW the thesis path". Coded MISS on margin. Ratios, not annualised: Q1 revenue 1,151.51 = 23.2% of FY27E base 4,958; Q1 PAT 68.55 = 17.4% of FY27E base 394. vs guidance: revenue +9.58% above the 5-9% guide top; adj EBITDA 9.5% vs ~12% guide MISSED. |
| ROUTE | Q2FY27 | MISS | File 6A: revenue "between Bear and Base" (H1 2,331.18 vs half-year base 2,479); "Below Base (-23.3%)" for H1 PAT (151.10 vs 197); EPS 22.57 vs 31.3 "Below Base (-27.9%)"; margin Adj 9.8% H1 vs base 12.5% "Below Base". Ratios, not annualised: H1 revenue 2,331.18 = 47.0% of FY27E 4,958; H1 PAT 151.10 = 38.3% of FY27E 394. Review is pre re-audit (PAUSED). |
| RPTECH | Q1FY27 | BEAT | File 6A: revenue growth 'At/above base' (+61.9% vs >20% green); EBITDA margin 'Green (level)'; PAT 'At/above base (accrual)'; CFO 'INDETERMINATE'. Notion carries FY26 actuals as base, not explicit Q1 FY27 lines. vs guidance: n/a (first call). |
| RSYSTEMS | Q1FY27 | BEAT | Rule 1: file states margin 'At/above Bull' (20.07% vs base >=18.5%, review L296). Organic growth and ROCE 'UNDETERMINED', revenue/PAT bases ND (L296-L297). Result filing date not stated; Notion edit 2026-07-29 precedes the 2026-08-04 review. Margin only. vs guidance: management guided sustainable margin ~18% (concall). |
| SAMBHV | Q1FY27 | IN LINE | File 6A: 'Q1FY27 lands at or above the base trajectory on revenue, EPS run-rate and EBITDA/tonne; margin is flat (in line, not expanding). No metric is below bear.' Bear/Base/Bull FY27 cells ND; FY29-anchored proxy (Rs 1.92 x4 = ~Rs 7.68 annualised vs FY29 base 9.87). Mixed 'at or above'; classified IN LINE. vs guidance: Q1 +31% vs mgmt FY27 +10-15% ('contradicted in direction'); EBITDA/ton ~9,355 vs Q1 guide 7,000-8 |
| SASKEN | Q1FY27 | BEAT | File: 'Revenue Rs339.24 Cr and PAT Rs23.52 Cr land at/above base on the P&L, but the master gate ... is NOT cleared' (EBITDA 9.5% vs >=10% criterion FAIL). No numeric base; classified per file statement. |
| SATIN | Q1FY27 | BEAT | Review: 'by our own rules this is an at-or-above-plan quarter'; PAT 122.65 vs gate 110 = +11.5% above (122.65/110); GNPA 2.18% <= 3.05%; ROE 16.75% >= 16% ('cleared by a whisker'). All stop-loss triggers not breached. |
| SCODATUBES | Q1FY27 | MISS | Rule 1 (file): "Revenue at/above base; operating margin BELOW guide; ... PAT trajectory below base. Mixed, tilted negative" (6A landing verdict). Revenue +27.6% YoY "at/above base on top-line"; op margin 12.85% "Below the 14-15% guide"; PAT 5.250 "Below a base FY27 path". No point quarterly base (Revenue/PAT Bear/Base/Bull = ND). |
| SFL | Q1FY27 | BEAT | Review table (quarterly Bear/Base/Bull ND): revenue "likely ≥ Base on top line"; PAT "Above Base on headline, but 23% non-recurring-aided"; standalone core margin "Below-Bear signal", falsification trigger (c) FIRED on standalone <10% limb. No numeric quarterly base. |
| SOUTHWEST | Q2FY27 | MISS | No modelled base. Rule 2 on the pre-result bar in our Q1 review (22-Jul-2026): 'Q2 FY27 must clear ~Rs 68 Cr'; actual Rs 57.73 cr = -15.1% vs Rs 68 cr (57.73/68 - 1). Profit base NOT FOUND. Step1 brief L16: 'Q2 FY27 is the first test, and it printed 14.38%' vs 'at or above the 24% FY26 margin'. vs guidance: H1 +16.3%, H2 needs +22.7% to reach ~20% (05-concall L249). |
| SPAPPAREL | Q1FY27 | MISS | File states vs thesis gate: 'SPUK thesis-broken tripwire = FIRED' (SPUK EBITDA -Rs 1.04 cr, 2nd consecutive negative quarter); 1 of 5 testable early warning signals fired; master 3+ rule not triggered; consol revenue Rs 401.08 cr only Rs 1.08 cr above the Rs 400 cr line. Mixed: consol PAT +20.4%, margin +220 bps. No quarterly base number exists. Classified MISS on the thesis-broken tripwire statement. |
| SRM | Q1FY27 | MISS | Rule 1 (file): 6A "Revenue growth YoY (std) / <10% (red) / ~15-20% / >20% (green) / +5.05% / Below Bear / red zone (organic)". Margin: std 21.83% / consol 19.44% vs base ~15-16% "Above band — but unverified". Consol +37.83% "N.M. — not organic". Post-result addendum base (FY27E consol Rs 1,300 cr, dated 13-Aug-2026, same day as filing) not used as a pre-result base. |
| STLTECH | Q1FY27 | BEAT | Rule 1: review 6A: revenue annualised Rs 7,640 cr vs base ~Rs 5,500 cr "At/Above Base"; reported EBITDA margin 20.8% vs 20% by Q4FY27 "Above Base (3 qtrs early)"; PAT "Above trend". Annualised one-quarter vs annual run-rate base (B11 flags FLAG-ONE-QUARTER). vs guidance: 20% margin guide met early (Role 5 3A: PARTIALLY DELIVERED). |
| SYNGENE | Q2FY27 | MISS | File: "Target reported: MIXED. Revenue is above the Notion base path. Margin, core PBT and cash are weak." Revenue Q2 832.7 vs ~790 base = +5.4% (revenue alone BEAT; "Between Base and Bull"). Margin H1 15.18% / Q2 17.70% vs FY27 base 19.7% and PAT H1 23.2 vs FY27 base ~207: "Between Bear and Base". Marked MISS because profit lines are below base; revenue BEAT. vs guidance: Q2 -8.6% "inside the single-digit decline gu |
| TEJASNET | Q2FY27 | MISS | File states vs thesis: 'Below the FY27 floor run-rate' (Q2 annualised 1,622.72 vs floor 2,000; needs 596.08/qtr in H2) and PAT/EBITDA 'Below Bear' (FY29E end-points); 'Probability re-weighting FIRES'. No numeric FY27 base exists. Thesis-broken FY27 floor test itself: 'NOT FIRED (full-year test)'. |
| TRANSRAIL | Q1FY27 | MISS | File: revenue growth "BELOW BEAR (vs any growth band)": +4.0% vs thesis base +22-25% / co. guide +20-22%; margin "BASE (low end)" 11.90% in 11.5-12.5% band; PAT "BELOW BASE on quality"; net debt Rs466.42 cr vs anchor Rs274 cr "WORSE". Order intake Rs1,034 cr RED. |
| UNIMECH | Q4FY26 | BEAT | FY26 vs FY26E: revenue 240.49/250 = -3.8% (within 5%), PAT 63.28/58 = +9.1% (>5% above), so BEAT by rule 2. File says: "Revenue marginally light; profit beat the trough estimate" and "mixed signal". Base dated 29 May; press release 28 May; file says base built on FY26E with actuals pending. Q4 PAT -10.6% YoY. |
| URBANCO | Q1FY27 | BEAT | Rule 1, single metric only: pre-committed test was ICS ex-InstaHelp NTV growth >=22% survives, <18% weakens; actual 29%, review says "Above test bar" and "cleared decisively (29% vs >=22% bar)". No Bear/Base/Bull numbers for revenue, EBITDA or PAT exist (ND). Consolidated PAT swung to a loss. |
| UTLSOLAR | Q1FY27 | BEAT | File 6A: revenue 'ABOVE Base - +49.5% over the Q1 phasing target' (1,345.693 vs ~900); PAT margin 'AT Base (mid-band)' 12.25% vs 12%; reported PAT 'below any case, but entirely because of the fire exceptional'; file concludes 'AT or ABOVE Base'. Base is the guidance proxy, not an independent projection. |
| VENUSPIPES | Q1FY27 | MISS | File states: 'Two pre-committed watch lines MISSED: PAT (26.4 < 28-30) and EBITDA margin (16.08% < 16.5% and not rising)'; 'Below base on the two lines that matter'; revenue growth 15.96% 'BELOW the 25% Green line'. PAT 26.41 vs 28 = -5.7%. vs guidance: ~20% FY27 growth, Q1 run-rate 'a touch light'. |

## 11. Conflicts and caveats reported during extraction

- MIDEAST: not a company; runs/mideast-2026-10-25 is a video production run.
- TIPCO: runs/tipco-2026-08-05 is a Regulation 30 review of promoter acquisitions, no results.
- UNIABEX: run invoked as "UNIPART"; document is Uni Abex Alloy Products.
- CMSINFO: valuation dated 2026-08-31, after Q4FY26 and Q1FY27 results. FY26 services revenue Rs 2,360 Cr (11-valuation.md) vs Rs 2,312 Cr (media release); both recorded.
- CYBERTECH, KNACK: base numbers are post-result indicative estimates; treated as NO BASELINE.
- MACPOWER: base built 30-Jul, one day after Q1 FY27 result; Q1 actuals from a non-anchored operator-context file.
- RSYSTEMS: calendar-year reporter; Q1 CY26 mapped to Q4FY26 row, Q2 CY26 to Q1FY27 row.
- Several quarterly-only names: risk flags rest on Notion thesis text quoted inside run files; the Notion pages are not in the repo.
- GOLDIAM: run folder is named goldium-q1fy27; files say Goldiam International (GOLDIAM).
- MILLWORKS: two variants disagree. Main folder: PROCEED WITH CAVEATS, FLAG-CASH INDETERMINATE, Gate 0 83/160. LESSONS_ARCHIVE off-main line: PROCEED WITH FLAGS, FLAG-CASH STRUCTURAL, Gate 0 81/160. Both recorded.
- Weak first_analysis_date: INOXINDIA (Notion CMP date), GARGI (Notion snapshot date), KRN (run date; earlier thesis undated), STALLION (board-approval date), SHARIKA (filing date). NOT FOUND: VAIBHAVGBL, GMDC.
- FABCLEAN (run folder 544332-2026-08-04): dirty run, halted at Stage 1/2; collector put sibling Fabtech Technologies Ltd (BSE 544558) filings in the target's slots. FY26 figures conflict: about Rs 221 cr (concalls/screener) vs Rs 431.33 cr (operator summary, called FTL/group scale by the halt file). Both recorded.
- CYIENTDLM: first analysis 2026-09-06 gate verdict REWORK; no valuation. Mental model unsigned.
- HERITGFOOD: only a Q2FY27 quarterly run; no company file.
- EBGNG Q1FY27: BEAT rests on the review's own statement ("Actuals at/above base? YES"); the review says no per-quarter base grid was passed.
- MENONBE: base case made 2026-07-16, the same day as the Q1 FY27 result, and uses its numbers; results PDFs are image-only, actuals from the B10 report.
- BIRLANU: only a Q1 FY27 results review; no thesis baseline.
- Run folders that hold inputs and a manifest only (no report of any kind on any branch): ameenji-2026-07-24, kopran-2026-07-14, kecl-2026-08-05, venusrem-2026-07-23, venusrem-2026-07-24. kecl-2026-09-06 and voepl-2026-09-06 hold a manifest and extracted corpus text only.
- FEDFINA: valuation of 2026-07-15/16 has no FY27E revenue, margin or PAT; base is EPS CAGR 15% to Y3 (FY29E) EPS Rs 13.87. Operator flipped Pillar 2L multiplier 0.80x to 1.00x on 2026-07-16.
- VISAKAIND: Phase 1 only, gate verdict REWORK; actuals are screener-tier, unverified against a filing.
- WORKMATES: only a 2026-09-07 deck review; decision AVOID at Rs 392; actuals are the Notion thesis record quoted in the review.
- AURUM: only forward base is Year-3 SOTP (FY29E revenue Rs 733 Cr, PAT Rs 30 Cr); no FY27E base. Q1FY27 and Q2FY27 are MISS because the quarterly reviews state our tripwire 1 fired, not from a like-for-like number. FY26 total income conflict: Rs 424 Cr (July run) vs Rs 412.43 Cr (Q2 review); both recorded.
- PERMAGNET: base dated 2026-08-19 to 08-23, after the Q4FY26 and Q1FY27 results; actuals come from noisy OCR text of the results PDFs.
- AEQUS: only base is the unsigned Notion projection (FY27 revenue Rs 1,690 cr, PAT Rs (158) cr); no Stage 10/11 valuation. Q2FY27 MISS rests on the operator brief statement that the draft model's falsification test fired on both legs.
- INDGN: B11 base built 2026-08-03 with Q1 FY27 actuals in hand. Q1FY27 MISS rests on the Q1 review text ("Below the recovery glide-path", thesis "WEAKENED").
- SUPREMEPWR: base is the operator-commissioned forward module of 2026-10-06, not a pipeline valuation; the H1 review never received the module.
- GALLANTT, INDGN: board marked "main" from NSE and BSE listing lines; no file names the board outright.
- Some line numbers come from grep output and may be approximate; a few sources entries drop the branch prefix on continuation items.
- AYE Q2FY27: IN LINE rests on review wording (PAT "At/above Base on run-rate", AUM "Base (lower half)"); ambiguous between IN LINE and BEAT. FY26 total income conflict: Rs 1,863.24 cr (10-valinputs.md) vs Rs 1,844.94 cr (Q2 operator brief); both recorded.
- TRUALT: FY27E base dated 2026-10-02; the draft calls the figures "illustrative" and "not a forecast of record".
- URBANCO Q1FY27: BEAT rests on one metric (ICS ex-InstaHelp NTV growth 29% vs pre-committed >=22% test); no revenue, EBITDA or PAT base; consolidated PAT was a loss of Rs (92.12) cr.
- KROSS: no Section 1B valuation; only base is the Notion FY27 table, labelled INFERENCE off Q1 plus management guidance. Q2FY27 IN LINE rests on the review's own H1 vs 50%-of-FY27-base check (revenue 419.43 vs 415; PAT 33.16 vs 32.5), a part-year test.
- JUBLCPL: base numbers cover Business A (PP&C) only; actuals are whole company. Two PP&C Q1 growth figures in 10-assembly: 25.5% (L324) and 27.5% (L326); both recorded.
- KISSHT: base dated 4 Oct 2026, after Q4FY26 and Q1FY27 results; no Q2FY27 result in files.
- INDIAGLYCO: base (run 2026-08-24) post-dates Q4FY26 and Q1FY27 results; base has FY27E consolidated PAT Rs 312.2 Cr only. Company demerged 1 Sep 2026; no Q2FY27 result in files. Results file is OCR text.
- UNIMECH Q4FY26: BEAT by the 5% rule (FY26E revenue Rs 250 Cr vs actual 240.49, -3.8%; PAT Rs 58 Cr vs 63.28, +9.1%); the file calls it a "mixed signal". Pre-result FY27E range (Rs 480-500 Cr revenue, Rs 95-105 Cr PAT) is from a 2026-08-04 illustrative scenario. Q1 run log: companies/UNIMECH.md was absent at the time.
- ZEEL: no company file, no base case, review undated; guidance facts come second-hand from a Notion baseline not in the repo.
- AZAD: base from 2026-07-12 stage 11 valuation (FY27E revenue Rs 743.88 cr, EBITDA margin 35.0%, PAT margin 21.0%); full-year only, FY27E PAT in rupees not in file. H1 actual Rs 363.53 cr = 48.9% of FY27E base. Company file on the 2026-11-15 branch, 2026-07-12 run folder on main.
- TATACOMM: no company file. FY26 PAT Rs 996.85 cr (total) vs Rs 1,039.04 cr (continuing operations); both recorded.
- INA: Q1FY27 profit Rs 37.04 cr (screener sheet) vs Rs 38.02 cr (board outcome extract); Q4FY26 profit Rs 70.07 cr vs Rs 69.84 cr; both recorded.
- KABRAEXTRU: FY26 EBITDA Rs 10 cr (chairman's letter) vs Rs 13.05 cr (MD&A table); Q1 FY27 filing named as missing from corpus.
- BALAJITELE: archetype "NO SINGLE ARCHETYPE FITS"; shallow analysis only, dated 2026-09-15.
- RAYMONDREL: Q1 folder is named raymondrealty-q1fy27; same company. No company file. MISS in Q1FY27 and Q2FY27 rests on review text ("between the thesis bear and base on margin"; "actuals land BETWEEN BEAR AND BASE"). Q1 margin: 13% as spoken on the call vs 11.61% as filed; both recorded.
- FABTECH, UFBL: base (2026-08-04, 2026-08-05) post-dates Q4FY26 and Q1FY27 results. UFBL base is pre-Ind AS while reported figures are Ind AS; the Q1 review says no Notion base exists while a 2026-08-05 valuation sits on another branch; both recorded.
- DSSL: base 2026-07-27 has only a Yr3 (FY29E) figure. MAPMYINDIA: FY27E numbers in the FTTCP draft are labelled "illustrative".
- SHAWGELTIN: forward numbers come from the CARE rating, not management; Q2 results were due on the run date and are not in the corpus.
- HFCL: BEAT in Q1FY27 and Q2FY27 rests on review text against the Notion thesis base (FY27E revenue Rs 6,200 cr, EBITDA 17.5%, PAT Rs 520 cr). The Q1 review's own base column is management's 40% aspiration and it says the Notion page has no quarterly base, so Q1 is arguable. Base table comes from a Notion brief fetched 2026-10-19; thesis dated 4-Jun-2026. Q1 run was invoked as "HFCA".
- CAPILLARY: analysis (2026-09-19) and base (2026-10-10) post-date Q4FY26 and Q1FY27 results; no Q2 result in files.
- TATVA: base runs to FY29 only (revenue Rs 755 cr, EBITDA 20%, PAT Rs 71.7 cr); projection basis quoted as "SOM-implied revenue CAGR".
- JAYKAY: monitoring-grade corpus extraction, no valuation. LTELEVATOR: deck review only, price targets but no base case.
- 526717: base stops at FY29E. FY26 EBITDA margin 9.55% (Q1 review) vs 8.13% (valuation file); both recorded. projection_basis "capacity" is the closest allowed label; the file states an 18% revenue CAGR with logic text.
- IEX: stages 10 and 11 never ran; no base.
- MANINDS: base dated 2026-08-21, after Q4FY26 and Q1FY27 results. First verdict PROCEED WITH FLAGS (gate file) vs PROCEED WITH CAVEATS (LESSONS_ARCHIVE first-pass line); both recorded. FY26 consolidated revenue Rs 3,563.9 cr filed vs Rs 3,592.5 cr on the call. Operator kill-line override on 2026-08-25.
- PITTIENG: only estimate is the indicative FY27E/FY28E in the operator brief dated 2026-10-24, two days after the 22-Oct Q2 result. Archetype from an unsigned draft Mental Model.
- LESSONS_ARCHIVE off-main excerpts cite line numbers of the union file built for this census, not a repo file.
- ECOSMOBLTY (run folder ecosmobility-q1fy27): ticker from review header. MISS in Q4FY26 and Q1FY27 rests on file text ("FY26 margin recovery failed"; "Actuals land BELOW BEAR"); base is a margin range only.
- GOCLCORP: gocl-q2fy27 and goclcorp-q1fy27 are the same company. first_analysis_date is month only (Notion "Created May 2026").
- RAMRAT: gate-recommendation.md says REWORK (Verifier A, 3 CRITICAL, acceptance 0%); the company file says PROCEED WITH CAVEATS; both recorded.
- KCPSUGIND Q1FY27: MISS rests on the review statement that two of six thesis tripwires fired; no FY27E revenue or profit base, only SOTP values.
- CLEANMAX: only forward figure is FY30 forward EBITDA of about Rs 4,100 Cr, written after the Q4FY26 and Q1FY27 results.
- AARTISURF: base dated 4 Aug 2026, after the Q1 result filed 1 Aug. DYCL, ANAWIL: base post-dates the Q2/H1 result.
- DYCL, GEE, SAMHI: no company file. GEE and SAMHI have only Notion-quoted qualitative bases. GEE Q1FY27: file states a mixed result; recorded NO BASELINE with the quote.
- ORCHPHARMA: no valuation.
- GRWRHITECH, INDIAMART: only base is a Notion page copy saved in the run folder (13-May-2026, 30-Apr-2026), built after the Q4 FY26 print. GRWRHITECH Q2FY27 BEAT rests on review text ("Above Base" on revenue, margin and PAT). INDIAMART Q1FY27 and Q2FY27 IN LINE rest on "at/above base" wording; Q2 revenue growth 9.6% vs 10% base.
- SYNGENE: no valuation run; base is the Notion signed model of 28-Sep-2026 quoted in the Q2 review. Q2FY27 MISS: review verdict is "MIXED" (revenue 5.4% above the Rs 790 cr Q2 path; margin and PAT between bear and base).
- SKYGOLD: operator-brief FY27E/FY28E figures post-date the result; not counted as a base.
- GAUDIUMIVF: the Q1 FY27 review ran on a different branch and says no company file or Decision Status existed; it did not carry the July flags.
- Board "main" for several names rests on NSE and BSE listing lines, not on an explicit main-board statement.
- ASIANENE Q1FY27: IN LINE rests on the refresh file ("revenue and PAT track BASE"); consolidated margin 7.80% vs July base 12.5% is in the note. FY27E Rs 949 cr is from the 2026-08-14 refresh; the July valuation gives only a 20% CAGR.
- PAISALO Q1FY27: IN LINE rests on "On Base, almost exactly" for PAT; the cost-to-income gate failed (about 40% vs 35%). Q2FY27: H1 PAT Rs 126.96 cr = 52.0% of FY27E base Rs 244 cr.
- SFL Q1FY27: BEAT rests on review wording (revenue "likely >= Base", PAT "Above Base on headline") with no numeric quarterly base; standalone core margin 8.99% was below the 10% falsification line and that tripwire fired. FY26 core EBITDA 10.29%/10.05% (Q1 review) vs 10.8% (B05); both recorded.
- SONACOMS: folders sona-q1fy27 (main) and sonacoms-q2fy27 (branch) are the same company; Notion page has no FY27 revenue, margin or PAT base.
- TLL: phase 1 only; half-yearly; Q1 figures come from the step-1 brief, labelled web-sourced company memory.
- AVANA: base dated 2026-07-16, after FY26 results of 21-May-2026; SME half-yearly; H1 FY27 not in files. KIADB plant delay (mid-May 2026 target, now end-Oct 2026) recorded.
- FAIRCHEMOR: Q2 review says "no base-case projection exist (ND)"; operator-brief FY27E post-dates the result.
- KARNIKA: 2026-07-11 run ended in FTTCP DEEP WATCH leaning AVOID, no valuation; SME half-yearly, H1 filing carries Q1 and Q2 columns.
- NETWEB: base is the Notion EPS path (FY27 base EPS Rs 51), no revenue base. Q4FY26 BEAT: Notion page says "Beat base (Rs 33)". Q2FY27 BEAT on EPS per review text (H1 EPS 38.60 = 75.7% of Rs 51); cash flagged RED, operator ruling open.
- TEJASNET: base is Notion FY29E end-points only. Q2FY27 MISS rests on review text ("Below the FY27 floor run-rate", "Below Bear"). BSNL tripwire overridden by a 27-Aug operator ruling.
- VENUSPIPES Q1FY27: MISS; review says both pre-committed watch lines missed (PAT 26.41 vs 28-30; EBITDA margin 16.08% vs 16.5%).
- APEXECO, SICALLOG, SYSTANGO: base dated after the Q4 FY26 result; Q1/Q2 FY27 results not in files. SYSTANGO FY26 EBITDA margin appears as 45.4% (10-valinputs.md), 37.6% and about 33.1% for H2 (gate-recommendation.md); all recorded.
- BALUFORGE, SSWL, TDPOWERSYS: Phase 1 lite runs, no valuation. WEWORK: only an indicative FY27E built after the result.
- Some mgmt_stated_reason cells are the stage 5 report's summary, not a verbatim management quote (SSWL, TDPOWERSYS, KROSS); the cells say so.
- AMAGI Q1FY27: BEAT; the file says "AT/ABOVE base" (ambiguous); coded BEAT because growth of 32.4% exceeds the 25% base CAGR.
- QPOWER: no company file; base is Notion thesis text copied into run folders (FY27E Rs 1,140 cr). Q4FY26 MISS: PAT Rs 185.55 cr vs Rs 207 cr (-10.4%), date the FY26 base was set is not in files. Q1FY27 IN LINE: file says revenue "at Notion base". Q2 folder holds only an EGM outcome and the Nigde commencement letter.
- ROUTE: no company file; base from Notion copy (FY26E Rs 4,427 cr, FY27E Rs 4,958 cr). Q4FY26 MISS: revenue -0.4%, PAT Rs 256.94 cr vs Rs 338 cr (-24.0%). Q1FY27 MISS was coded on margin gates while revenue ran ahead of guidance. Q2FY27 MISS: review says "Below Base (-23.3%)" on H1 PAT. The Rs 135.87 cr exceptional is placed in Q4 FY26 by the July Notion digest and in Q2 FY26 by the Q2 review. First analysis date is month only (2026-05).
- DIVGIITTS: FY26 revenue Rs 375 cr quoted on the call vs Rs 352.89 cr in the filing; base post-dates Q4FY26 and Q1FY27.
- PRIZOR: base runs Year 0 = FY25 to FY28E; FY26 unaudited actual Rs 147.9 cr already exceeds FY28E base Rs 105.2 cr; base post-dates all three periods.
- EIMCOELECO: no base; lessons-archive "Eimco" hits concern KCPSUGIND's Eimco-KCP unit, a different entity.
- DEEDEV: run folders d-dev-q1fy27 and deedev-2026-11-15 are the same company (DEE Development Engineers). Rows merged under DEEDEV. Q1FY27 MISS rests on review text (margin path to >19% "DELAYED"). Q2 FY27 figures partly from Step-1 web briefs.
- BANDHAN Q1FY27: MISS rests on review text (ROA "Below old base"); no NII or PAT base grid.
- GVPIL: Q1FY27 IN LINE ("At/near base path" for revenue); Q2FY27 MISS (Q1 review set a Q2 margin test of about 14%; actual 9.8%). Q2 figures partly from Step-1 web briefs. No valuation has run.
- SATIN Q1FY27: BEAT; PAT Rs 122.65 cr vs pre-committed Rs 110 cr gate (+11.5%).
- ACCORD, TAALTECH, ADOR: forward figures post-date the result for some periods; not counted as a base there.
- No company file: BANDHAN, SATIN, SHHARICH, ADOR, GMBREW, POONAWALLA. SHHARICH FY26 revenue Rs 184 cr vs Rs 185 cr and profit decline 19% vs 18% across two files; both recorded.
- E2ENETWORKS (run folder e2e-q1fy27): ticker from the Notion packet. Q1FY27 BEAT rests on review text ("AT or ABOVE base"; "~2 years ahead of the plan").
- SOUTHWEST Q2FY27: MISS against a bar in our own Q1 review of 22-Jul-2026 ("Q2 FY27 must clear ~Rs 68 Cr"); actual Rs 57.73 cr (-15.1%). The bar is a derived threshold, not a modelled base case.
- PARACABLES: folder sits on a branch named qr-dycl-q2fy27-766ddd; content is Paramount Communications. Operator ruling on the cash-flow falsifier is pending.
- LT, PARACABLES, PREMIERPOL: estimates dated after the result; context only. AKUMS: Year-3 base only.
- FRATELLI: FY26 revenue Rs 181.29 cr vs Rs 184 cr; Q1FY27 revenue Rs 44.72 cr vs Rs 45.4 cr. CEIGALL: FY26 profit Rs 309 cr vs Rs 312 cr. Both values recorded in each case.
- QUALITEK: run folders qualitek-2026-09-26 and qll-2026-11-15 are the same company; rows merged (check at merge).
- MTAR Q1FY27: NO BASELINE; Q1 actual = 32.2% of the May-2026 FY27E base of Rs 1,121 Cr; review says "Actuals do NOT land below bear on any metric - they are strong".
- ENTERO: Q1FY27 and Q4FY26 quarterly actuals come from work/operator-ferried-2026-08-29.md, marked non-anchored. The August rebuild was used; the agent reported the July run as not in the export.
- AIMTRON FY26 revenue Rs 301.2 Cr consolidated (concall report) vs Rs 257.13 Cr standalone (valuation). OBSCP FY26 EBITDA margin 19.8% vs 19.5%.
- 544516 (Airfloa): base has a Year-3 figure only, read as FY29 because Year-0 is FY26.
- ATLANTAELEC: only forward base (FY27E revenue Rs 2,740 Cr, PAT margin 10.7%, CON PAT Rs 293 Cr) is dated 22 Jul 2026, after the Q1 result of 21 Jul.
- ASTRAMICRO FY26 revenue Rs 713.2 Cr total income vs Rs 701.58 Cr revenue. ONWARDTEC FY26 revenue Rs 550 Cr vs Rs 544 Cr; Q2 EBITDA Rs 26.5 Cr vs Rs 26.6 Cr. ESCONET FY26 margin 3.46% EBITDA vs 2.60% CRISIL operating margin. Both values recorded in each case.
- ASTRAMICRO, PREMEXPLN: Q2 FY27 call transcript absent; Q2 reasons NOT FOUND. PVRINOX FY26 revenue not stated in any file.
- Phase 1 only, no valuation: ASTRAMICRO, CREDENT, EMUDHRA, ESCONET, INDNIPPON, MMP, ONWARDTEC, PREMEXPLN, PVRINOX.
- BALAMINES Q1FY27: BEAT; review says "The pre-committed Q1 test lands BULL" (25.41% vs bull threshold of 19% or more). Run was invoked as "Balaji Mines"; issuer is Balaji Amines.
- INDIQUBE Q1FY27: NO BASELINE; review table has "Base proj ND" and says only "At/above base".
- FLUIDOMAT, GSMFOILS, JITFINFRA, NRAIL: base is the FTTCP "EXPECTED, illustrative" column, made after FY26 results.
- VILAS FY26 revenue (about Rs 470 cr) is a derived figure in the files. SHAREINDIA Q1FY27 actuals come from secondary sources quoted in the step1 brief.
- PNGSREVA (run folder pngs-q1fy27): ticker from the files.
- NEPHROPLUS, PNGSREVA, STLTECH Q1FY27: BEAT rests on the file's own statement; the "base" is a monitoring band or an annualised run-rate, not a point projection.
- RATHIST: manifest BSE code 513456 belongs to Kanishk Steel (a peer); the company's code in the files is 504903.
- LAXMIINDIA: the Q1FY27 review calls it a "NEW NAME" with no prior thesis and does not cite the 2026-07-22 Phase 1 run on a different branch.
- BORANA, TITANBIO, RKFORGE: Phase 1 only, no valuation. RKFORGE Q2FY27 actuals come from the step-1 brief (web sources).
- STLTECH valuation dated 2026-07-24, after the Q1 result. TOTEM FY27 base set after the Q1FY27 result. GANECOS valuation dated one day after the Q1 result; base is a normalised, undated figure.
- ANUP Q1FY27: MISS; the review itself says "below bear" on annualised Q1 against FY27E. TRANSRAIL Q1FY27: MISS; review says revenue growth "below bear".
- KERNEX, IPCL Q1FY27: BEAT from the file's own wording.
- MCFOS, SEDEMAC: quarterly Bear/Base/Bull cells were not passed (ND); NO BASELINE.
- DECCANGOLD: concall-only run, no results filing, review undated. SEDEMAC: Notion thesis undated.
- First coverage with no base: DECCANGOLD, IKS, TATAPOWER, MODISONLTD, YASHO.
- JNKINDIA: Q4FY26 BEAT from notes ("FY26 beat model (consol rev 818 vs 750E; PAT 65 vs 63E)"); the files do not say whether the 750E model predates the FY26 result. Q1FY27 MISS from notes ("Profit light on margin (needs 13.5%, got 11.8% reported / 8.8% operating)").
- SPAPPAREL Q1FY27: MISS; review says "SPUK thesis-broken tripwire = FIRED" while consolidated PAT rose 20.4%.
- WELCORP Q1FY27: NO BASELINE; review calls Q1 revenue "Below the pro-rata base run-rate (seasonal Q1 low)" against a full-year base.
- INDOSOLAR, TINNARUBR, NEOCHEM: FY27E only in an operator brief written after the result. NEOCHEM call transcript is operator-pasted and unverified, never processed by the A1 to A5 chain.
- DHANBANK, INVPRECQ, KUSUMGAR, VRLLOG: Phase 1 gates only, no base. Some KUSUMGAR and VRLLOG Q2 actuals are web figures from the step1 brief.
- VENUSREM: FTTCP draft dated 2026-09-03 has FY27E revenue about Rs 877 Cr, OPM about 18.0%, and a scenario base margin of 11.8%; both margins recorded. Only venusrem-2026-09-02 holds reports.
- KRONOX: Q1 FY27 PAT growth 16.24% (company file) vs +38.5% (gate, B05, Verifier B; gate says operating PBT rose 16.2%). INDOBORAX: FY26 PAT Rs 50.27 Cr (concall) vs Rs 49.74 Cr (company file). Both recorded.
- SUSAN: gate file line 1 says PROCEED WITH FLAGS; its text says the cash flag caps it at PROCEED WITH CAVEATS. Recorded as filed.
- QMSMEDI: moved from NSE SME to Mainboard on 2026-06-18; Q4FY26 was reported while SME.
- Phase 1 lite or first-time quarterly review, no valuation: AWFIS, CNL, DATAPATTNS, GOODLUCK, INDOBORAX, KRONOX, QMSMEDI, SAMMAANCAP, SUDARCOLOR, SUSAN.
- PARKHOSPS, SAMBHV Q1FY27: IN LINE; RPTECH, SASKEN, UTLSOLAR Q1FY27: BEAT. All five are classifications of mixed file wording ("at/above base"), not arithmetic. SASKEN's master gate (EBITDA 9.5% vs 10% criterion) was not cleared. UTLSOLAR's "base" is the management-guidance midpoint used as a proxy; reported PAT fell on the Bawal fire exceptional item.
- UTLSOLAR is the ticker for Fujiyama Power Systems Ltd.
- WALCHANNAG: FY26 revenue Rs 296 Cr (web brief) vs Rs 275 Cr (narrative and screener); Q1 FY27 EBITDA 1,432 vs 1,431 Lakhs in two press releases; PAT lines from the web-sourced step-1 brief.
- SMRUTHI: base exists (FY27E Rs 107.07 Cr, EBITDA 11.5%, PAT Rs 3.7 Cr); Q1 and Q2 FY27 actuals not in files. MPSLTD: entry price only.
- Phase 1, no valuation: DPABHUSHAN, IOLCP, QLL, WALCHANNAG.
- AMEENJI: run folders 544555-2026-07-30 and ameenji-2026-07-24 are the same company (Ameenji Rubber); rows merged under AMEENJI. The ameenji folder holds a manifest only.
- PURETROP (run folder 530077-q2fy27): base is an orchestrator "indicative estimate" dated 2026-10-29, after the 27-Oct-2026 result.
- DIGITIDE: file names in the run use a wrong "dssl" slug; CORRECTION.md voids the Dynacons tripwire and thesis the run had borrowed.
- EMVDL Q1FY27: MISS; review marks owned presales Rs 868 Cr "RED", "BELOW FLOOR on run-rate" vs the Q1 red line of Rs 1,200 Cr.
- KELTECH: stage 5 tables carry digit misreads fixed by ERRATA-verifier-corrections.md (Q2 EBITDA margin ex other income 8.16%, not 8.21%). KPL: filed Q2 MD&A prints PAT Rs 50 Cr, which is the EBITDA value; consolidated Q2 PAT is Rs 29.03 Cr.
- KWICK: half-yearly, no results after listing; only FY26 prospectus numbers.
- ADFFOODS, EXICOM, OSWAL, SCODATUBES, SRM Q1FY27: MISS from the file's own statement against thesis bands or watch lines. SCODATUBES verdict is mixed (revenue at or above base; margin and PAT below).
- SRM: only FY27 base (Rs 1,300 cr) is a post-result addendum dated 13-Aug-2026, the filing day; not used as a base.
- STYL Q1FY27: NO BASELINE; triggers split (revenue +21.1% favourable; EBITDA margin 25.1% breached the >27% line).
- OSWAL: run had only the concall transcript; Q1FY27 actuals come from CMD and CFO opening remarks.
- KECL: kecl-2026-08-05 and kecl-2026-09-06 hold no analysis text; only kecl-q1fy27 has a review.
- AVIENCE: SME half-yearly; H1 FY27 not published at run date.

## 12. Checks run on the census

- Format: 726 rows, 3 per company, no duplicate ticker and period pair, every `result_vs_base` in the allowed set.
- Cited paths: 4,768 `branch:path` citations parsed from `sources`; 4,767 exist in the files read. The one that does not: AVANA, `runs/avana-2026-10-05/outputs/final/step1-business-brief.md`.
- Numbers: the first number in each filled revenue and profit cell (base and actual) was searched in that company's files. 1,158 of 1,172 were found verbatim. The 14 not found are Rs lakh to Rs crore conversions (AIMTRON, DEEDEV, FEDFINA, KELTECH, MODISONLTD, SOUTHWEST, WALCHANNAG); the cell shows the lakh figure beside the conversion.
- Not checked: line numbers. Several are approximate (taken from search output). Quotes were not re-read one by one.
- `board`: `main` often rests on an NSE and BSE listing line, not on an explicit main-board statement. The cell carries the qualifier where the extractor gave one.
