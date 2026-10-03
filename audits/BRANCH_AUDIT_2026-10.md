# Branch audit, October 2026

Date: 2026-10-03. Compared against `origin/main` at `c3bf379`, after deepening the clone to full history (the session clone was shallow, which had made merged branches look stranded). Merged = tip is an ancestor of main (`git merge-base --is-ancestor`) or listed by `git branch -r --merged`. Category comes from the paths a branch changed since its merge base: FRAMEWORK if it touches frameworks/, .claude/, CLAUDE.md, tools/, prompts/, verifiers/, settings or the style files; QUARTERLY by name or a `runs/*-qNfyNN` folder; RUN if it touches only runs/, companies/, screens/, data/ or LESSONS; merged branches have no diff left, so they are categorised by name.

## Counts

| merged | category | branches |
|---|---|---|
| no | FRAMEWORK | 28 |
| no | OTHER | 1 |
| no | QUARTERLY | 97 |
| no | RUN | 99 |
| yes | FRAMEWORK | 31 |
| yes | OTHER | 13 |
| yes | QUARTERLY | 5 |
| yes | RUN | 30 |
| | total | 304 |

## All branches

| merged | category | branch | last commit | author | run-folder check |
|---|---|---|---|---|---|
| no | FRAMEWORK | (local) claude/inflection-opus-5.5-audit-102xpl | 2026-10-03 | Claude |  |
| no | FRAMEWORK | (local) framework/oct-2026-model-update | 2026-10-03 | Claude |  |
| no | FRAMEWORK | claude/auto-compact-threshold-lcb3a2 | 2026-07-25 | Claude |  |
| no | FRAMEWORK | claude/baluforge-2026-09-06-runs-ah784w | 2026-09-11 | Claude |  |
| no | FRAMEWORK | claude/damodaran-framework-amendments-2wmk1z | 2026-08-19 | Claude |  |
| no | FRAMEWORK | claude/gmg-electronics-analysis-0owflj | 2026-07-31 | Claude |  |
| no | FRAMEWORK | claude/inflection-opus-5.5-audit-102xpl | 2026-10-03 | Claude |  |
| no | FRAMEWORK | claude/laxmi-quarterly-results-nk7iej | 2026-08-12 | Claude |  |
| no | FRAMEWORK | claude/narrative-writing-style-guide-ijkol4 | 2026-08-11 | Claude |  |
| no | FRAMEWORK | claude/netweb-results-analysis-qb5mas | 2026-07-30 | Claude |  |
| no | FRAMEWORK | claude/pipeline-finalize-updates-b6gkr7 | 2026-07-10 | Claude |  |
| no | FRAMEWORK | claude/pipeline-input-contract-refactor-ywsitf | 2026-07-09 | Claude |  |
| no | FRAMEWORK | claude/pipeline-repair-signal-wiring-5v31ae | 2026-08-20 | Claude |  |
| no | FRAMEWORK | claude/quarterly-analysis-agent-z2p3ps | 2026-07-21 | Claude |  |
| no | FRAMEWORK | claude/quarterly-credit-care-analysis-pjrg9x | 2026-07-31 | Claude |  |
| no | FRAMEWORK | claude/quarterly-results-analysis-ffii20 | 2026-08-04 | Claude |  |
| no | FRAMEWORK | claude/quarterly-results-analysis-jz50z8 | 2026-08-13 | Claude |  |
| no | FRAMEWORK | claude/sasken-quarterly-analysis-xgjg0m | 2026-08-04 | Claude |  |
| no | FRAMEWORK | claude/section1b-banners-stage11-sync | 2026-08-19 | Claude |  |
| no | FRAMEWORK | claude/sfl-pipeline-run-lya9nj | 2026-07-14 | Claude |  |
| no | FRAMEWORK | claude/shyammetl-pipeline-run-x08gtb | 2026-07-19 | Claude |  |
| no | FRAMEWORK | claude/tata-power-analysis-2x2wx8 | 2026-07-27 | Claude |  |
| no | FRAMEWORK | claude/token-consumption-analysis-6tl0ko | 2026-08-03 | Claude |  |
| no | FRAMEWORK | claude/token-consumption-spike-f1tz7x | 2026-07-29 | Claude |  |
| no | FRAMEWORK | claude/truevault-quarterly-analysis-27abp5 | 2026-07-29 | Claude |  |
| no | FRAMEWORK | claude/urban-company-quarterly-analysis-ib51ci | 2026-08-01 | Claude |  |
| no | FRAMEWORK | framework/oct-2026-model-update | 2026-10-03 | Claude |  |
| no | FRAMEWORK | tools/chartink-push-main | 2026-09-25 | sumit-604 |  |
| no | OTHER | claude/kids-game-repair-ylpv03 | 2026-10-03 | Claude | folders: -; on main: no; branch-only files: 0; modified: 0 |
| no | QUARTERLY | claude/adf-food-quarterly-analysis-b8cygp | 2026-07-30 | Claude | folders: adffoods-q1fy27; on main: no; branch-only files: 20; modified: 0 |
| no | QUARTERLY | claude/aeroflex-results-analysis-x9xrqs | 2026-07-29 | Claude | folders: aeroflex-q1fy27; on main: no; branch-only files: 24; modified: 0 |
| no | QUARTERLY | claude/anoop-engineering-quarterly-8lr5l1 | 2026-08-06 | Claude | folders: anup-q1fy27; on main: no; branch-only files: 15; modified: 0 |
| no | QUARTERLY | claude/aspara-quarterly-results-7k23p1 | 2026-07-30 | Claude | folders: ivalue-q1fy27; on main: no; branch-only files: 23; modified: 0 |
| no | QUARTERLY | claude/aurob-proptech-investor-analysis-cqrz1p | 2026-07-21 | Claude | folders: aurum-q1fy27; on main: no; branch-only files: 23; modified: 0 |
| no | QUARTERLY | claude/australian-india-quarterly-results-wiv2a8 | 2026-08-12 | Claude | folders: stallion-q1fy27; on main: no; branch-only files: 6; modified: 0 |
| no | QUARTERLY | claude/availability-check-oyrf2l | 2026-08-04 | Claude | folders: sambhv-q1fy27; on main: yes; branch-only files: 13; modified: 0 |
| no | QUARTERLY | claude/balaji-mines-quarterly-analysis-ygfira | 2026-07-28 | Claude | folders: balamines-q1fy27; on main: no; branch-only files: 12; modified: 0 |
| no | QUARTERLY | claude/birlanu-quarterly-results-2zbr6l | 2026-08-06 | Claude | folders: birlanu-q1fy27; on main: no; branch-only files: 4; modified: 0 |
| no | QUARTERLY | claude/black-rose-quarterly-analysis-a9u9a4 | 2026-07-31 | Claude | folders: blackrose-q1fy27; on main: no; branch-only files: 6; modified: 0 |
| no | QUARTERLY | claude/bundan-bank-q1-fy27-lo837s | 2026-07-22 | Claude | folders: bandhan-q1fy27; on main: no; branch-only files: 18; modified: 0 |
| no | QUARTERLY | claude/conference-call-analysis-a2myie | 2026-07-30 | Claude | folders: aye-q1fy27; on main: no; branch-only files: 2; modified: 0 |
| no | QUARTERLY | claude/cool-euler-1on89m | 2026-07-30 | Claude | folders: pngs-q1fy27; on main: no; branch-only files: 18; modified: 0 |
| no | QUARTERLY | claude/credo-quarterly-analysis-r7tbey | 2026-08-11 | Claude | folders: credo-q1fy27; on main: no; branch-only files: 19; modified: 0 |
| no | QUARTERLY | claude/d-dev-quarterly-analysis-jnyqb1 | 2026-08-05 | Claude | folders: d-dev-q1fy27; on main: no; branch-only files: 22; modified: 0 |
| no | QUARTERLY | claude/deccan-gold-concall-analysis-5eyww0 | 2026-08-12 | Claude | folders: deccangold-q1fy27; on main: no; branch-only files: 6; modified: 0 |
| no | QUARTERLY | claude/dhanbank-pipeline-run-bi3wv6 | 2026-07-29 | Claude | folders: dhanbank-2026-07-27,dhanbank-q1fy27; on main: no; branch-only files: 64; modified: 0 |
| no | QUARTERLY | claude/digitite-results-analysis-yek08v | 2026-07-28 | Claude | folders: digitide-q1fy27; on main: no; branch-only files: 65; modified: 0 |
| no | QUARTERLY | claude/digvi-quarterly-analysis-o97k0v | 2026-08-12 | Claude | folders: divgi-q1fy27; on main: no; branch-only files: 12; modified: 0 |
| no | QUARTERLY | claude/e2e-quarterly-analysis-j6j65r | 2026-07-23 | Claude | folders: e2e-q1fy27; on main: no; branch-only files: 26; modified: 0 |
| no | QUARTERLY | claude/ecos-mobility-quarterly-analysis-1gxkan | 2026-08-12 | Claude | folders: ecosmobility-q1fy27; on main: no; branch-only files: 109; modified: 0 |
| no | QUARTERLY | claude/emvdl-quarterly-analysis-1eikkc | 2026-08-11 | Claude | folders: emvdl-q1fy27; on main: no; branch-only files: 15; modified: 0 |
| no | QUARTERLY | claude/exicom-q1-fy27-analysis-0bxvcc | 2026-08-11 | Claude | folders: exicom-q1fy27; on main: no; branch-only files: 22; modified: 0 |
| no | QUARTERLY | claude/extra-light-quarterly-analysis-befw6c | 2026-07-25 | Claude | folders: stltech-q1fy27; on main: yes; branch-only files: 6; modified: 0 |
| no | QUARTERLY | claude/fedfina-call-analysis-ggpjgq | 2026-07-22 | Claude | folders: fedfina-q1fy27; on main: no; branch-only files: 7; modified: 0 |
| no | QUARTERLY | claude/g-limited-results-analysis-q4cm3w | 2026-08-06 | Claude | folders: gee-q1fy27; on main: no; branch-only files: 19; modified: 0 |
| no | QUARTERLY | claude/ganesha-quarterly-analysis-rsgtf3 | 2026-07-30 | Claude | folders: ganecos-q4fy26; on main: yes; branch-only files: 4; modified: 1 |
| no | QUARTERLY | claude/gargi-quarterly-analysis-11fbsc | 2026-08-01 | Claude | folders: gargi-q1fy27; on main: no; branch-only files: 13; modified: 0 |
| no | QUARTERLY | claude/ghv-infra-quarterly-analysis-z6m8wn | 2026-08-11 | Claude | folders: ghvinfra-q1fy27; on main: no; branch-only files: 7; modified: 0 |
| no | QUARTERLY | claude/gmdc-quarterly-analysis-c3vej5 | 2026-07-31 | Claude | folders: gmdc-q1fy27; on main: no; branch-only files: 7; modified: 0 |
| no | QUARTERLY | claude/gmm-pfaudler-quarterly-analysis-55jc3e | 2026-08-06 | Claude | folders: gmmpfaudler-q1fy27; on main: no; branch-only files: 14; modified: 0 |
| no | QUARTERLY | claude/goldium-q1-fy27-earnings-8csvi8 | 2026-08-11 | Claude | folders: goldium-q1fy27; on main: no; branch-only files: 6; modified: 0 |
| no | QUARTERLY | claude/hfca-quarterly-analysis-4a6fod | 2026-07-22 | Claude | folders: hfcl-q1fy27; on main: yes; branch-only files: 5; modified: 1 |
| no | QUARTERLY | claude/india-mart-quarterly-analysis-nujr2m | 2026-07-22 | Claude | folders: indiamart-q1fy27; on main: no; branch-only files: 22; modified: 0 |
| no | QUARTERLY | claude/jk-india-quarterly-analysis-xulrvt | 2026-08-12 | Claude | folders: jnkindia-q1fy27; on main: no; branch-only files: 23; modified: 0 |
| no | QUARTERLY | claude/k-solve-quarterly-analysis-23wdwl | 2026-07-23 | Claude | folders: ksolves-q1fy27; on main: no; branch-only files: 6; modified: 0 |
| no | QUARTERLY | claude/map-my-india-quarterly-analysis-43nbwc | 2026-08-04 | Claude | folders: mapmyindia-q1fy27; on main: no; branch-only files: 20; modified: 0 |
| no | QUARTERLY | claude/max-india-earnings-analysis-2pm9im | 2026-08-12 | Claude | folders: maxind-q1fy27; on main: no; branch-only files: 7; modified: 0 |
| no | QUARTERLY | claude/mcfos-quarterly-analysis-n1t1pq | 2026-08-12 | Claude | folders: mcfos-q1fy27; on main: no; branch-only files: 10; modified: 0 |
| no | QUARTERLY | claude/mtar-annual-reports-qo0c39 | 2026-07-30 | Claude | folders: mtar-q1fy27; on main: no; branch-only files: 26; modified: 0 |
| no | QUARTERLY | claude/nephro-plus-quarterly-analysis-vqj5xc | 2026-08-12 | Claude | folders: nephroplus-q1fy27; on main: no; branch-only files: 25; modified: 0 |
| no | QUARTERLY | claude/oswal-pumps-q1-analysis-si2lg8 | 2026-08-11 | Claude | folders: oswal-q1fy27; on main: no; branch-only files: 8; modified: 0 |
| no | QUARTERLY | claude/paushak-quarterly-analysis-1lg8ur | 2026-07-31 | Claude | folders: paushak-q1fy27; on main: no; branch-only files: 10; modified: 0 |
| no | QUARTERLY | claude/qpower-q1-fy27-notion-6lgxlt | 2026-08-11 | Claude | folders: qpower-q1fy27; on main: no; branch-only files: 7; modified: 0 |
| no | QUARTERLY | claude/quarterly-data-pattern-analysis-7vzvt2 | 2026-07-31 | Claude | folders: datapattns-q1fy27; on main: no; branch-only files: 21; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-01wssj | 2026-08-12 | Claude | folders: sharika-q1fy27; on main: no; branch-only files: 6; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-06y8qn | 2026-07-27 | Claude | folders: welcorp-q1fy27; on main: no; branch-only files: 18; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-0ffwkb | 2026-08-12 | Claude | folders: krn-q1fy27; on main: no; branch-only files: 8; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-324riy | 2026-08-13 | Claude | folders: utlsolar-q1fy27; on main: no; branch-only files: 15; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-3y7lxn | 2026-08-13 | Claude | folders: dssl-q1fy27; on main: no; branch-only files: 11; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-53w4to | 2026-08-12 | Claude | folders: 526717-q1fy27; on main: no; branch-only files: 21; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-7dqyyn | 2026-08-14 | Claude | folders: gaudiumivf-q1fy27; on main: no; branch-only files: 20; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-91a9t7 | 2026-08-13 | Claude | folders: scodatubes-q1fy27; on main: no; branch-only files: 11; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-9ef8ys | 2026-08-06 | Claude | folders: uniparts-q1fy27; on main: no; branch-only files: 15; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-ag4rkl | 2026-08-04 | Claude | folders: ganecos-q1fy27; on main: yes; branch-only files: 11; modified: 2 |
| no | QUARTERLY | claude/quarterly-results-analysis-b1d9jd | 2026-08-13 | Claude | folders: sammaancap-q1fy27; on main: no; branch-only files: 30; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-b66fgh | 2026-08-04 | Claude | folders: sambhv-q1fy27,samhi-q1fy27; on main: yes; branch-only files: 12; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-bjv3ft | 2026-08-13 | Claude | folders: finkurve-q1fy27; on main: no; branch-only files: 15; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-c8fsiv | 2026-08-14 | Claude | folders: asianene-q1fy27; on main: no; branch-only files: 15; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-d723ow | 2026-08-13 | Claude | folders: goclcorp-q1fy27; on main: no; branch-only files: 6; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-dwprvc | 2026-08-13 | Claude | folders: ipcl-q1fy27; on main: no; branch-only files: 27; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-h2f1ss | 2026-08-05 | Claude | folders: vaibhavgbl-q1fy27; on main: no; branch-only files: 15; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-h4n2ul | 2026-08-06 | Claude | folders: iks-q1fy27; on main: yes; branch-only files: 2; modified: 2 |
| no | QUARTERLY | claude/quarterly-results-analysis-i1ji43 | 2026-08-12 | Claude | folders: indiqube-q1fy27; on main: no; branch-only files: 25; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-ixhbmx | 2026-08-14 | Claude | folders: kernex-q1fy27; on main: no; branch-only files: 8; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-j2wrxj | 2026-08-05 | Claude | folders: rsystems-q2cy26; on main: no; branch-only files: 26; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-lft8iz | 2026-08-13 | Claude | folders: rathist-q1fy27; on main: no; branch-only files: 10; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-mk45d6 | 2026-08-12 | Claude | folders: kcpsugind-q1fy27; on main: no; branch-only files: 6; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-o83a25 | 2026-08-06 | Claude | folders: rptech-q1fy27; on main: yes; branch-only files: 2; modified: 2 |
| no | QUARTERLY | claude/quarterly-results-analysis-oxt7o0 | 2026-08-13 | Claude | folders: kecl-q1fy27; on main: no; branch-only files: 6; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-qhuohq | 2026-08-13 | Claude | folders: gvpil-q1fy27; on main: no; branch-only files: 7; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-qj2kqr | 2026-08-04 | Claude | folders: parkhosps-q1fy27; on main: yes; branch-only files: 4; modified: 3 |
| no | QUARTERLY | claude/quarterly-results-analysis-rnbvw5 | 2026-08-13 | Claude | folders: amagi-q1fy27; on main: no; branch-only files: 7; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-u9lgke | 2026-08-14 | Claude | folders: srm-q1fy27; on main: no; branch-only files: 9; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-analysis-vx8dc4 | 2026-08-06 | Claude | folders: pacedigitk-q1fy27; on main: no; branch-only files: 18; modified: 0 |
| no | QUARTERLY | claude/quarterly-results-protocol-dlltuf | 2026-08-06 | Claude | folders: paisalo-q1fy27; on main: no; branch-only files: 18; modified: 0 |
| no | QUARTERLY | claude/ram-ratna-quarterly-analysis-0161le | 2026-07-31 | Claude | folders: ramrat-q1fy27; on main: no; branch-only files: 15; modified: 0 |
| no | QUARTERLY | claude/raymond-realty-q1-fy27-h5wmo2 | 2026-08-11 | Claude | folders: raymondrealty-q1fy27; on main: no; branch-only files: 7; modified: 0 |
| no | QUARTERLY | claude/red-grain-quarterly-results-1xrd0f | 2026-08-06 | Claude | folders: rategain-q1fy27; on main: no; branch-only files: 19; modified: 0 |
| no | QUARTERLY | claude/route-mobile-quarterly-pkqpxv | 2026-07-25 | Claude | folders: route-q1fy27; on main: no; branch-only files: 22; modified: 0 |
| no | QUARTERLY | claude/run-pipeline-aye-adnmeu | 2026-07-23 | Claude | folders: aye-2026-07-22,aye-q1fy27; on main: no; branch-only files: 83; modified: 0 |
| no | QUARTERLY | claude/run-pipeline-indgn-6wej1t | 2026-08-06 | Claude | folders: indgn-q1fy27; on main: no; branch-only files: 25; modified: 0 |
| no | QUARTERLY | claude/sedemac-quarterly-analysis-4k2otx | 2026-07-29 | Claude | folders: sedemac-q1fy27; on main: no; branch-only files: 11; modified: 0 |
| no | QUARTERLY | claude/sesha-sai-analysis-t7sqgg | 2026-07-25 | Claude | folders: styl-q1fy27; on main: no; branch-only files: 15; modified: 0 |
| no | QUARTERLY | claude/sheela-quarterly-results-zxbbvj | 2026-08-04 | Claude | folders: sfl-q1fy27; on main: no; branch-only files: 17; modified: 0 |
| no | QUARTERLY | claude/shriram-properties-quarterly-8swem6 | 2026-08-12 | Claude | folders: sprop-q1fy27; on main: no; branch-only files: 39; modified: 0 |
| no | QUARTERLY | claude/sona-blw-ads-analysis-wn318h | 2026-07-30 | Claude | folders: sona-q1fy27; on main: yes; branch-only files: 0; modified: 3 |
| no | QUARTERLY | claude/southrest-quarterly-results-wo3ltt | 2026-07-22 | Claude | folders: southwest-q1fy27; on main: no; branch-only files: 16; modified: 0 |
| no | QUARTERLY | claude/sp-apparel-quarterly-analysis-q2eld6 | 2026-08-11 | Claude | folders: spapparel-q1fy27; on main: no; branch-only files: 9; modified: 0 |
| no | QUARTERLY | claude/spra-quarterly-results-analysis-ctlfwb | 2026-08-06 | Claude | folders: aris-q1fy27; on main: no; branch-only files: 18; modified: 0 |
| no | QUARTERLY | claude/sugs-lyod-results-analysis-sa8wi5 | 2026-07-29 | Claude | folders: sugslloyd-q1fy27; on main: no; branch-only files: 7; modified: 0 |
| no | QUARTERLY | claude/tejas-network-quarterly-analysis-4mzxz3 | 2026-07-28 | Claude | folders: tejasnet-q1fy27; on main: no; branch-only files: 27; modified: 0 |
| no | QUARTERLY | claude/transrail-quarterly-analysis-f7kqqf | 2026-08-06 | Claude | folders: transrail-q1fy27; on main: no; branch-only files: 11; modified: 0 |
| no | QUARTERLY | claude/unipart-quarterly-analysis-5ky0ug | 2026-08-11 | Claude | folders: uniabex-q1fy27; on main: no; branch-only files: 7; modified: 0 |
| no | QUARTERLY | claude/united-food-investor-analysis-fdzhmr | 2026-08-18 | Claude | folders: ufbl-q1fy27; on main: yes; branch-only files: 4; modified: 2 |
| no | QUARTERLY | claude/venus-pipes-q1-fy27-jtc505 | 2026-08-11 | Claude | folders: venuspipes-q1fy27; on main: no; branch-only files: 25; modified: 0 |
| no | QUARTERLY | claude/zeel-quarterly-analysis-9i2r1v | 2026-08-11 | Claude | folders: zeel-q1fy27; on main: no; branch-only files: 7; modified: 0 |
| no | RUN | claude/aartisurf-pipeline-run-3wqmjl | 2026-08-04 | Claude | folders: aartisurf-2026-08-04; on main: yes; branch-only files: 73; modified: 0 |
| no | RUN | claude/aartisurf-pipeline-run-811pku | 2026-08-04 | Claude | folders: aartisurf-2026-08-04; on main: yes; branch-only files: 35; modified: 6 |
| no | RUN | claude/aequs-step-one-42trpa | 2026-09-05 | Claude | folders: aequs-2026-09-05; on main: yes; branch-only files: 10; modified: 2 |
| no | RUN | claude/amazing-gauss-t7h354 | 2026-09-24 | Claude | folders: -; on main: no; branch-only files: 0; modified: 0 |
| no | RUN | claude/apexeco-pipeline-run-gkdm6t | 2026-07-10 | Claude | folders: apexeco-2026-07-10; on main: yes; branch-only files: 1; modified: 0 |
| no | RUN | claude/asianene-pipeline-run-1x1vxr | 2026-07-14 | Claude | folders: asianene-2026-07-13; on main: yes; branch-only files: 0; modified: 10 |
| no | RUN | claude/avana-pipeline-run-jq6rz4 | 2026-07-17 | Claude | folders: avana-2026-07-16; on main: yes; branch-only files: 44; modified: 0 |
| no | RUN | claude/birlacable-pipeline-4rln8o | 2026-08-20 | Claude | folders: birlacable-2026-08-20; on main: yes; branch-only files: 51; modified: 0 |
| no | RUN | claude/borana-2026-09-07-vpvzja | 2026-09-08 | Claude | folders: borana-2026-09-07; on main: yes; branch-only files: 91; modified: 0 |
| no | RUN | claude/brave-volta-gfcki3 | 2026-09-19 | Claude | folders: -; on main: no; branch-only files: 0; modified: 0 |
| no | RUN | claude/ceigall-runs-2026-09-06-67mi8o | 2026-09-06 | Claude | folders: ceigall-2026-09-06; on main: yes; branch-only files: 62; modified: 0 |
| no | RUN | claude/cmsinfo-spear-pass-9v2yyz | 2026-08-31 | Claude | folders: cmsinfo-2026-08-29; on main: yes; branch-only files: 16; modified: 3 |
| no | RUN | claude/company-analysis-five-firms-48nqeu | 2026-09-07 | Claude | folders: borana-2026-09-07,fratelli-2026-09-07; on main: yes; branch-only files: 6; modified: 0 |
| no | RUN | claude/company-financial-analysis-fy27-p359ze | 2026-09-28 | Claude | folders: -; on main: no; branch-only files: 0; modified: 0 |
| no | RUN | claude/company-shallow-analysis-lk6ddk | 2026-09-10 | Claude | folders: -; on main: no; branch-only files: 0; modified: 0 |
| no | RUN | claude/company-shallow-analysis-y3r9le | 2026-09-11 | Claude | folders: -; on main: no; branch-only files: 0; modified: 0 |
| no | RUN | claude/divgiitts-pipeline-run-9hokoy | 2026-08-30 | Claude | folders: divgiitts-2026-08-29; on main: yes; branch-only files: 15; modified: 5 |
| no | RUN | claude/dssl-pipeline-run-onx7hd | 2026-07-28 | Claude | folders: dssl-2026-07-27; on main: yes; branch-only files: 15; modified: 3 |
| no | RUN | claude/ebgng-pipeline-run-e7jis5 | 2026-07-13 | Claude | folders: ebgng-2026-07-12; on main: yes; branch-only files: 13; modified: 4 |
| no | RUN | claude/entero-pipeline-run-ndqp3v | 2026-07-28 | Claude | folders: entero-2026-07-27; on main: yes; branch-only files: 52; modified: 26 |
| no | RUN | claude/fabtech-pipeline-run-2ap5pp | 2026-08-05 | Claude | folders: fabtech-2026-08-04; on main: yes; branch-only files: 49; modified: 0 |
| no | RUN | claude/fedfina-pipeline-run-3mq2uj | 2026-07-16 | Claude | folders: fedfina-2026-07-15; on main: yes; branch-only files: 78; modified: 1 |
| no | RUN | claude/festive-bardeen-ne846x | 2026-07-11 | Claude | folders: akums-2026-07-10,karnika-2026-07-11; on main: yes; branch-only files: 1; modified: 6 |
| no | RUN | claude/fincables-pipeline-9mrge1 | 2026-08-12 | Claude | folders: fincables-2026-08-12; on main: yes; branch-only files: 38; modified: 1 |
| no | RUN | claude/fluidomat-pipeline-ngoubg | 2026-07-17 | Claude | folders: fluidomat-2026-07-16; on main: yes; branch-only files: 37; modified: 0 |
| no | RUN | claude/fratelli-2026-09-07-71euee | 2026-09-08 | Claude | folders: fratelli-2026-09-07; on main: yes; branch-only files: 43; modified: 0 |
| no | RUN | claude/friendly-sagan-wnl8zv | 2026-09-18 | Claude | folders: -; on main: no; branch-only files: 0; modified: 0 |
| no | RUN | claude/fttcp-autonomous-draft-j0h1jl | 2026-07-11 | Claude | folders: -; on main: no; branch-only files: 0; modified: 0 |
| no | RUN | claude/gaudiumivf-pipeline-tvrgn0 | 2026-07-17 | Claude | folders: gaudiumivf-2026-07-16; on main: yes; branch-only files: 49; modified: 0 |
| no | RUN | claude/gifted-cerf-tj5ol3 | 2026-09-12 | Claude | folders: -; on main: no; branch-only files: 0; modified: 0 |
| no | RUN | claude/gsmfoils-pipeline-nc36ie | 2026-07-24 | Claude | folders: gsmfoils-2026-07-24; on main: yes; branch-only files: 77; modified: 0 |
| no | RUN | claude/indiaglyco-docreview-run | 2026-09-02 | Claude | folders: indiaglyco-2026-09-02; on main: no; branch-only files: 20; modified: 0 |
| no | RUN | claude/indiaglyco-pipeline-run-nv2zsl | 2026-08-25 | Claude | folders: indiaglyco-2026-08-24; on main: yes; branch-only files: 18; modified: 3 |
| no | RUN | claude/indoborax-investment-thesis-curszr | 2026-08-30 | Claude | folders: indoborax-2026-08-30,kronox-2026-08-30; on main: yes; branch-only files: 4; modified: 0 |
| no | RUN | claude/jaykay-corpus-extraction-vkjw6a | 2026-08-26 | Claude | folders: jaykay-2026-08-26; on main: no; branch-only files: 3; modified: 0 |
| no | RUN | claude/kronox-lab-sciences-bjc54f | 2026-08-30 | Claude | folders: indoborax-2026-08-30,kronox-2026-08-30; on main: yes; branch-only files: 4; modified: 0 |
| no | RUN | claude/laxmiindia-pipeline-run-apfp2a | 2026-07-22 | Claude | folders: laxmiindia-2026-07-22; on main: yes; branch-only files: 36; modified: 0 |
| no | RUN | claude/macpower-pipeline-g9ouq4 | 2026-07-31 | Claude | folders: macpower-2026-07-30; on main: yes; branch-only files: 52; modified: 0 |
| no | RUN | claude/mapmyindia-pipeline-run-qj742m | 2026-07-19 | Claude | folders: mapmyindia-2026-07-13; on main: yes; branch-only files: 1; modified: 0 |
| no | RUN | claude/maxind-pipeline-run-63lhar | 2026-07-24 | Claude | folders: maxind-2026-07-24; on main: yes; branch-only files: 33; modified: 0 |
| no | RUN | claude/menonbe-pipeline-run-bs4dq5 | 2026-07-17 | Claude | folders: menonbe-2026-07-16; on main: yes; branch-only files: 80; modified: 0 |
| no | RUN | claude/millworks-pipeline-run-xl204h | 2026-08-22 | Claude | folders: millworks-2026-08-22; on main: yes; branch-only files: 26; modified: 18 |
| no | RUN | claude/modisonltd-pipeline-run-e5lytf | 2026-09-09 | Claude | folders: modisonltd-2026-09-03; on main: yes; branch-only files: 61; modified: 0 |
| no | RUN | claude/nrail-pipeline-run-k3gtja | 2026-07-23 | Claude | folders: nrail-2026-07-22; on main: yes; branch-only files: 35; modified: 0 |
| no | RUN | claude/obscp-pipeline-run-vbusqd | 2026-07-13 | Claude | folders: obscp-2026-07-12; on main: yes; branch-only files: 0; modified: 3 |
| no | RUN | claude/orchpharma-2026-09-06-runs-bx6lcr | 2026-09-28 | Claude | folders: orchpharma-2026-09-06; on main: yes; branch-only files: 1; modified: 0 |
| no | RUN | claude/pi-value-annual-report-4pq7qr | 2026-07-27 | Claude | folders: aimtron-2026-07-12; on main: yes; branch-only files: 1; modified: 0 |
| no | RUN | claude/pipeline-526717-n61a68 | 2026-07-16 | Claude | folders: 526717-2026-07-15; on main: yes; branch-only files: 52; modified: 0 |
| no | RUN | claude/pipeline-544332-upvab5 | 2026-08-04 | Claude | folders: 544332-2026-08-04; on main: yes; branch-only files: 10; modified: 0 |
| no | RUN | claude/pipeline-544516-8t948a | 2026-07-16 | Claude | folders: 544516-2026-07-15; on main: yes; branch-only files: 57; modified: 0 |
| no | RUN | claude/pipeline-544555-o9qto2 | 2026-07-30 | Claude | folders: 544555-2026-07-30; on main: yes; branch-only files: 42; modified: 0 |
| no | RUN | claude/pipeline-run-aequs-171qf0 | 2026-09-05 | Claude | folders: aequs-2026-09-05; on main: yes; branch-only files: 53; modified: 0 |
| no | RUN | claude/pipeline-run-kabraextru-t0dwrv | 2026-09-09 | Claude | folders: kabraextru-2026-09-05; on main: yes; branch-only files: 67; modified: 0 |
| no | RUN | claude/pipeline-run-pittieng-1u15zn | 2026-09-08 | Claude | folders: pittieng-2026-09-05; on main: yes; branch-only files: 61; modified: 0 |
| no | RUN | claude/pipeline-run-shharich-q9d0gj | 2026-09-09 | Claude | folders: shharich-2026-09-05; on main: yes; branch-only files: 47; modified: 0 |
| no | RUN | claude/pipeline-run-visakaind-41w19l | 2026-09-05 | Claude | folders: visakaind-2026-09-05; on main: yes; branch-only files: 49; modified: 0 |
| no | RUN | claude/presentation-analysis-3onxgk | 2026-09-07 | Claude | folders: workmates-2026-09-07-presentation; on main: no; branch-only files: 1; modified: 0 |
| no | RUN | claude/presentation-analysis-hw7bol | 2026-09-07 | Claude | folders: vividel-2026-09-07; on main: no; branch-only files: 2; modified: 0 |
| no | RUN | claude/ramrat-pipeline-run-e5xukv | 2026-07-30 | Claude | folders: ramrat-2026-07-29; on main: yes; branch-only files: 50; modified: 0 |
| no | RUN | claude/rathist-pipeline-ml8nfh | 2026-07-20 | Claude | folders: rathist-2026-07-20; on main: yes; branch-only files: 38; modified: 0 |
| no | RUN | claude/run-diffnkg-pipeline-8n6qp1 | 2026-09-07 | Claude | folders: diffnkg-2026-09-05; on main: yes; branch-only files: 41; modified: 0 |
| no | RUN | claude/run-jitfinfra-pipeline-iobgub | 2026-08-12 | Claude | folders: jitfinfra-2026-08-12; on main: yes; branch-only files: 35; modified: 0 |
| no | RUN | claude/run-pipeline-ddevplstik-405lmq | 2026-07-24 | Claude | folders: ddevplstik-2026-07-23; on main: yes; branch-only files: 66; modified: 0 |
| no | RUN | claude/run-pipeline-mpsltd-nmmtdo | 2026-09-04 | Claude | folders: mpsltd-2026-09-03; on main: yes; branch-only files: 40; modified: 0 |
| no | RUN | claude/runs-cyientdlm-2026-09-06-w70pyd | 2026-09-06 | Claude | folders: cyientdlm-2026-09-06; on main: yes; branch-only files: 62; modified: 0 |
| no | RUN | claude/runs-ina-2026-09-06-kav2sw | 2026-09-11 | Claude | folders: ina-2026-09-06; on main: yes; branch-only files: 65; modified: 0 |
| no | RUN | claude/shallow-analysis-companies-zx79xm | 2026-09-08 | Claude | folders: -; on main: no; branch-only files: 0; modified: 0 |
| no | RUN | claude/sicallog-pipeline-pwftth | 2026-07-29 | Claude | folders: sicallog-2026-07-28; on main: yes; branch-only files: 66; modified: 0 |
| no | RUN | claude/spear-override-2026-09-02-oecn2r | 2026-09-04 | Claude | folders: venusrem-2026-09-02; on main: yes; branch-only files: 3; modified: 0 |
| no | RUN | claude/tatva-pipeline-run-kl58kw | 2026-07-21 | Claude | folders: tatva-2026-07-12; on main: yes; branch-only files: 1; modified: 12 |
| no | RUN | claude/transcript-indigene-analysis-5zmus0 | 2026-08-17 | Claude | folders: indgn-agm-2026-08-13; on main: no; branch-only files: 4; modified: 0 |
| no | RUN | claude/trusting-einstein-qap7vj | 2026-09-15 | Claude | folders: balajitele-2026-09-15,emudhra-2026-09-15,grpltd-2026-09-15; on main: no; branch-only files: 3; modified: 0 |
| no | RUN | claude/ufbl-pipeline-run-8age4c | 2026-08-06 | Claude | folders: ufbl-2026-08-05; on main: yes; branch-only files: 0; modified: 0 |
| no | RUN | claude/vilas-equity-research-tuuvfi | 2026-09-03 | Claude | folders: vilas-2026-09-03; on main: yes; branch-only files: 16; modified: 2 |
| no | RUN | claude/voepl-pipeline-run-ppnypi | 2026-07-18 | Claude | folders: voepl-2026-07-18; on main: yes; branch-only files: 12; modified: 5 |
| no | RUN | claude/yasho-industries-step-one-iuo5ii | 2026-09-05 | Claude | folders: yasho-2026-09-05; on main: yes; branch-only files: 40; modified: 1 |
| no | RUN | claude/zen-cannon-f5qm0s | 2026-09-17 | Claude | folders: -; on main: no; branch-only files: 0; modified: 0 |
| no | RUN | extract/asianene-fy26-halt1 | 2026-09-03 | Claude | folders: asianene-2026-07-13; on main: yes; branch-only files: 0; modified: 0 |
| no | RUN | run/avience-2026-09-26 | 2026-09-26 | sumit-604 | folders: avience-2026-09-26; on main: no; branch-only files: 109; modified: 0 |
| no | RUN | run/awfis-2026-09-19 | 2026-09-19 | sumit-604 | folders: awfis-2026-09-19; on main: no; branch-only files: 176; modified: 0 |
| no | RUN | run/capillary-2026-09-19 | 2026-09-19 | sumit-604 | folders: capillary-2026-09-19; on main: no; branch-only files: 213; modified: 0 |
| no | RUN | run/emudhra-2026-09-19 | 2026-09-19 | sumit-604 | folders: emudhra-2026-09-19; on main: no; branch-only files: 181; modified: 0 |
| no | RUN | run/fabtech-2026-09-26 | 2026-09-26 | sumit-604 | folders: fabtech-2026-09-26; on main: no; branch-only files: 203; modified: 0 |
| no | RUN | run/goodluck-2026-09-19 | 2026-09-19 | sumit-604 | folders: goodluck-2026-09-19; on main: no; branch-only files: 245; modified: 0 |
| no | RUN | run/iex-2026-09-08 | 2026-09-19 | sumit-604 | folders: iex-2026-09-08; on main: no; branch-only files: 123; modified: 0 |
| no | RUN | run/iolcp-2026-09-19 | 2026-09-19 | sumit-604 | folders: iolcp-2026-09-19; on main: no; branch-only files: 212; modified: 0 |
| no | RUN | run/kissht-2026-09-19 | 2026-10-03 | sumit-604 | folders: kissht-2026-09-19; on main: no; branch-only files: 271; modified: 0 |
| no | RUN | run/kross-2026-09-27 | 2026-09-27 | sumit-604 | folders: kross-2026-09-27; on main: no; branch-only files: 160; modified: 0 |
| no | RUN | run/qmsmedi-2026-09-26 | 2026-09-26 | sumit-604 | folders: qmsmedi-2026-09-26; on main: no; branch-only files: 242; modified: 0 |
| no | RUN | run/qualitek-2026-09-26 | 2026-09-26 | sumit-604 | folders: qualitek-2026-09-26; on main: no; branch-only files: 198; modified: 0 |
| no | RUN | run/shareindia-2026-09-19 | 2026-09-19 | sumit-604 | folders: shareindia-2026-09-19; on main: no; branch-only files: 348; modified: 0 |
| no | RUN | run/sswl-2026-09-19 | 2026-09-19 | sumit-604 | folders: sswl-2026-09-19; on main: no; branch-only files: 204; modified: 0 |
| no | RUN | run/susan-2026-09-19 | 2026-09-29 | sumit-604 | folders: susan-2026-09-19; on main: no; branch-only files: 135; modified: 0 |
| no | RUN | run/taaltech-2026-09-10 | 2026-09-21 | sumit-604 | folders: taaltech-2026-09-10; on main: yes; branch-only files: 1; modified: 1 |
| no | RUN | run/titanbio-phase1-2026-09-16 | 2026-09-16 | sumit-604 | folders: titanbio-2026-09-10; on main: yes; branch-only files: 35; modified: 2 |
| no | RUN | run/tll-2026-09-26 | 2026-09-26 | sumit-604 | folders: tll-2026-09-26; on main: no; branch-only files: 227; modified: 0 |
| no | RUN | run/totem-fttcp-2026-09-16b | 2026-09-16 | sumit-604 | folders: totem-2026-09-09; on main: yes; branch-only files: 2; modified: 0 |
| no | RUN | run/trualt-2026-09-18 | 2026-10-02 | sumit-604 | folders: trualt-2026-09-18; on main: no; branch-only files: 224; modified: 0 |
| no | RUN | run/yashhv-2026-09-26 | 2026-09-26 | sumit-604 | folders: yashhv-2026-09-26; on main: no; branch-only files: 278; modified: 0 |
| yes | FRAMEWORK | claude/claudemd-team-workflow-note-a3wcfe | 2026-08-24 | Claude |  |
| yes | FRAMEWORK | claude/delta-aware-refresh-runs-edf0w3 | 2026-07-10 | Claude |  |
| yes | FRAMEWORK | claude/document-review-token-fix-ump2n4 | 2026-09-02 | Claude |  |
| yes | FRAMEWORK | claude/filename-collision-run-folders-7s4lgk | 2026-07-11 | Claude |  |
| yes | FRAMEWORK | claude/fttcp-deliberation-command-id3dgh | 2026-07-10 | Claude |  |
| yes | FRAMEWORK | claude/fttcp-handoff-dossier-xrqfwt | 2026-07-10 | Claude |  |
| yes | FRAMEWORK | claude/fttcp-runs-permagnet-tnfysa | 2026-08-23 | Claude |  |
| yes | FRAMEWORK | claude/growth-symmetry-amendment-26-fzh816 | 2026-09-08 | Claude |  |
| yes | FRAMEWORK | claude/halt1-understanding-dossier-vosrgg | 2026-08-23 | Claude |  |
| yes | FRAMEWORK | claude/inflection-pipeline-setup-izdned | 2026-07-09 | Claude |  |
| yes | FRAMEWORK | claude/lessons-framework-amendments-maninds-koqpsq | 2026-08-25 | Claude |  |
| yes | FRAMEWORK | claude/merge-framework-versions-h02mnx | 2026-08-19 | Claude |  |
| yes | FRAMEWORK | claude/pipeline-token-optimization-co1857 | 2026-08-18 | Claude |  |
| yes | FRAMEWORK | claude/section-1b-amendments-v3-9-rzlhwo | 2026-09-07 | Claude |  |
| yes | FRAMEWORK | claude/section1b-relative-crosscheck-1c | 2026-08-26 | Claude |  |
| yes | FRAMEWORK | claude/spear-gate-framework-c7bjgd | 2026-08-29 | Claude |  |
| yes | FRAMEWORK | claude/team-workflow-v2-analysis-pn1u7j | 2026-08-27 | Claude |  |
| yes | FRAMEWORK | claude/user-memory-file-setup-5mqpmx | 2026-08-21 | Claude |  |
| yes | FRAMEWORK | extract/cleanmax-halt1-01 | 2026-09-02 | Claude |  |
| yes | FRAMEWORK | fix/collector-and-preflight | 2026-09-16 | sumit-604 |  |
| yes | FRAMEWORK | fix/stage0-gates-and-provenance | 2026-09-16 | sumit-604 |  |
| yes | FRAMEWORK | fix/verifier-calibration | 2026-09-16 | sumit-604 |  |
| yes | FRAMEWORK | framework/amendment-19-fv-cagr | 2026-08-23 | Claude |  |
| yes | FRAMEWORK | framework/model-5-5 | 2026-10-02 | sumit-604 |  |
| yes | FRAMEWORK | framework/v38-exit-symmetry | 2026-08-23 | Claude |  |
| yes | FRAMEWORK | lessons/name-pr-167 | 2026-09-16 | sumit-604 |  |
| yes | FRAMEWORK | memory/compost-2026-09-16 | 2026-09-16 | sumit-604 |  |
| yes | FRAMEWORK | prompt-audit-fixes | 2026-09-15 | sumit-604 |  |
| yes | FRAMEWORK | prompt/lessons-preread-closeout | 2026-09-16 | sumit-604 |  |
| yes | FRAMEWORK | prompt/stage11-skill-preload | 2026-09-15 | sumit-604 |  |
| yes | FRAMEWORK | run/totem-fttcp-2026-09-16 | 2026-09-16 | sumit-604 |  |
| yes | OTHER | (local) main | 2026-10-02 | sumit-604 |  |
| yes | OTHER | claude/cleanmax-equity-research-v8tes6 | 2026-09-03 | Claude |  |
| yes | OTHER | claude/cmsinfo-prior-year-ars | 2026-08-30 | sumit-604 |  |
| yes | OTHER | claude/operator-voice-ste | 2026-08-19 | Claude |  |
| yes | OTHER | claude/pillar-3-entry-rules-l278il | 2026-07-11 | Claude |  |
| yes | OTHER | claude/refine-protocol-v1-eilc5g | 2026-07-19 | Claude |  |
| yes | OTHER | claude/relative-valuation-cross-check-f3lgaq | 2026-08-26 | Claude |  |
| yes | OTHER | claude/section-1b-v3-9-consumption-wiring | 2026-09-08 | Claude |  |
| yes | OTHER | claude/stage-0-research-gitkeep-k7prfg | 2026-08-25 | Claude |  |
| yes | OTHER | claude/upbeat-carson-a9mou7 | 2026-09-21 | Claude |  |
| yes | OTHER | extract/cleanmax-role1-02 | 2026-09-03 | Claude |  |
| yes | OTHER | main | 2026-10-02 | sumit-604 |  |
| yes | OTHER | skill/section-1b | 2026-09-15 | sumit-604 |  |
| yes | QUARTERLY | claude/atlanta-electric-quarterly-tlhdye | 2026-07-22 | Claude |  |
| yes | QUARTERLY | claude/folder-inputs-no-concall-y19ndm | 2026-07-09 | Claude |  |
| yes | QUARTERLY | claude/maninds-corppres-2026-09-quarterly | 2026-09-01 | Claude |  |
| yes | QUARTERLY | claude/quarterly-results-analysis-d4p3lt | 2026-08-03 | Claude |  |
| yes | QUARTERLY | claude/spra-quarterly-results-analysis-w8v26k | 2026-08-06 | Claude |  |
| yes | RUN | claude/aimtron-pipeline-run-5ws1rt | 2026-07-14 | Claude |  |
| yes | RUN | claude/amagi-pipeline-run-a8dnwj | 2026-07-13 | Claude |  |
| yes | RUN | claude/aurum-pipeline-run-hsfb25 | 2026-07-15 | Claude |  |
| yes | RUN | claude/azad-pipeline-run-2wm49f | 2026-07-12 | sumit-604 |  |
| yes | RUN | claude/kcpsugind-pipeline-run-6sp4j3 | 2026-07-22 | Claude |  |
| yes | RUN | claude/northarc-pipeline-run-5psvxt | 2026-07-12 | Claude |  |
| yes | RUN | claude/pipeline-graceful-degradation-x23ex2 | 2026-07-09 | Claude |  |
| yes | RUN | claude/pipeline-run-entero-pchzpu | 2026-08-30 | sumit-604 |  |
| yes | RUN | claude/pipeline-run-smruthi-tdloc4 | 2026-07-09 | Claude |  |
| yes | RUN | claude/pipeline-stage-0-empty-folders-rfslzv | 2026-07-10 | Claude |  |
| yes | RUN | claude/prizor-pipeline-run-lzsz8c | 2026-07-12 | sumit-604 |  |
| yes | RUN | claude/run-jublcpl-pipeline-kyh0rr | 2026-08-21 | Claude |  |
| yes | RUN | claude/run-maninds-2026-08-21 | 2026-08-26 | Claude |  |
| yes | RUN | claude/run-millworks-pipeline-cmygjn | 2026-08-25 | sumit-604 |  |
| yes | RUN | claude/run-pipeline-karnika-vq0a0k | 2026-07-11 | sumit-604 |  |
| yes | RUN | claude/synthesis-pipeline-specs-yrq07e | 2026-07-10 | Claude |  |
| yes | RUN | claude/systango-pipeline-run-a82gb8 | 2026-08-30 | Claude |  |
| yes | RUN | claude/three-phase-pipeline-restructure-8noaqc | 2026-07-10 | sumit-604 |  |
| yes | RUN | claude/ufbl-pipeline-run-lt3u5t | 2026-08-18 | Claude |  |
| yes | RUN | claude/vinyas-investment-thesis-dywsg0 | 2026-09-03 | Claude |  |
| yes | RUN | claude/zaggle-pipeline-run-rist4h | 2026-07-28 | sumit-604 |  |
| yes | RUN | run/aequs-2026-09-05 | 2026-09-05 | sumit-604 |  |
| yes | RUN | run/kabraextru-2026-09-05 | 2026-09-05 | sumit-604 |  |
| yes | RUN | run/pittieng-2026-09-05 | 2026-09-05 | sumit-604 |  |
| yes | RUN | run/shharich-2026-09-05 | 2026-09-05 | sumit-604 |  |
| yes | RUN | run/syngene-2026-09-15 | 2026-09-28 | sumit-604 |  |
| yes | RUN | run/titanbio-2026-09-10 | 2026-09-10 | sumit-604 |  |
| yes | RUN | run/totem-2026-09-09 | 2026-09-09 | sumit-604 |  |
| yes | RUN | run/visakaind-2026-09-05 | 2026-09-05 | sumit-604 |  |
| yes | RUN | thesis/cleanmax-role2-role3 | 2026-09-04 | Claude |  |

## Unmerged FRAMEWORK branches: per-change classification

Classes: IN MAIN (same substance on main), NOT IN MAIN (absent, never replaced), CONFLICTS (main rewrote the same place differently; usually superseded). Excluded: `framework/oct-2026-model-update` (PR #178) and `claude/inflection-opus-5.5-audit-102xpl` (this audit's working branch).

Note on three branches the October summary called stranded: `framework/amendment-19-fv-cagr`, `framework/v38-exit-symmetry` and `claude/claudemd-team-workflow-note` are MERGED into main. The earlier call came from the shallow clone.

### Autocompact threshold

- `claude/auto-compact-threshold-lcb3a2`: `.claude/settings.json` sets `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` = 75 (written for a 200k window, about 150k tokens).
- `main`: `.claude/settings.json` sets no autocompact value.
- Live: this cloud session runs with `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80` from the environment configuration, not from the repo.

### origin/claude/auto-compact-threshold-lcb3a2  (tip 109b3479, 2026-07-25, merge-base 84b2f546)
- Purpose: pin auto-compact at 75% in project settings, harden the pipeline against mid-run compaction (resume from disk, fttcp overrides to disk), split LESSONS into archive + LESSONS_ACTIVE.md head, compost promotions (stage-0 PDF pre-extraction, YAML block in report file, Verifier A anti-degradation).
- Settings check: branch `.claude/settings.json` sets `"env": {"CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "75"}` (commit eb7d98c1: "~150k tokens on the standard 200k window"). origin/main `.claude/settings.json` carries only a SessionStart hook (`$CLAUDE_PROJECT_DIR/.claude/hooks/session-start.sh`); it sets NO env and no CLAUDE_AUTOCOMPACT_PCT_OVERRIDE. `git grep AUTOCOMPACT origin/main` returns nothing anywhere in the repo.

| file | class | note |
|---|---|---|
| .claude/settings.json | NOT IN MAIN | env CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=75; main has the file but only the hook block |
| CLAUDE.md (MEMORY, STRUCTURE) | CONFLICTS | branch: LESSONS.md = archive, LESSONS_ACTIVE.md = regenerated head. Main: LESSONS.md = ACTIVE lean file (<1,500 tokens), LESSONS_ARCHIVE.md = full history. Main superseded with an inverted naming |
| .claude/commands/compost.md | CONFLICTS | "regenerate LESSONS_ACTIVE.md" step; main has no LESSONS_ACTIVE.md (same supersession) |
| .claude/commands/fttcp.md (LOAD ORDER, close step) | CONFLICTS | reads/regenerates LESSONS_ACTIVE.md; superseded by main's LESSONS.md/LESSONS_ARCHIVE.md split |
| .claude/commands/fttcp.md (override record) | NOT IN MAIN | branch appends each override to outputs/final/fttcp-deliberation.md as it is made; main still says "Record every override the moment it happens" with no disk write, and writes the file only at sign-off |
| prompts/00-orchestrator.md (Section 3 block schema) | IN MAIN | branch: block appended at end of report file, extracted from file. Main: block written to outputs/blocks/<stage>.yaml and read from that file, reply is a copy. Same goal (block survives compaction), different mechanism; main's is later |
| prompts/00-orchestrator.md (new 7A RESUME FROM DISK) | NOT IN MAIN | main has no resume/re-derive-from-disk rule; only per-stage re-invoke checks in run-pipeline.md |
| .claude/agents/* (18 stage/verifier files, YAML-at-end wording) | IN MAIN | every main agent file now carries "ALSO write that same YAML block ... to the block path"; same substance via main's mechanism |
| .claude/agents/verifier-a-numerical.md (never run degraded bullet) | IN MAIN | main 12-verifiers rules 5a/5b/7 + run-pipeline "Verifiers must never skip source verification" cover it |
| prompts/12-verifiers-pipeline.md (Verifier A rules 8-9) | IN MAIN | rule 9 (no false CRITICALs, MATCH never a finding, transcribed anomaly is company fact, self-check) = main 5a/5b. Rule 8 residual: the explicit sentence "cross-report consistency is NOT source verification and must never, on its own, produce a finding" has no exact main twin; main rule 7 and run-pipeline TOOLING GATE carry the intent |
| .claude/commands/run-pipeline.md (PDF PRE-EXTRACTION) | IN MAIN | main TOOLING GATE: pypdf + cffi force-reinstall, page-marked .txt, ".txt path to every stage and verifier", "Pre-extracted text is the reliable default on any large corpus", record in B00 |
| .claude/commands/finalize.md (PDF PRE-EXTRACTION) | CONFLICTS (minor) | main finalize keeps the old short "PDF READING RESILIENCE" text; the substance lives in main's run-pipeline TOOLING GATE, and phase 3 reuses the phase-1 corpus. Main wins |

Exact lines, NOT IN MAIN / CONFLICTS:

1. .claude/settings.json (NOT IN MAIN)
```
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "env": {
    "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "75"
  }
}
```
Main: `{"hooks": {"SessionStart": [ ... session-start.sh ... ]}}`, no env.
Recommendation: operator choice. If kept, merge the env key into main's file beside the hook block (never replace the file). The 75% / 150k rationale was written for a 200k window; re-check it against the current session window before adopting.

2. prompts/00-orchestrator.md new section 7A (NOT IN MAIN)
```
## 7A. RESUME FROM DISK AFTER COMPACTION OR RESET
The authoritative state of a run is the files on disk, never this
conversation. ...
On ANY resume — after a compaction, a container reset, or re-invoking the
command on an in-progress run — re-derive progress from disk before
launching another stage:
- List `outputs/blocks/` to see which stages already have a block.
- For each, confirm its report in `outputs/reports/` ends with a closed
  ```yaml block (tail it). A stage whose block is missing, or whose report
  has no closed block, is NOT done: re-run it, do not trust memory.
- Never assume a number, a determination, or an operator ruling from
  conversation memory; read it back from the block, the report, or the
  deliberation file. If memory and the file disagree, the file wins.
```
Recommendation: recover, reworded to main's mechanism (check `outputs/blocks/<stage>.yaml` exists and parses, not "report ends with a closed block").

3. .claude/commands/fttcp.md override record (NOT IN MAIN)
```
Record every override the moment it happens, to DISK and not only in this
conversation: append it to outputs/final/fttcp-deliberation.md as it is made
... The deliberation file accretes during
review and is finalized at sign-off (below). Persisting each override as it
happens means a mid-deliberation context compaction cannot lose an operator
ruling.
...
When the operator signs off, finalize outputs/final/fttcp-deliberation.md
(it already exists if any override was recorded during review; complete and
reconcile it now).
```
Main (same place): "Record every override the moment it happens: what the draft said, what the operator ruled, and the operator's stated reasoning ... AND the default-track sensitivity ..." and "When the operator signs off, write outputs/final/fttcp-deliberation.md."
Recommendation: recover the to-disk clause, keep main's default-track sensitivity text.

4. LESSONS_ACTIVE.md split (CONFLICTS: CLAUDE.md, compost.md, fttcp.md)
```
Operational memory is split: LESSONS.md is the full permanent archive;
LESSONS_ACTIVE.md is a lean regenerated head (RECURRING PATTERNS + PROMOTED
TO LAW + the ~10 most recent entries, ~5k tokens).
```
Main: "read the ACTIVE LESSONS.md at start (the lean working memory, hard budget under 1,500 tokens ...). The full dated run history lives in LESSONS_ARCHIVE.md (never deleted)".
Recommendation: discard (superseded).

5. finalize.md PDF PRE-EXTRACTION (CONFLICTS, minor): branch replaces "PDF READING RESILIENCE: at session start, verify PDF text extraction works by test-reading one inputs/ PDF; run pip install pypdf if it is needed." with the 4-step `inputs/_textcache/` block. Main keeps the short text. Recommendation: main wins (the rule is in main's run-pipeline TOOLING GATE).

- Branch verdict: NEEDS OPERATOR CHOICE (CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=75, absent from main) + RECOVER (orchestrator 7A resume-from-disk rule; fttcp override-to-disk clause). Rest IN MAIN or superseded.

### origin/claude/gmg-electronics-analysis-0owflj  (tip 7a85b514, 2026-07-31, merge-base bf223fc1)
- Purpose: EBGNG Q1 FY27 quarterly run, plus prompt edits: a lone-concall FAST PATH for /run-quarterly and a mandatory three-part OPERATOR BRIEF on quarterly, phase 1 and phase 3.

| file | class | note |
|---|---|---|
| .claude/commands/run-quarterly.md (FAST PATH) | NOT IN MAIN | main has no lone-concall path; main's only scoped path is DOCUMENT REVIEW (presentation / press release) |
| .claude/commands/run-quarterly.md (4.5 OPERATOR BRIEF) | CONFLICTS | main: A4 writes a 4-part PLAIN-LANGUAGE BRIEF as the FINAL section; branch: orchestrator writes a 3-part brief inline as the executive HEADER |
| prompts/quarterly-00-orchestrator.md (FAST PATH section + SEQUENCE pointer) | NOT IN MAIN | same as above |
| prompts/quarterly-00-orchestrator.md (OPERATOR BRIEF spec, steps 6-8) | CONFLICTS | main steps: A4 PLAIN-LANGUAGE BRIEF, saved at the end of the review, surfaced in chat |
| .claude/commands/run-pipeline.md (operator-brief.md in phase 1) | CONFLICTS | main phase 1 prints 09b-understanding-dossier.md first (it carries a 14-15 point plain-language summary) and business-narrative.md opens with the BUSINESS UNDERSTANDING NARRATIVE |
| .claude/commands/finalize.md (operator-brief.md in phase 3) | CONFLICTS | main: BUSINESS UNDERSTANDING NARRATIVE (five questions, 12-18 sentences) first, before the verdict card, also in the Notion payload |
| prompts/13-synthesis-pipeline.md (DELIVERABLE 0) | CONFLICTS | same; main's shared BUSINESS-UNDERSTANDING-NARRATIVE-SPEC v1 occupies that slot |

Exact lines:

1. FAST PATH (NOT IN MAIN), prompts/quarterly-00-orchestrator.md
```
## FAST PATH — STANDALONE CONCALL TRANSCRIPT (default for a lone concall)
When the run is a SINGLE conference-call transcript and nothing else ...
do NOT spawn five separate agents.
- The ORCHESTRATOR performs A1 + A2 + A3 + A4 itself, inline, and writes the
  SAME named `work/` artifacts ... Every gate is still
  self-enforced and recorded ...
- Then spawn EXACTLY ONE agent: A5 (quarterly-a5-adversary), fresh context,
  task message carrying ONLY the A4 review, the A1 extract, and the A2 ledger.
This fast path is ONLY for a lone concall. The moment a run includes a Reg 33
results filing, an investor presentation, OR more than one document, revert to
the full five-agent per-document chain below
```
run-quarterly.md mirror: "FAST PATH (default for a lone concall): if `--docs` is a SINGLE `concall` transcript and nothing else, do NOT spawn five agents ... spawns ONLY the A5 adversary".
Recommendation: operator choice. It keeps A5 independent, but it collapses enumeration-before-interpretation into the maker's context, and main's CLAUDE.md DISPATCH now routes A1 to Sonnet low and A2 to Sonnet medium, so the cost case is weaker than when written.

2. OPERATOR BRIEF (CONFLICTS), prompts/quarterly-00-orchestrator.md / 13-synthesis-pipeline.md
```
1. SUMMARY (10 to 12 lines) ...
2. SECTOR AND COMPETITIVE INTELLIGENCE (6 to 7 lines) ...
3. BUSINESS MODEL, WHAT IS UNIQUE (5 to 6 lines) ...
The orchestrator writes this INLINE ... Write it as the executive header of
`work/review_<ticker>_<quarter>.md`
```
Main (run-quarterly.md section 2): "MANDATORY on every run — the PLAIN-LANGUAGE BRIEF as the final section: a 10-20 line plain summary narrative plus SECTOR intelligence, BUSINESS-MODEL intelligence, and COMPETITION intelligence (provenance-labelled ...)"; Document_Review_Protocol_v1_1 step 11 sets 200-400 words and five-tier provenance. Main (13-synthesis): "## BUSINESS UNDERSTANDING NARRATIVE (mandatory; appears FIRST, before the verdict card)".
Recommendation: discard (superseded).

- Branch verdict: NEEDS OPERATOR CHOICE (lone-concall FAST PATH, absent from main). Operator-brief edits: discard, superseded.

### origin/claude/quarterly-results-analysis-ffii20  (tip 39cf28f5, 2026-08-04, merge-base a5e269bc)
- Purpose: UNIMECH Q1 FY27 quarterly results + concall run (A1-A5, company memory, LESSONS). Only framework-path change is .gitignore.

| file | class | note |
|---|---|---|
| .gitignore `runs/*/work/*_check.txt` | IN MAIN | covered by main's `runs/*/work/*.txt` |
| .gitignore `runs/*/work/ocr/*.jpg` | NOT IN MAIN | run-only side effect: scratch OCR page images for this run |

Exact line: `+runs/*/work/ocr/*.jpg`. Recommendation: discard (run-only scratch rule; main's `runs/*/work/raster/` and `runs/*/extracted/images/` cover the current image paths).

- Branch verdict: NOTHING TO RECOVER.

### origin/claude/sasken-quarterly-analysis-xgjg0m  (tip 8cb75101, 2026-08-04, merge-base 7070d85a)
- Purpose: SASKEN Q1 FY27 quarterly + concall run, plus a new Role 4 "Step 10 Operator Intelligence Brief" (five parts, live-web sector and competitor parts by the orchestrator).

| file | class | note |
|---|---|---|
| frameworks/Quarterly_Results_Review_Protocol_v1_2.md (STEP 10 + non-negotiable) | CONFLICTS | file is now v1_4 in main, which has no Step 10; main put the brief in run-quarterly / A4 / Document_Review_Protocol as a 4-part PLAIN-LANGUAGE BRIEF |
| .claude/commands/run-quarterly.md (step 4 brief, renumbering, print brief) | CONFLICTS | main: A4 PLAIN-LANGUAGE BRIEF, final section, printed every run |
| prompts/quarterly-00-orchestrator.md (step 6 brief, Notion PREPEND) | CONFLICTS | main: brief saved at the END of the review, no orchestrator web step |
| prompts/quarterly-a4-analyst.md (OPERATOR INTELLIGENCE BRIEF opening section, YAML fields) | CONFLICTS | main A4 writes 4 parts (summary, sector, business-model, competition) as the last section; no brief_parts_written / brief_headline fields |

Exact lines (branch, Quarterly_Results_Review_Protocol_v1_2.md):
```
## STEP 10 — OPERATOR INTELLIGENCE BRIEF (always produced; the operator-facing deliverable)
3. **Sector intelligence.** ... Gathered from live sources, not memory; every external figure carries its source.
4. **Competitor intelligence.** A same-quarter peer comparison table (revenue, revenue growth, margin, PAT trend, one-line read per peer) for the closest listed comparables ... Gathered live; sourced.
5. **Forward view (house view).** A decided forward-looking assessment: the bull path and the bear weight stated symmetrically, then the two or three specific things that decide the thesis next, ranked, each with its threshold and timing.
**Producer split (architectural).** The A4 analyst subagent writes Parts 1, 2 and 5 ... Parts 3 and 4 require live market data ... the ORCHESTRATOR gathers them by web research after A5 returns COMPLETE ... PREPENDS the brief to the Notion review section
```
Main (prompts/quarterly-a4-analyst.md): "A PLAIN-LANGUAGE BRIEF (MANDATORY on EVERY run ...; the FINAL narrative section of the review, immediately before the closing YAML). Four labelled parts ... 1. SUMMARY NARRATIVE ... 2. SECTOR INTELLIGENCE ... 3. BUSINESS-MODEL INTELLIGENCE ... 4. COMPETITION INTELLIGENCE ... The three intelligence parts draw on the Notion thesis ... reconciled with this quarter's findings."
Two ideas in the branch have no main equivalent: (a) a live-web same-quarter peer comparison table gathered by the orchestrator, and (b) a ranked Forward View part with thresholds and timing. Main's brief draws on Notion and filings only.
Recommendation: discard (superseded) for structure and placement; main wins. Raise (a) and (b) to the operator only if a live-web peer table is wanted in quarterly runs (it would also touch CLAUDE.md TEAM WORKFLOW, which limits Claude Code live web to /step1 and stages 8 and 9).

- Branch verdict: NOTHING TO RECOVER (superseded by main's PLAIN-LANGUAGE BRIEF; optional operator idea: live-web peer table + ranked forward view).

### origin/claude/shyammetl-pipeline-run-x08gtb  (tip 97b6982e, 2026-07-19, merge-base 90e11189)
- Purpose: add steel rows to the Section 1B sector cap table (commodity 20x, value-added stainless/specialty 25x) after the SHYAMMETL run.

| file | class | note |
|---|---|---|
| frameworks/Master_Project_Prompt_v3.3.md (cap table, 2 rows) | NOT IN MAIN | file renamed in main to Master_Project_Prompt_v3_6.md; its cap table (lines ~430-441) has no steel row |
| frameworks/Section_1B_v3.3_Amendments.md (Amendment 8 rows + rationale paragraph) | NOT IN MAIN | main Amendment 8 table unchanged (Hospitals ... Mining 20x, Banks 18x); skill chunk .claude/skills/section-1b/references/05-sector-cap.md also has no steel row |

Main confirms the gap is still open: LESSONS.md OPEN ACTIONS: "Add a Steel / Integrated Metals row to the Section 1B cap table (SHYAMMETL ruled 20x ad hoc; MANINDS line pipe ruled 20x ad hoc on that precedent 2026-08-25; no dedicated row exists). [archetype: Commodity converter]".

Exact lines (branch):
```
| Steel — value-added stainless / specialty (durable pricing) | 25x |
| Steel — commodity (long + flat, ferro-alloys, integrated, cyclical) | 20x |

**Steel rows added 2026-07-19** (SHYAMMETL run), split 2026-07-19 into two.
- **Steel — commodity, 20x.** Long + flat carbon steel, ferro-alloys, sponge
  iron, pellets, integrated producers. ... (Mining 20x neighbourhood).
- **Steel — value-added stainless / specialty, 25x.** High-end stainless flat,
  specialty and SBQ long products ... (Recycling / Manufacturing 25x neighbourhood).
Pick the row that matches the revenue mix that DOMINATES the destination-year
economics, not the current commodity base, for a company mid mix-shift; where a
producer is genuinely split, a revenue-weighted blend of the two caps is
permitted and must be shown on the worksheet. The cap is a ceiling, not a target.
```
Recommendation: recover into main's current files (Master_Project_Prompt_v3_6.md cap table, Section_1B_v3.3_Amendments.md Amendment 8, and the regenerated skill chunk 05-sector-cap.md in the same commit, per CLAUDE.md STRUCTURE), then close the LESSONS.md OPEN ACTIONS steel line. The 20x commodity row matches the operator-confirmed SHYAMMETL and MANINDS rulings; the 25x value-added row was never operator-ruled, so the operator confirms that number. Framework amendment goes on its own branch and PR.

- Branch verdict: RECOVER steel cap rows (20x commodity, operator-confirmed; 25x value-added needs operator sign-off) into v3_6 Master, Amendment 8, and skill chunk 05.

### origin/claude/baluforge-2026-09-06-runs-ah784w  (tip 10d023ef, 2026-09-11, merge-base 5264b591)
- Purpose: BALUFORGE 2026-09-06 batch run outputs (stages 0-9, verifiers A-D), plus three PDF-extraction helper scripts (ce238916, eacc8efa).
- Framework-path files changed: tools/ only. Everything else is runs/ output (out of scope).

| file | class | note |
|---|---|---|
| tools/extract_pdfs.py | NOT IN MAIN | Main has the RULE (run-pipeline.md TOOLING GATE: "extract every inputs/ PDF to a page-marked .txt ... one "[page N]" marker per page") and LESSONS.md says the same, but no script implements it on main. Marker format differs: branch writes `[[PAGE n]]`, main's rule says `[page N]`, main's ocr_repair.py writes `===== PAGE n =====` + `[OCR:tag]`. |
| tools/check_extraction.py | NOT IN MAIN | Run-level coverage report (blank pages <50%, non-ASCII >15%). Main's tools/ocr_repair.py detects garbled/short pages per PDF (`garble_rate`, <200 chars = corrupt) but has no whole-run "which files need OCR" report. Parses only the branch's `[[PAGE n]]` marker. |
| tools/ocr_pdf.py | IN MAIN (superseded) | Main's tools/ocr_repair.py (eb1f6118, 5f67ce00) is a superset: re-OCRs only bad pages, resumable cache, priority pages, `[OCR:embedded-CORRUPT]` tagging. |

Exact lines, NOT IN MAIN items:

tools/extract_pdfs.py (branch):
```
"""Pre-extract every PDF under a run's inputs/ to page-marked .txt.
Usage: python3 tools/extract_pdfs.py runs/<ticker>-<date>
Writes runs/<ticker>-<date>/work/text/<subfolder>__<stem>.txt
Each page is preceded by a line: [[PAGE n]]
Prints one line per file: path, pages, chars, OK|EMPTY|FAIL
"""
...
        text = text.replace("\x00", "")  # null bytes make the file read as binary
        chunks.append("[[PAGE %d]]\n%s\n" % (i, text))
    status = "OK" if chars > 200 else "EMPTY"
```
Main, same subject (.claude/commands/run-pipeline.md 39-44):
```
Switch the whole run to pre-extracted text FIRST: extract every inputs/ PDF to a
page-marked .txt beside it (one "[page N]" marker per page), and pass the
.txt path to every stage and every verifier in place of the PDF.
```
Recommendation: recover, after aligning the marker to main's `[page N]` and output path ("beside it", not work/text/).

tools/check_extraction.py (branch):
```
"""Report per-page text coverage for every extracted corpus file.
A file whose pages are mostly blank has no usable text layer (scanned images),
and one whose pages carry bytes that are mostly non-ASCII is a custom-encoded
subset font. Both need OCR before any stage reads them. Run this after
tools/extract_pdfs.py and before dispatching stages.
Usage: python3 tools/check_extraction.py runs/<ticker>-<date> [more runs...]
"""
PAGE = re.compile(r"\[\[PAGE \d+\]\]")
    if coverage < 0.5:  -> "BLANK PAGES: ..."
    if ascii_share < 0.85: -> "GARBLED: ... (custom font encoding)"
```
Recommendation: recover together with extract_pdfs.py (same marker alignment); it is the triage step that tells the operator which PDFs to feed to ocr_repair.py.

- Branch verdict: RECOVER tools/extract_pdfs.py + tools/check_extraction.py (align page marker with main's `[page N]` rule first). Discard tools/ocr_pdf.py (superseded by ocr_repair.py).

### origin/claude/damodaran-framework-amendments-2wmk1z  (tip 353a61e1, 2026-08-19, merge-base d3f39876)
- Purpose: add Role 5.5 Downstream Signal Identification as a runnable Claude Code pipeline stage (stage 5b) and a standalone /downstream command; one JUBLCPL degraded run.

| file | class | note |
|---|---|---|
| prompts/05b-downstream-signal-pipeline.md | CONFLICTS | Main took a different design (4724ef09, 2026-08-20): stage 9 emits SECTION 6 DOWNSTREAM SIGNAL CANDIDATES (unverified), carried B09 -> 09b -> B10 -> 11 -> 13/finalize; verification and tracker writes happen at Role 5.5 in claude.ai. |
| .claude/agents/stage-05b-downstream.md | CONFLICTS | No stage 5b on main; same reason. |
| .claude/commands/downstream.md | CONFLICTS | No /downstream command on main; Role 5.5 runs in claude.ai; /fttcp only gates on its tracker proof. |
| prompts/00-orchestrator.md | CONFLICTS | Branch inserts row 5b and B05b payload; main's stage table (now Sonnet 5.5 / Opus 5.5, lines 425-441) has no 5b. |
| .gitignore (`runs/*/inputs/_extracted/`) | NOT IN MAIN, run-only | Side effect of the JUBLCPL degraded run's PDF-text fallback. Main ignores other paths (runs/*/work/*.txt, runs/*/extracted/images/). |

Does a Role 5.5 / downstream-signal stage exist on main in any form? YES, but not as a Code stage:
- No stage-05b agent, no 05b prompt, no /downstream command, no B05b block on main.
- Candidate generation: prompts/09-tam-pipeline.md SECTION 6 ("These are CANDIDATES: verification happens later at Role 5.5 (claude.ai) per Downstream_Source_Discovery_Protocol_v1_0"), emitted as `downstream_candidates:` (3-8 rows), copied to B10 (prompts/10-input-assembly-pipeline.md 74, 109), used by stage 11 (line 47) and 09b dossier (line 173).
- Payload: .claude/commands/finalize.md 238 "DOWNSTREAM SIGNAL TRACKER PAYLOAD (candidates for Role 5.5 verification)"; "the pipeline never writes to the tracker, Role 5.5 does".
- Gate: .claude/commands/fttcp.md 54 "ROLE 5.5 TRACKER GATE ... Tracker writes happen at Role 5.5 in claude.ai; this gate confirms they happened".
- Source registry: frameworks/Downstream_Source_Discovery_Protocol_v1_0.md; CLAUDE.md 170 "Role 5.5 verifies against it in claude.ai"; CLAUDE.md pipeline sequence puts "Role 5.5 tracker writes" in claude.ai after Halt 1.
- Signal Gate itself: .claude/skills/section-1b/references/16-fttcp-verdict-logic.md line 10 (requires signals physically written to the tracker with row URLs).
- CHANGES.md 186 still lists "The pipeline needs a Role 5.5 stage ... wired between the concall stage and FTTCP" as a follow-up; that line is stale against the design main adopted.

Exact lines, CONFLICTS:

Branch prompts/00-orchestrator.md:
```
+| 5b | Downstream Signal Identification (Role 5.5) | 05b-downstream-signal-pipeline.md | Sonnet 5 + web search | B03/B04/B05/B06 + inputs; web for primary sources only | `B05b-downstream` |
+after stage 3. Stage 6 requires stage 5. Stage 5b (Downstream Signal
+Identification, Role 5.5) requires stages 3, 4, 5, and 6, and runs after
+stage 6; it is web-search-heavy like stages 8 and 9 ...
+Stage 5b feeds the valuation stage's FTTCP Signal Gate ... Stage 5b
+can also be run on demand outside a full pipeline via the /downstream command.
+- `B05b-downstream`: signals[] (each: name, signal_type, primary_source_url,
+  cadence, current_value, bull_element, falsifying_observation,
+  anchors_transition, tracker_case), unanchored_transitions[], ...
```
Branch prompts/05b-downstream-signal-pipeline.md (header):
```
# STAGE 5b: DOWNSTREAM SIGNAL IDENTIFICATION (Role 5.5, PIPELINE MODE)
# Model: Sonnet 5 + web search enabled | Emits: B05b-downstream
# ... It runs AFTER the concall stage (B05) and peer stage (B06) and BEFORE the
# valuation stage (which carries FTTCP v2.0).
3. Every signal carries a primary-source URL and a pulled current value
```
Main, same place (prompts/09-tam-pipeline.md 101-107):
```
## SECTION 6: DOWNSTREAM SIGNAL CANDIDATES
... These are CANDIDATES: verification happens later at
Role 5.5 (claude.ai) per Downstream_Source_Discovery_Protocol_v1_0
(frameworks/). Do not verify URLs here; do name the LIKELY primary source
```
Main CLAUDE.md TEAM WORKFLOW: Claude Code's live web "is limited to WebSearch and WebFetch in /step1 and stages 8 and 9". A web-verifying stage 5b would breach that rule.

Recommendation: main wins / discard (superseded by the stage-9 candidate route plus claude.ai Role 5.5). The .gitignore line: discard (run-only). Optional cleanup for the operator, not a recovery: CHANGES.md line 186 still asks for a Code-side Role 5.5 stage.

- Branch verdict: NOTHING TO RECOVER (stage 5b and /downstream superseded by main's design; flag stale CHANGES.md 186 follow-up).

### origin/claude/pipeline-input-contract-refactor-ywsitf  (tip 535a116d, 2026-07-09, merge-base 9392f5ba)
- Purpose: "folder-based inputs + no-concall mode" (input subfolders, any filenames, concalls_available flag, degraded stage 5).

| file | class | note |
|---|---|---|
| prompts/00-orchestrator.md (folder layout, any filename) | IN MAIN | Main lines 66-110: "Inputs are identified BY FOLDER, not by filename"; main adds more folders (prospectus, announcements, shareholding, research, other). |
| prompts/00-orchestrator.md (concall quarter map) | IN MAIN | Main 121-122: "Concall quarter map: from filename if evident, else read each transcript's first page; confirm chronology before stage 5." |
| prompts/00-orchestrator.md (NO-CONCALL MODE) | IN MAIN | Main 323-340, near-verbatim (stage 5 grade C max B, stage 6 skip, verifier B, stage 7 F2). |
| prompts/00-orchestrator.md (required folder counts) | CONFLICTS | Branch makes AR/results/rating/concalls required with STOP; main later made every folder 0-N, "No input folder is required", degrade via DEGRADATION MAP. |
| .claude/commands/run-pipeline.md | CONFLICTS | Same required-count STOP rule; main lines 144-149 use 0-N counts and NO-CONCALL MODE. |
| prompts/05-concall-pipeline.md (NO-CONCALL override) | IN MAIN | Main 157-184 carries the same five-point degraded procedure. |
| runs/_template (README, .gitkeeps, manifest concalls_available) | IN MAIN | Main template has the subfolders and `concalls_available: true`. |

Exact lines, CONFLICTS:

Branch .claude/commands/run-pipeline.md / 00-orchestrator.md:
```
+   parse. Identification is by subfolder, not filename. Required folder
+   counts: inputs/annual-report/ exactly 1 PDF; inputs/results/ 2 or 3
+   PDFs (both pass); inputs/rating/ exactly 1 PDF; inputs/concalls/
+   exactly 3 PDFs, but required ONLY when the manifest has
+   concalls_available: true ...
+   Any folder missing or with the wrong count: STOP and list the offending folders.
```
Main prompts/00-orchestrator.md:
```
No input folder is required. Every folder holds 0-N files. The pipeline
inventories what exists per folder ... Degraded stages run
per the DEGRADATION MAP below; the pipeline degrades gracefully rather than
gatekeeping input.
```
Recommendation: main wins (later rewrite, consistent with CLAUDE.md "Never halt a run on company quality... only mechanical failures halt").

- Branch verdict: NOTHING TO RECOVER.

### origin/claude/quarterly-results-analysis-jz50z8  (tip c6444a78, 2026-08-13, merge-base 0921bda7)
- Purpose: GEMAROMA q1fy27 quarterly review run outputs (A1-A5 loops), plus one .gitignore chore (306230d2).

| file | class | note |
|---|---|---|
| .gitignore (`runs/*/work/ocr/`, `runs/*/work/*_tmp/`) | NOT IN MAIN, run-only | Scratch dirs from that run's A1 OCR. Main's A1 now treats OCR as a narrow scan-only exception ("TEXT ONLY BY DEFAULT", quarterly-a1-extractor.md 25) with temp images in {{WORK_DIR}}; main already ignores `runs/*/work/raster/` and `runs/*/work/*.txt`. |

Exact lines:
```
+# quarterly pipeline A1 OCR/scratch temp dirs
+runs/*/work/ocr/
+runs/*/work/*_tmp/
```
Recommendation: discard (run-only side effect). Harmless if the operator wants scratch-dir hygiene; not required.

Note outside scope: runs/gemaroma-q1fy27/ does not exist on main. Its run outputs live only on this branch (A5 loop-2 INCOMPLETE, loop cap reached). Whether to keep them is an operator call on the runs side.

- Branch verdict: NOTHING TO RECOVER (framework side). Run outputs for GEMAROMA q1fy27 are branch-only.

### origin/tools/chartink-push-main  (tip a25b9c21, 2026-09-25, merge-base b4f399aa)
- Purpose: make push_data.bat commit Chartink data in a sparse worktree of origin/main, so the nightly push reaches main whatever branch the operator's checkout holds (it failed nightly while the checkout sat on run/dpabhushan-2026-09-19).

| file | class | note |
|---|---|---|
| tools/chartink/push_data.bat | NOT IN MAIN | Main's file is unchanged since 2cb37fea (2026-09-06); it still commits in the main checkout on whatever branch it holds. |
| tools/chartink/README.md | NOT IN MAIN | Step 9 description of the worktree flow. |

Exact lines (branch push_data.bat):
```
+set "DATAWT=C:\Users\SUMIT SHARMA\repos\ip-chartink-main"
+%GIT% fetch -q origin main || exit /b 7
+if not exist "%DATAWT%\.git" (
+    %GIT% worktree prune
+    %GIT% worktree add -q --no-checkout --detach "%DATAWT%" origin/main || exit /b 6
+    %GIT% -C "%DATAWT%" sparse-checkout set --no-cone /data/chartink/ || exit /b 6
+)
+%GIT% -C "%DATAWT%" reset -q --hard origin/main || exit /b 7
+robocopy "%REPO%\data\chartink" "%DATAWT%\data\chartink" /E /XF *.html _collector.log /R:1 /W:1 /NFL /NDL /NJH /NJS /NP >nul
+if %ERRORLEVEL% GEQ 8 exit /b 8
+cd /d "%DATAWT%" || exit /b 9
-%GIT% pull -q --rebase --autostash origin main
+%GIT% pull -q --rebase origin main
```
Main, same place:
```
REM Stage only the data tree. Rendered HTML and the run log are git-ignored.
%GIT% add -A -- data\chartink
...
%GIT% pull -q --rebase --autostash origin main
```
Context: chartink data commits do reach main now (latest c3bf3793, 2026-10-02, "chartink data: 2026-10-01"), so either the checkout is back on main or the operator runs the branch script locally. The defect returns whenever the checkout sits on a run branch.

Recommendation: recover (bug fix still valid; main's script still has the defect).

- Branch verdict: RECOVER tools/chartink/push_data.bat + tools/chartink/README.md step 9.

### origin/claude/narrative-writing-style-guide-ijkol4  (tip 76ff6606, 2026-08-11, merge-base d2092762)
- Purpose: "Add Dhruva-Research output style". This adds a Claude Code output-style file that restates the house writing style. Merge-base d2092762 is the commit that added Narrative_Writing_Style_v1.md.

| file | class | note |
|---|---|---|
| .claude/output-styles/dhruva-research.md (new, 123 lines) | IN MAIN | The file is absent from main, but its substance is in main. Narrative_Writing_Style_v1.md has the STE rules, Zinsser's four principles, the AI-tell list and the "structured outputs keep their format" scope. anti-ai-writing-style.md has the 15-year-old reading level, the symmetric bull/bear rule and the no-landing-lines rule. CLAUDE.md OPERATOR VOICE and STYLE also carry them. The only thing missing from main is the packaging: an output-style mechanism with `keep-coding-instructions: true` and the "Dhruva Research" name. Main has no .claude/output-styles/ directory. |

- Exact lines: none needed (no NOT IN MAIN or CONFLICTS item).
- Branch verdict: NOTHING TO RECOVER. Optional operator choice: whether a Claude Code output-style wrapper is wanted at all. If it is, it should point at the main style files, not copy them.

### origin/claude/section1b-banners-stage11-sync  (tip 83114fbd, 2026-08-19, merge-base 2463aeef)
- Purpose: put an "ACTIVE, not a superseded draft" banner at the top of the three Section_1B amendment files (v3.3, v3.5.1, v3.6).

| file | class | note |
|---|---|---|
| frameworks/Section_1B_v3.3_Amendments.md | IN MAIN | Main has the same banner, extended to list the v3.7 and v3.8 layers. |
| frameworks/Section_1B_v3_5_1_Reconciliation.md | IN MAIN | Main has the same banner, extended to list v3.7 and v3.8. |
| frameworks/Section_1B_v3_6_Amendments.md | IN MAIN | Main has the same banner, including the "stage 11 does not yet inject this file" NOTE. It is reworded to "below the v3.7 Amendments and the v3.8 Amendments". |

- Exact lines: none needed.
- Branch verdict: NOTHING TO RECOVER. Main's banners supersede the branch's. Side note: main's banners still name layers only up to v3.8, while CLAUDE.md names v3.9 and v3.10. This is a main-side staleness, not a branch item.

### origin/claude/tata-power-analysis-2x2wx8  (tip 3cf0b88f, 2026-07-27, merge-base 84b2f546)
- Purpose: TATAPOWER Q1FY27 quarterly review run (A1 through A5, PROCEED WITH FLAGS, finalized).

| file | class | note |
|---|---|---|
| .gitignore | NOT IN MAIN (run-only side effect) | Commit 99ba92e8 (the A1 WIP commit) adds a single `scratch/` line. That line serves only as a scratch directory for this run. Main's .gitignore was later rewritten with targeted run patterns (runs/*/work/raster/, runs/*/work/*.txt and others). Nothing in main's prompts or .claude references `scratch/`. |

- Exact lines (NOT IN MAIN):
```
+scratch/
```
  Recommendation: discard. It was a run-only ignore line, and main's scoped run patterns replace it.
- Out of framework scope, for the caller: `runs/tatapower-q1fy27/` is not on main. The whole quarterly run output exists only on this branch.
- Branch verdict: NOTHING TO RECOVER (framework). The run folder runs/tatapower-q1fy27 needs a separate operator decision if the run record is wanted on main.

### origin/claude/token-consumption-spike-f1tz7x  (tip 5f0998d5, 2026-07-29, merge-base 411d98c2)
- Purpose: three linked changes. (1) Tier 1: stage 0 builds a text cache plus an AR SECTION INDEX, and stages 2, 4, 8 and 9 read only their AR slice (about 40% fewer AR-read tokens). (2) Tier 2: verifier B reads only the 3 main-company transcripts, not all 15. (3) Stage 6 Part 6 adds sector intelligence, a peer ranking and a stronger-peer watchlist, carried into synthesis Deliverable 5 (sector-intelligence.md), verifier D, /finalize and companies/<TICKER>.md.
- Main check: main has none of `ar_section_index`, `_textcache`, `__INDEX.yaml`, `financials_and_notes`, `sector_intelligence`, `peer_ranking`, `stronger_peers` or `sector-intelligence.md`. Main's verifier B still receives "15 raw transcripts (3 main company, 12 peers)". No commit or LESSONS line on main records a rejection of these ideas. The only partial overlap is run-pipeline.md TOOLING GATE: on tooling failure, it extracts each PDF to a page-marked .txt beside the PDF, with "[page N]" markers. It does this as a fallback, says it is "the reliable default on any large corpus", and builds no section index.

| file | class | note |
|---|---|---|
| prompts/00-orchestrator.md | NOT IN MAIN | Adds the STAGE 0 TEXT CACHE AND AR SECTION INDEX section, the slice-based "Consumes" column, the B06 Part 6 payload fields, the fifth synthesis output and the SECTION-SCOPED AR READS cost note. The stage table rows it edits now carry Sonnet 5.5 / Opus 5.5 model names on main, so the edit cannot apply cleanly. |
| prompts/02-notes-triple-pass-pipeline.md | NOT IN MAIN | Stage 2 reads the notes slice, with {{ANNUAL_REPORT_FULL_FALLBACK}}. |
| prompts/04-business-model-pipeline.md | NOT IN MAIN | Stage 4 reads the business_overview + mdna slice plus the fallback. |
| prompts/08-promoter-pipeline.md | NOT IN MAIN | Stage 8 reads the governance slice, with {{AR_FULL_FALLBACK}}. |
| prompts/09-tam-pipeline.md | NOT IN MAIN | Stage 9 reads the mdna + business_overview slice plus the fallback. |
| prompts/06-peer-concall-pipeline.md | NOT IN MAIN | Adds Part 6 (6A sector state, 6B competitive standing, 6C stronger peers) and new YAML fields, and bumps the protocol to 1.2. Main stays at 1.1 with Part 5 only. |
| prompts/12-verifiers-pipeline.md | CONFLICTS (number collision) / NOT IN MAIN (substance) | The branch narrows verifier B to 3 transcripts and adds a new "rule 6" peer-contradiction audit. Main has since added a different rule 6 ("GRADE YOUR OWN LIST BEFORE YOU SCORE IT") and rule 7 (acceptance_rate null when there are fewer than 4 material items). The narrowing itself is absent from main. The branch also adds verifier D rule 6 (sector/ranking anchor check), which is NOT IN MAIN. |
| prompts/13-synthesis-pipeline.md | NOT IN MAIN | Adds Deliverable 5 sector-intelligence.md and the YAML fields sector_cycle_stage and stronger_peers. On main, the file opens with the BUSINESS UNDERSTANDING NARRATIVE spec, so the edit's line positions moved. |
| .claude/commands/run-pipeline.md | NOT IN MAIN | Adds the text cache/index build step, the AR SECTION SLICES routing, the verifier B inputs limited to 3 transcripts plus the folder path, synthesis-lite with "exactly four files", and printing sector-intelligence.md in chat. Main still says "exactly three files". The cache location also differs: the branch writes inputs/_textcache/ with [[PAGE N]] markers, and main writes a .txt beside the PDF with "[page N]" markers. |
| .claude/commands/finalize.md | NOT IN MAIN | Adds a SECTOR SNAPSHOT and PEER WATCHLIST to companies/<TICKER>.md, accrued across runs. |
| CLAUDE.md | NOT IN MAIN | Adds a MEMORY line on the sector snapshot/watchlist and a STRUCTURE line on inputs/_textcache/. |

- Exact lines (load-bearing, branch):

  Tier 1 (prompts/00-orchestrator.md, new section):
```
### STAGE 0 TEXT CACHE AND AR SECTION INDEX
1. **Page-marked cache, every input PDF.** Extract every input PDF to
   `inputs/_textcache/<source-basename>.txt` with `[[PAGE N]]` markers ...
2. **AR SECTION INDEX, annual-report caches only.** After caching each
   annual report, write `inputs/_textcache/<ar-basename>__INDEX.yaml`
   mapping the AR's canonical sections to line and page ranges ...
       financials_and_notes / mdna / business_overview / governance
   - **Slices are generous.** Round outward to whole pages ...
   - **`confidence: low` means fall back to full.** ...
   - **The full cache is always the fallback of record.** ...
   Stages 3 (AR deep dive, 8-phase backward) and 7 (Emerging Moat) traverse
   the whole document and always receive the FULL cache. Stages 2, 4, 8, 9
   receive slices per the STAGE SEQUENCE "Consumes" column.
```
  Main, same topic (.claude/commands/run-pipeline.md TOOLING GATE):
```
the whole run to pre-extracted text FIRST: extract every inputs/ PDF to a
page-marked .txt beside it (one "[page N]" marker per page), and pass the
.txt path to every stage and every verifier in place of the PDF. Pre-extracted
text is the reliable default on any large corpus in any case ...
```
  Tier 2 (prompts/12-verifiers-pipeline.md, verifier B):
```
+You are an independent concall auditor. You receive the 3 MAIN-COMPANY
+transcripts (full, raw) and the pipeline's concall analyses (B05, B06
+reports). ... You are NOT given the 12 peer transcripts to read cover to cover:
+peer-coverage completeness is Verifier D's mandate, not yours.
+6. PEER-CONTRADICTION AUDIT (narrow, no full peer read): take B06's
+   contradicted[] and unverifiable[] items ... spot-read ONLY the peer passage
+   B06 cites ... A peer contradiction B06 claims but the cited passage
+   does not support is MAJOR.
+INPUTS: {{MAIN_3_TRANSCRIPTS}} (read in full) + {{PEER_TRANSCRIPTS_FOLDER}}
```
  Main, same place:
```
You are an independent concall auditor. You receive 15 raw transcripts
(3 main company, 12 peers) and the pipeline's concall analyses (B05,
B06 reports). Read the transcripts YOURSELF, fresh, then compare.
6. GRADE YOUR OWN LIST BEFORE YOU SCORE IT. ...
7. WHEN YOUR MATERIAL LIST IS SHORT, SAY SO INSTEAD OF SCORING. ...
```
  Part 6 (prompts/06-peer-concall-pipeline.md):
```
+## PART 6: SECTOR INTELLIGENCE AND PEER RANKING (mandatory closing deliverable)
+6A SECTOR STATE. ... cycle stage ... demand trajectory; pricing and input-cost
+direction; the capex posture ...; and the 2-4 structural themes ...
+6B COMPETITIVE STANDING. Rank the main company against each peer ...
+6C STRONGER PEERS (watchlist leads). ... the caveat that keeps it a lead not a conclusion.
+- ... Never phrase 6C as a recommendation on any peer's stock, and never assign it a valuation.
+- Part 6 must not soften or override any Part 1 verdict.
+stronger_peers:  # WATCHLIST LEADS, not verdicts; operator screens them
```
  Recommendations:
  - Tier 1 (section index): recover. It is a pure token saving with a full-cache fallback. It must be re-applied onto main and reconciled with main's TOOLING GATE text format (beside-PDF .txt, "[page N]"), not merged as-is.
  - Tier 2 (verifier B narrowing): needs an operator choice. Main has since calibrated verifier B scoring (rules 6/7) around a 15-transcript read. Narrowing it changes what the Opus red-flag read sees. If recovered, renumber the branch's rule 6 as rule 8.
  - Part 6 / Deliverable 5 / watchlist: needs an operator choice. This is new scope (a stronger-peer watchlist in company memory). It overlaps with main's BUSINESS UNDERSTANDING NARRATIVE question 5 (competitive advantage) but does not duplicate it.
- Branch verdict: NEEDS OPERATOR CHOICE. Recover Tier 1, the AR section index, by re-applying it on current main. Decide Tier 2 (verifier B on 3 transcripts) and Part 6 (sector intelligence and stronger-peer watchlist). The base is 2 months stale (Opus 4.8 / Sonnet 5 era), so nothing should merge directly.

### origin/claude/urban-company-quarterly-analysis-ib51ci  (tip bd0d7b45, 2026-08-01, merge-base 7070d85a)
- Purpose: URBANCO Q1FY27 quarterly review (results, presentation and concall addendum). Commit f5758fa7 also makes a CLOSING BRIEF mandatory "across pipelines": a narrative plus sectoral, competitive and business-model intelligence. It also touches LESSONS.md, which is outside the audited path list.

| file | class | note |
|---|---|---|
| prompts/quarterly-a4-analyst.md | IN MAIN | Main's A4 has a mandatory PLAIN-LANGUAGE BRIEF with the same four parts: SUMMARY NARRATIVE, SECTOR, BUSINESS-MODEL and COMPETITION INTELLIGENCE. It also has `plain_language_brief_included: true` in its YAML, added in commit bde4fed6. Only the name differs (CLOSING BRIEF / "SECTION D" / closing_brief_included). |
| prompts/quarterly-00-orchestrator.md | IN MAIN | Main prints the A4 PLAIN-LANGUAGE BRIEF in the report (around line 234). |
| .claude/commands/run-quarterly.md | IN MAIN | Main has: "ALSO print the A4 PLAIN-LANGUAGE BRIEF every run ... The user gets this automatically". |
| prompts/13-synthesis-pipeline.md | CONFLICTS | The branch appends a 4-part CLOSING BRIEF at the END of business-narrative.md. Main replaced this place with the BUSINESS UNDERSTANDING NARRATIVE spec v1 (5 questions, 12-18 sentences, FIRST, before the verdict card, shared with finalize.md and 09b). |
| CLAUDE.md | CONFLICTS | The branch adds a "## CLOSING BRIEF (every analysis, mandatory, non-negotiable)" section covering /run-pipeline and /run-quarterly. Main has no such section. The quarterly half lives in the A4 prompt. The pipeline half is replaced by the NEVER rule "Never emit a final synthesis or Notion payload without the BUSINESS UNDERSTANDING NARRATIVE (five questions, prose, before the verdict card)". |

- Exact lines (CONFLICTS):

  Branch, CLAUDE.md:
```
+## CLOSING BRIEF (every analysis, mandatory, non-negotiable)
+Every analysis (/run-pipeline via stage 13, and /run-quarterly via A4)
+closes with a CLOSING BRIEF. ... Four parts, in this order:
+1. NARRATIVE: 10 to 12 lines ...
+2. SECTORAL INTELLIGENCE ...
+3. COMPETITIVE INTELLIGENCE ...
+4. BUSINESS MODEL ...
```
  Branch, prompts/13-synthesis-pipeline.md (in DELIVERABLE 1):
```
+Then a CLOSING BRIEF (mandatory, per CLAUDE.md "CLOSING BRIEF"), as four
+labelled sections closing the file: (1) NARRATIVE ... (2) SECTORAL INTELLIGENCE ...
+(3) COMPETITIVE INTELLIGENCE ... (4) BUSINESS MODEL ...
```
  Main, same place (prompts/13-synthesis-pipeline.md and CLAUDE.md NEVER list):
```
## BUSINESS UNDERSTANDING NARRATIVE (mandatory; appears FIRST, before the verdict card)
... The narrative MUST answer, in order:
1. WHAT THE PRODUCTS ARE ... 2. WHO THE CUSTOMERS ARE ... 3. WHY THERE IS DEMAND ...
4. WHY DEMAND SHOULD GROW ... 5. WHERE THE COMPETITIVE ADVANTAGE SITS ...
- Never emit a final synthesis or Notion payload without the
  BUSINESS UNDERSTANDING NARRATIVE (five questions, prose, before the verdict card).
```
  Recommendation: main wins for both. Main's narrative spec is the later, cross-wired design (stage 13, finalize and 09b). One gap: main's /run-pipeline synthesis has no explicit SECTORAL INTELLIGENCE part. This is the same gap the token-consumption branch's Part 6 would fill, so decide it there.
- Out of framework scope, for the caller: `runs/urbanco-q1fy27/` is not on main. All 11 run commits and the branch's LESSONS.md edits exist only on this branch.
- Branch verdict: NOTHING TO RECOVER (framework). The quarterly brief is in main as the PLAIN-LANGUAGE BRIEF, and main supersedes the pipeline CLOSING BRIEF with its BUSINESS UNDERSTANDING NARRATIVE. The run folder runs/urbanco-q1fy27 and the LESSONS.md lines need a separate decision.

### origin/claude/laxmi-quarterly-results-nk7iej  (tip f40cd780, 2026-08-12, merge-base 0921bda7)
- Purpose: /run-quarterly review of LAXMIINDIA Q1 FY27 (A1 to A5, A5 re-audit COMPLETE), plus one chore commit (c8b3609e) to gitignore a stray scratchpad dir.
- Per-file table:

| file | class | note |
|---|---|---|
| .gitignore | NOT IN MAIN | adds `scratchpad/` at repo root. Run-only side effect: no tracked `scratchpad/` exists in main, and session scratch now lives outside the repo (/tmp/.../scratchpad). |

- Exact lines (NOT IN MAIN):
```
+scratchpad/
```
  Recommendation: discard (housekeeping for one session's stray dir; harmless but not needed).
- Out of framework scope, noted for the caller: the run folder `runs/laxmiindia-q1fy27/` does not exist on main (main has only `runs/laxmiindia-2026-07-22`). If the Q1 FY27 quarterly review is wanted on record, it travels on a run PR, not a framework PR.
- Branch verdict: NOTHING TO RECOVER (framework). Run outputs `runs/laxmiindia-q1fy27/` are absent from main: operator decides whether to land them as a run PR.

### origin/claude/pipeline-finalize-updates-b6gkr7  (tip 35b457b5, 2026-07-10, merge-base 148faf2e)
- Purpose: turn /fttcp from an interactive section-by-section deliberation into an autonomous plain-language draft (MY RULINGS, year tables, operator review after), and add an RRM units clarification to Master v3.3.
- Per-file table:

| file | class | note |
|---|---|---|
| .claude/commands/fttcp.md | IN MAIN | Main's fttcp.md is the later, much larger autonomous version (FTTCP v2.3): NAME RESOLUTION (line 33), MY RULINGS (line 279), outputs/final/fttcp-draft.md (line 259), "Ask me anything or give me your overrides." (line 380). The branch's v1.2-era text is superseded in full by main; nothing of substance is missing. |
| frameworks/Master_Project_Prompt_v3.3.md | IN MAIN | The "(13.5 − r) is in percentage points" line is in main at frameworks/Master_Project_Prompt_v3_6.md:553, frameworks/Section_1B_v3.3_Amendments.md:190 (Amendment 4.4), and .claude/skills/section-1b/references/15-cost-of-capital-relative-valuation.md:28. The v3.3 file path itself no longer exists in main (renamed to v3_6). |

- Branch verdict: NOTHING TO RECOVER.

### origin/claude/pipeline-repair-signal-wiring-5v31ae  (tip 9003143f, 2026-08-20, merge-base 75a30b4a)
- Purpose: 20-Aug operator directives: Section 1B v3.7 (commodity converter, Amendment 17), stage 7 moat scan categories 21-22 (talent asymmetry, cannibalization barrier) with absolute EM thresholds, FTTCP survivorship guard, session-start fetch+merge of origin/main; plus one JUBLCPL run commit (Pillar 1 30x ratified).
- Per-file table:

| file | class | note |
|---|---|---|
| frameworks/Section_1B_v3_7_Amendments.md | IN MAIN | Byte-identical except main's banner adds a pointer to the later v3.8 layer. Also chunked into .claude/skills/section-1b/references/11-converter-amendment-17.md. |
| frameworks/FTTCP_v2_1_Consolidated.md | IN MAIN | SURVIVORSHIP GUARD (v2.1a) at main line 70-72 and version row 2.1a at line 790; also skill chunk 16. |
| frameworks/README.txt | IN MAIN | Main's version lists nine files and the seven-layer set (v3.3 to v3.10); the branch's six-file/four-layer text is superseded by a later rewrite carrying the same v3.7 entry. |
| VERSIONING.md | IN MAIN | Main lists the seven-layer set incl. "v3.7 Amendments (commodity converters, 20-Aug)". Branch four-layer wording superseded. |
| CLAUDE.md (NEVER: v3.7 layer, converter ROCE/WC line) | IN MAIN | Main NEVER list carries both: layer set through v3.10 and "Never feed spot-year ROCE or rupee-denominated WC trends ... CONVERTER-classified name (v3.7 Amendment 17)". |
| CLAUDE.md (SESSION START, mandatory fetch+merge, --no-edit, conflicts keep origin/main) | IN MAIN | Moved from CLAUDE.md prose into .claude/hooks/session-start.sh lines 99-122: `git fetch origin main`, `git merge --no-edit origin/main`, conflicts in frameworks/prompts/.claude resolved `--theirs` (origin/main), frameworks SHA list printed. Same substance, enforced by hook. |
| CLAUDE.md (STRUCTURE v3.7 layer) | IN MAIN | Main STRUCTURE lists v3.3/v3.5.1/v3.6/v3.7/v3.8/v3.9/v3.10. |
| .claude/agents/stage-07-emoat.md | IN MAIN | "Emerging moat 22-category scan" identical in main. |
| .claude/agents/stage-11-valuation.md | IN MAIN | Description bump only; main stage 11 now reads the section-1b skill (all layers). |
| .claude/agents/stage-14-thesis.md | IN MAIN | Converter top-quintile WATCHLIST line at main lines 38-40. |
| .claude/agents/stage-15-devil.md | IN MAIN | "company or the cycle? Show the spread at 5-year median input prices." at main line 47. |
| .claude/commands/finalize.md | IN MAIN | Main framework_versions string runs v3.3 to v3.10 incl. v3.7 (line 290); six-file list superseded by skill-based loading. |
| .claude/commands/fttcp.md | IN MAIN | Main lines 138-139: layer order incl. v3.7 and "For CONVERTER-classified names, the Cash transition verdict uses volume-denominated WC per v3.7 17.2." |
| prompts/00-orchestrator.md | IN MAIN | "22-category moat scan" at main line 721. |
| prompts/07-emerging-moat-pipeline.md | IN MAIN | Only diff vs main is model label (Sonnet 5 -> 5.5 in main). Family I (cat 21-22) and ABSOLUTE thresholds on 22-category base (line 178) present. |
| prompts/11-valuation-pipeline.md | IN MAIN | Converter classification rule at main lines 62-63; layer injection superseded by section-1b skill. |
| prompts/12-verifiers-pipeline.md | IN MAIN | "all 23 categories" (main line 227) and the categories 21/22 rule (main rule 8, lines 278-283). |

- Out of framework scope: commit 87c179a5 (JUBLCPL 30x ratification) differs from main's run files, but main superseded them with the 2026-08-21 Part B run; the ratification and "keep both caps" ruling are on main in LESSONS_ARCHIVE.md:201 and companies/JUBLCPL.md ("RESOLVED: Pillar 1 base 30.0x", line 38).
- Side note (main defect, not branch content): main prompts/12-verifiers-pipeline.md:207 and :209 still say "20-category scan rules" / "21-category rubric" while line 227 says 23 categories. Stale counts on main, worth a one-line fix.
- Branch verdict: NOTHING TO RECOVER.

### origin/claude/token-consumption-analysis-6tl0ko  (tip 59e97290, 2026-08-03, merge-base a5e269bc)
- Purpose: stage-0 annual-report sectioning (tools/ar_section.py) to split the AR at the Independent Auditor's Report so stages 2/4/7 read only the slice they need (~0.6M tokens per company claimed).
- Per-file table:

| file | class | note |
|---|---|---|
| tools/ar_section.py | NOT IN MAIN | 178-line byte-exact AR slicer; main tools/ has only chartink/, collector/, extract_block.py, ocr_repair.py. |
| .claude/commands/run-pipeline.md (TEXT EXTRACTION block) | IN MAIN | Main run-pipeline.md lines 38-43: pre-extract every inputs/ PDF to page-marked .txt, "reliable default on any large corpus". |
| .claude/commands/run-pipeline.md (ANNUAL REPORT SECTIONING routing) | NOT IN MAIN | No AR_front / AR_financial / ar_section anywhere in main prompts, .claude, CLAUDE.md, tools. |
| prompts/00-orchestrator.md | NOT IN MAIN | Stage-input table rows for slices and the "Annual report sectioning (token economy)" paragraph. Branch table still says "Sonnet 5", stale vs main's 5.5 dispatch. |
| prompts/02-notes-triple-pass-pipeline.md | NOT IN MAIN | AR_financial framing + {{ANNUAL_REPORT_FULL}} marker + re-read {{ANNUAL_REPORT}} in passes 2 and 3. Main still has a single {{ANNUAL_REPORT}} (line 80). |
| prompts/03-ar-deep-dive-pipeline.md | NOT IN MAIN | Comment only: stage 3 reads the full AR by design. Main behaviour is already full AR, so no functional gap. |
| prompts/04-business-model-pipeline.md | NOT IN MAIN | AR_front framing + {{ANNUAL_REPORT_FINANCIAL}} on-demand marker. |
| prompts/07-emerging-moat-pipeline.md | NOT IN MAIN | AR_front framing + {{ANNUAL_REPORT_FINANCIAL}} on-demand marker. |
| CLAUDE.md | NOT IN MAIN | STRUCTURE line for tools/ ("ar_section.py: byte-exact AR slicer"). Main STRUCTURE has no tools/ entry. Only meaningful if ar_section.py is recovered. |
| .gitignore | NOT IN MAIN | `__pycache__/` and `*.pyc`. Harmless; only relevant once Python tools run in repo. |

- Exact lines (NOT IN MAIN), load-bearing:
```
# .claude/commands/run-pipeline.md
+   ANNUAL REPORT SECTIONING (stage-0 setup, the token-saving step): after the
+   AR text exists, run
+     python3 tools/ar_section.py outputs/_working/<AR>.txt
+   It splits the AR at the Independent Auditor's Report into
+   outputs/_working/AR_sections/AR_front.txt (business, MD&A, Director's
+   report, chairman, governance) and AR_financial.txt (auditor's report, face
+   statements, and EVERY note), byte-exact, and writes AR_sections/index.txt.
+     - it printed "OK ..."  -> SLICES AVAILABLE. Route:
+         stage 2 (notes, all 3 passes): {{ANNUAL_REPORT}} = AR_financial.txt,
+             {{ANNUAL_REPORT_FULL}} = the full AR path
+         stage 4 (business):  {{ANNUAL_REPORT}} = AR_front.txt,
+             {{ANNUAL_REPORT_FINANCIAL}} = AR_financial.txt
+         stage 7 (moat):      {{ANNUAL_REPORT}} = AR_front.txt,
+             {{ANNUAL_REPORT_FINANCIAL}} = AR_financial.txt
+         stage 3 (deep dive): the FULL AR (unchanged, whole-document read)
+     - it printed "FALLBACK ..."  -> NO slices written. Route every AR marker
+         above ... to the FULL AR path ... A slice is never allowed to starve a stage of content.
+   Verifier A always reads the full source PDFs, never a slice
```
```
# prompts/00-orchestrator.md
+Boundary detection is heading-anchored and fail-safe: if the auditor's report cannot be
+located inside the middle 10-90% of the document, no slices are written and
+every AR marker routes to the full AR (today's behavior). ...
+Typical saving: the notes stage drops ~100k tokens per pass and the two business stages
+~150k each, roughly 0.6M tokens per company off the AR line
```
```
# .gitignore
+__pycache__/
+*.pyc
```
  Recommendation: NOT a lost fix but an unadopted design. Main never replaced it, so it is recoverable, but it cannot be merged as is: the prompts it edits have moved on (Sonnet 5.5 dispatch, new run-pipeline TOOLING GATE, stage 7 Family I). If wanted, re-port ar_section.py plus the routing onto current main on a framework branch; check the stage 7 prompt still finds capex/CWIP evidence when it reads AR_front only. Otherwise discard.
- Branch verdict: NEEDS OPERATOR CHOICE: adopt AR sectioning (tools/ar_section.py + stage 2/4/7 routing, re-ported onto current prompts) or discard it.

### origin/claude/truevault-quarterly-analysis-27abp5  (tip 741acbcd, 2026-07-29, merge-base 8801b626)
- Purpose: /run-quarterly review of TRUALT Q1 FY27 (A1 to A5, loop 1 resolved, A5 re-audit COMPLETE); commit 8ba8c3d6 dropped A1 OCR scratch and gitignored it.
- Per-file table:

| file | class | note |
|---|---|---|
| .gitignore `runs/*/work/*_layout.txt` | IN MAIN | Covered by main's broader `runs/*/work/*.txt`. |
| .gitignore `runs/*/work/ocr/` | NOT IN MAIN | Run-only side effect of that run's A1 OCR scratch dir. Main's A1 prompt (prompts/quarterly-a1-extractor.md) now makes OCR an exception, not a routine step, and names no work/ocr/ dir; main ignores `runs/*/work/raster/` instead. |

- Exact lines (NOT IN MAIN):
```
+runs/*/work/ocr/
```
  Recommendation: discard (run-only; harmless if added, but no current main step writes there).
- Out of framework scope: `runs/trualt-q1fy27/` does not exist on main. If the Q1 FY27 TRUALT review is wanted on record, land it as a run PR.
- Branch verdict: NOTHING TO RECOVER (framework). Run outputs `runs/trualt-q1fy27/` are absent from main: operator decides whether to land them as a run PR.

### origin/claude/netweb-results-analysis-qb5mas  (tip e8b05025, 2026-07-30, merge-base 5e268242)
- Purpose: NETWEB Q1 FY27 quarterly review run (results, press release, concall; A1 to A5). 13 commits, all run outputs.
- Per-file table:

| file | class | note |
|---|---|---|
| .gitignore | NOT IN MAIN | Run-only side effect. Ignores OCR page images left in the work root by the 300dpi OCR repair. Main ignores `runs/*/work/raster/` and `runs/*/extracted/images/` but not loose `work/*.png` / `*.jpg`. |

- Exact lines (branch adds after `canary/canary.log`):
```
+runs/*/work/*.png
+runs/*/work/*.jpg
```
  Recommendation: discard. It is run scratch hygiene. Main covers page images via `work/raster/` and `extracted/images/`. Optional recover only if loose PNGs still show up in run work roots.
- Branch verdict: NOTHING TO RECOVER (one optional .gitignore hygiene line).

### origin/claude/quarterly-analysis-agent-z2p3ps  (tip c7cfeb39, 2026-07-21, merge-base b7777bdc)
- Purpose: TATVA Q1 FY27 quarterly test runs, plus one framework commit c87151f7 "feat(quarterly): make plain-language narrative a mandatory deliverable".
- Per-file table:

| file | class | note |
|---|---|---|
| .claude/commands/run-quarterly.md | CONFLICTS | Main (bde4fed6 and later) made a mandatory PLAIN-LANGUAGE BRIEF with four parts (summary narrative, sector, business model, competition). It is printed in chat every run. Branch's two-part narrative plus standalone file is superseded. |
| prompts/quarterly-00-orchestrator.md | CONFLICTS | Same. Main step 7 surfaces the A4 brief in chat. Main has no `narrative_<ticker>_<quarter>.md` file. |
| prompts/quarterly-a4-analyst.md | CONFLICTS | Main's brief: 4 labelled parts, 10-20 lines or 200-400 words under the Document Review Protocol, provenance-labelled figures from Notion/peer work allowed. Branch: "what unfolded" + "next ~10-11 months" forward map with bull/bear forks + bottom line, "adds no new number". Different design in the same slot. |
| prompts/quarterly-a5-adversary.md | CONFLICTS | Main audit 0 (deliverable completeness) checks the four parts exist. Branch audit 4 (narrative fidelity) bans any number not already in the review tables. Main's brief deliberately admits provenance-labelled outside figures, so the branch's "no new number" rule contradicts it. |

- Exact lines.

  quarterly-a4-analyst.md (branch):
```
+## NARRATIVE (operator brief) — mandatory final deliverable
+A story of the quarter in simple language a non-specialist can follow, then a
+forward map of the next ~10-11 months. It TRANSLATES the review; it adds no new
+number and no new analysis. Every number in it must already appear above in a
+table with its source anchor. Two parts plus a bottom line:
+1. WHAT UNFOLDED THIS QUARTER. ...
+2. WHAT THE NEXT ~10-11 MONTHS WILL DECIDE. A forward map built ONLY from the
+   monitorables / catalyst list and the single-cleanest-next-quarter metric:
+   the make-or-break next reading with its date, then each dated catalyst, each
+   with its bull fork and its bear fork in one line.
+3. BOTTOM LINE. Restate the verified Decision Status plainly ...
+narrative_path: ""             # narrative_<ticker>_<quarter>.md (mandatory)
+narrative_included: true
```
  quarterly-a4-analyst.md (main, same place):
```
- A PLAIN-LANGUAGE BRIEF (MANDATORY on EVERY run, whether or not anyone asks;
  the FINAL narrative section of the review, immediately before the closing
  YAML). Four labelled parts, in this order:
  1. SUMMARY NARRATIVE — 10 to 20 lines ...
  2. SECTOR INTELLIGENCE ...  3. BUSINESS-MODEL INTELLIGENCE ...  4. COMPETITION INTELLIGENCE ...
  ... PROVENANCE-LABEL every figure: mark whether it comes from prior
  Notion / peer work or from this quarter's filings ...
plain_language_brief_included: true
```
  quarterly-a5-adversary.md (branch):
```
+4. NARRATIVE FIDELITY. Confirm the PLAIN-LANGUAGE NARRATIVE exists (final
+   section of the review AND the standalone narrative_<ticker>_<quarter>.md).
+   ... must add NO new number, NO new claim, and NO new verdict ...
+   Any invented figure, any claim not in the review, or a missing narrative =
+   FAIL, loop back to A4.
+narrative_ok: true
+narrative_issues: []
```
  quarterly-a5-adversary.md (main): `0. DELIVERABLE-COMPLETENESS AUDIT (run FIRST; a hard gate). The A4 review MUST contain a PLAIN-LANGUAGE BRIEF with all four labelled parts present and non-empty ...`

  Recommendation: main wins on structure (discard superseded). One idea is absent from main in any form: the forward map ("what the next ~10-11 months will decide", make-or-break next reading with date, each dated catalyst with a bull fork and a bear fork). Main keeps the catalyst list only as a table. The operator may want it as a fifth brief part.
- Branch verdict: NEEDS OPERATOR CHOICE: whether to add the forward-map part (next ~10-11 months, bull/bear forks per dated catalyst) to main's four-part brief. Everything else is superseded.

### origin/claude/quarterly-credit-care-analysis-pjrg9x  (tip 6428e6ff, 2026-07-31, merge-base bf223fc1)
- Purpose: SATIN Q1 FY27 quarterly + concall review runs, plus framework commit c6ae538d "require plain-language summary + sector knowledge on every concall/quarterly/annual analysis" (adds per-sector memory `sectors/<SECTOR>.md`).
- Per-file table (also non-listed paths `sectors/_template.md`, `sectors/NBFC-MFI.md` (99 lines, seeded from SATIN), and LESSONS.md changed; main has no `sectors/` directory):

| file | class | note |
|---|---|---|
| CLAUDE.md | NOT IN MAIN | New "NARRATIVE + SECTOR" law and the `sectors/<SECTOR>.md` sector-memory layer (MEMORY + STRUCTURE). Main has no sector memory anywhere (git grep "sectors/", "SECTOR MEMORY" on main: no hits outside runs). |
| prompts/03-ar-deep-dive-pipeline.md | NOT IN MAIN | Plain summary + SECTOR KNOWLEDGE blocks and YAML keys `plain_summary`, `sector`, `sector_knowledge`. Main stage 3 has none. |
| prompts/05-concall-pipeline.md | NOT IN MAIN | Same two blocks + YAML keys for stage 5. Absent in main. |
| prompts/13-synthesis-pipeline.md | NOT IN MAIN | Plain summary part overlaps main's BUSINESS UNDERSTANDING NARRATIVE (12-18 sentences, first). The SECTOR KNOWLEDGE consolidation and append to `sectors/<SECTOR>.md` is absent. |
| prompts/quarterly-00-orchestrator.md | NOT IN MAIN | Chat print of summary + sector block is IN MAIN via the A4 PLAIN-LANGUAGE BRIEF. The append to `sectors/<SECTOR>.md` is absent. |
| prompts/quarterly-a4-analyst.md | CONFLICTS | Main later rewrote this slot as the four-part brief (summary 10-20 lines, SECTOR INTELLIGENCE, business model, competition). Branch's 10-12 line summary + SECTOR KNOWLEDGE is superseded in substance. Only the "appendable verbatim to sectors/<SECTOR>.md" purpose and YAML keys are missing. |

- Exact lines.

  CLAUDE.md (branch):
```
+## NARRATIVE + SECTOR (every concall, quarterly result, or annual report)
+Every analysis of a concall, a quarterly result, or an annual report ends
+with two plain-language blocks, in addition to the anchored report. ...
+- PLAIN-LANGUAGE SUMMARY: 10 to 12 lines, simple words, no jargon, numbers
+  rounded for reading. ...
+- SECTOR KNOWLEDGE: ... Append the durable points to
+  sectors/<SECTOR>.md (create from sectors/_template.md if absent), dated and
+  sourced to the run. It is sector memory to weigh, never anchored evidence.
+Per-sector memory lives in sectors/<SECTOR>.md, appended (never overwritten)
+by every concall, quarterly, and annual-report analysis via the SECTOR
+KNOWLEDGE block. It is read as SECTOR MEMORY at the start of any run in that
+sector so cross-company sector learning compounds.
+- sectors/<SECTOR>.md     durable per-sector memory, ...
```
  prompts/03 and 05 (branch, same shape in both):
```
+- PLAIN-LANGUAGE SUMMARY: 10 to 12 lines, simple words, no jargon, numbers
+  rounded for reading. ... Narrates the report above; introduces no new figures.
+- SECTOR KNOWLEDGE: the sector/industry lessons ... written so it can be
+  appended verbatim to sectors/<SECTOR>.md.
+plain_summary: ""
+sector: ""
+sector_knowledge: []
```
  prompts/13 (branch):
```
+- SECTOR KNOWLEDGE: consolidate the sector_knowledge blocks emitted by the
+  annual-report (B03) and concall (B05) stages ... and APPEND them (never
+  overwrite), dated and sourced to the run folder, to sectors/<SECTOR>.md
```
  prompts/quarterly-00-orchestrator.md (branch):
```
+   ... and append the
+   sector points to `sectors/<SECTOR>.md` (create from `sectors/_template.md`
+   if absent), dated and sourced to this run.
+- Save the PLAIN-LANGUAGE SUMMARY and SECTOR KNOWLEDGE blocks alongside the
+  review
```
  prompts/quarterly-a4-analyst.md: branch `+- A PLAIN-LANGUAGE SUMMARY and a SECTOR KNOWLEDGE block ... 10 to 12 lines`; main same place `- A PLAIN-LANGUAGE BRIEF (MANDATORY on EVERY run ...) Four labelled parts ... 2. SECTOR INTELLIGENCE`.

  Recommendations: CLAUDE.md sector-memory law, stage 3/5/13 sector blocks, orchestrator sectors append, and `sectors/_template.md` + `sectors/NBFC-MFI.md`: recover as one amendment, IF the operator wants a sector-memory layer (it is a new memory store, so it needs an operator ruling; it also adds a NEVER-style law to CLAUDE.md). Stage 3/5/13 10-12 line plain summaries: operator choice; main's synthesis narrative already covers stage 13. quarterly-a4-analyst: main wins; on recovery, point the sector append at main's SECTOR INTELLIGENCE part instead of re-adding a parallel block.
- Branch verdict: NEEDS OPERATOR CHOICE: adopt the per-sector memory layer (`sectors/<SECTOR>.md` + template + NBFC-MFI seed, CLAUDE.md law, append steps in stages 3/5/13 and the quarterly orchestrator). Quarterly A4 summary itself is superseded.

### origin/claude/sfl-pipeline-run-lya9nj  (tip 8b1bca90, 2026-07-14, merge-base 47aec04a)
- Purpose: single commit "amend: /fttcp adds visible Step 2E + business summary; /finalize adds anti-ai publication offer; save anti-ai-writing-style.md; SFL business summary" (framework amendment and run output mixed in one commit).
- Per-file table:

| file | class | note |
|---|---|---|
| anti-ai-writing-style.md | IN MAIN | Main added it via 79f6fde5 and later revised it (main differs by +212/-114 lines). Main's version wins. |
| .claude/commands/fttcp.md | NOT IN MAIN | Two new required draft parts: visible Step 2E management vision/action prose, and a 12-15 line plain business summary. Neither is in main's /fttcp. Step 2E exists only as a framework step (FTTCP v2.1 Step 2E ledger), not as a mandated visible prose section. Numbering collides: main's part 5 is now THE P/E BASE CARD. |
| .claude/commands/finalize.md | CONFLICTS | Branch step 10 has /finalize offer, and on yes write, a publication post. Main CLAUDE.md NEVER: "Never write X posts here. Publish candidates are flagged only." Main's /finalize has no publication step. |

- Exact lines.

  fttcp.md (branch, inserted as parts 5 and 6 after THE VERDICT):
```
+5. **MANAGEMENT VISION AND ACTION (Step 2E, must be a readable section, not
+   only a table).** Per transition, in plain sentences: what management SAYS it
+   will do (vision, discounted), what it is DOCUMENTED to be DOING (action,
+   📄), and whether that action argues the pillar verdict is too conservative.
+   The five-column ledger table may sit beneath, but the prose discussion is
+   mandatory and must be printed in chat (operator instruction 2026-07-14 ...)
+6. **BUSINESS SUMMARY (MANDATORY, 12 to 15 lines, plain language, anti-ai
+   style).** ... It answers, in order: what the business and business
+   model are; what transitions are going on in the business; what the future
+   opportunities are; what the strengths are; what the weaknesses are; what the
+   risks are. ...
+written. The printed draft MUST include, visibly in chat, the MY RULINGS
+block, the Step 2E management-vision-and-action discussion (part 5), and the
+12 to 15 line business summary (part 6).
```
  fttcp.md (main, same slot): `5. **THE P/E BASE CARD (for operator approval).** A plain preview of the exit multiple ...`
  Recommendation: recover the Step 2E visible-prose requirement (it cites a dated operator instruction, 2026-07-14, and main never replaced it), renumbered after main's P/E base card. Business summary: operator choice, since main's BUSINESS UNDERSTANDING NARRATIVE in /finalize and stage 13 partly covers it, but not at /fttcp time.

  finalize.md (branch):
```
+10. PUBLICATION OFFER (mandatory, after everything else finishes). Once phase 3
+    is complete and committed, ASK the operator, in one line, whether they want
+    a publication written in anti-ai style ...
+    ... Write it to
+    outputs/final/publication-draft.md, print it in chat ...
+    (drafting happens in the Dhruva Research Public project); this operator-asked
+    draft is the permitted exception, and it is still not posted anywhere by this
+    session.
```
  main CLAUDE.md: `- Never write X posts here. Publish candidates are flagged only.`
  Recommendation: main wins (discard). It contradicts the standing NEVER rule; reviving it needs an operator ruling that amends CLAUDE.md first.
- Branch verdict: RECOVER the /fttcp Step 2E visible-prose section (renumber after P/E base card); NEEDS OPERATOR CHOICE on the /fttcp 12-15 line business summary. Publication offer: main wins. anti-ai file: in main.

