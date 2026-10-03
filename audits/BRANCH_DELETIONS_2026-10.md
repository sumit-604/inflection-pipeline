# Branch deletions, October 2026

Approved by the operator on 2026-10-03 (branch audit items 2, 3, 18, 19). Not executed from the cloud session: its git proxy refuses remote branch deletes ("remote end hung up"). Run the script below from your own machine, in a clone of the repo. Every tip hash is printed here, so any branch can be restored with `git push origin <hash>:refs/heads/<name>` while GitHub keeps the commit (unreferenced commits stay reachable by hash for a long time but are not guaranteed forever).

Kept on purpose: `main`; `run/trualt-2026-09-18` (open PR #177); `framework/ar-section-index` (draft PR #185); `claude/inflection-opus-5.5-audit-102xpl`;  every run or quarterly branch that holds files main lacks (items 20 and 21, deferred).

109 branches (100 approved 2026-10-03, plus 9 added after the PR merges the same day).

| item | category | branch | tip |
|---|---|---|---|
| item 3 merged | RUN | `claude/aimtron-pipeline-run-5ws1rt` | `625987912827c72c48f7f2187bcc6b212cd0f8f2` |
| item 3 merged | RUN | `claude/amagi-pipeline-run-a8dnwj` | `3e51dd4c73582ff6ca642b724de152452cae2128` |
| item 3 merged | QUARTERLY | `claude/atlanta-electric-quarterly-tlhdye` | `9875c1667fac32dbbf3849ede17f354f9865a06a` |
| item 3 merged | RUN | `claude/aurum-pipeline-run-hsfb25` | `2127c76c9ef080dd8e45f1b5865db4cf7c5e4d83` |
| item 3 merged | RUN | `claude/azad-pipeline-run-2wm49f` | `93332092d87abfff3aad4ef2c04c9a1b9e10fc54` |
| item 3 merged | FRAMEWORK | `claude/claudemd-team-workflow-note-a3wcfe` | `ca781230d3efa2ac7b55139dbb54e8a992bb1876` |
| item 3 merged | OTHER | `claude/cleanmax-equity-research-v8tes6` | `f481c2ecdea37603000417c606079e67cb59ca10` |
| item 3 merged | OTHER | `claude/cmsinfo-prior-year-ars` | `a1f4bfd54afb79c3a9062f109d2ce2c428e5ca1a` |
| item 3 merged | FRAMEWORK | `claude/delta-aware-refresh-runs-edf0w3` | `f79c8b5b7640f55d5b0cd18464e22c58701e3b37` |
| item 3 merged | FRAMEWORK | `claude/document-review-token-fix-ump2n4` | `50b10bcc7d87088b2cf02292bd846ccacb842d13` |
| item 3 merged | FRAMEWORK | `claude/filename-collision-run-folders-7s4lgk` | `181d78b0502887dac1ea3547faa5b1b5c1133a49` |
| item 3 merged | QUARTERLY | `claude/folder-inputs-no-concall-y19ndm` | `652726e82e22aadadbd44554fd09ba48a9e78e71` |
| item 3 merged | FRAMEWORK | `claude/fttcp-deliberation-command-id3dgh` | `1d84e656875d29f2095894c109d8168a5f2df571` |
| item 3 merged | FRAMEWORK | `claude/fttcp-handoff-dossier-xrqfwt` | `e02c653759318efbff8a832a28363ff450e69a2b` |
| item 3 merged | FRAMEWORK | `claude/fttcp-runs-permagnet-tnfysa` | `e2333cc12d175276e7f2a260d16d512f720dac25` |
| item 3 merged | FRAMEWORK | `claude/growth-symmetry-amendment-26-fzh816` | `b1cae7b722bdef3aaee552ce3d10e66b88d52c74` |
| item 3 merged | FRAMEWORK | `claude/halt1-understanding-dossier-vosrgg` | `0a4737714b5a0478d7ff9900b74bd03ac2429a29` |
| item 3 merged | FRAMEWORK | `claude/inflection-pipeline-setup-izdned` | `3606dd69d9c4750722b2430f34e22323db4aa140` |
| item 3 merged | RUN | `claude/kcpsugind-pipeline-run-6sp4j3` | `40a84b03a16b91b45d72b0f180c4378fdfd5061f` |
| item 3 merged | FRAMEWORK | `claude/lessons-framework-amendments-maninds-koqpsq` | `50bc961bdfcae1627be2d461e5eec5a8902a40a2` |
| item 3 merged | QUARTERLY | `claude/maninds-corppres-2026-09-quarterly` | `0c4af3f5f5dc372d0564c16c66bcbabb74048011` |
| item 3 merged | FRAMEWORK | `claude/merge-framework-versions-h02mnx` | `12940ac4ac9cb9c7ff17246ddfa75e9d29ac9a7b` |
| item 3 merged | RUN | `claude/northarc-pipeline-run-5psvxt` | `ac210570ab65abc0799fa595a5be0674098c9dd8` |
| item 3 merged | OTHER | `claude/operator-voice-ste` | `c9ac72b0318a574a77ed50bb893b0e1f55d8a1b2` |
| item 3 merged | OTHER | `claude/pillar-3-entry-rules-l278il` | `dbe82da35102119ee32f5519a7436486c3d94968` |
| item 3 merged | RUN | `claude/pipeline-graceful-degradation-x23ex2` | `66c774ebb8dd56ffcbfc97fab9d11c323cc0affa` |
| item 3 merged | RUN | `claude/pipeline-run-entero-pchzpu` | `1f54c81eccd4246c6e655e1d62d6eb23ab2643a5` |
| item 3 merged | RUN | `claude/pipeline-run-smruthi-tdloc4` | `b3407e8af464e42cca33ac03d2f8b41ad34266f8` |
| item 3 merged | RUN | `claude/pipeline-stage-0-empty-folders-rfslzv` | `287c1eb85d9292c5f204fee5e9726b52b1aef591` |
| item 3 merged | FRAMEWORK | `claude/pipeline-token-optimization-co1857` | `f1d1dfe6ccbe187ac0738630f6e408de29df9880` |
| item 3 merged | RUN | `claude/prizor-pipeline-run-lzsz8c` | `1e897fe2d1d0a9f6759d8e3337e68f2c720ef624` |
| item 3 merged | QUARTERLY | `claude/quarterly-results-analysis-d4p3lt` | `8b9abb067b732c77608bd5496e117c7030b2ebb7` |
| item 3 merged | OTHER | `claude/refine-protocol-v1-eilc5g` | `fdc89973ffe41b9e9f2941a7fce8dc8074b7fba0` |
| item 3 merged | OTHER | `claude/relative-valuation-cross-check-f3lgaq` | `d8eb7ee2e1753b5fb32b98ba537b1bf7cea48eb5` |
| item 3 merged | RUN | `claude/run-jublcpl-pipeline-kyh0rr` | `6109df3fcceaccd79eba67801127dbfb939b1c91` |
| item 3 merged | RUN | `claude/run-maninds-2026-08-21` | `894558e1b2ee4f3aacaf145a2c090abfc20e265b` |
| item 3 merged | RUN | `claude/run-millworks-pipeline-cmygjn` | `23d6a558532e2c06d58a9731724a6831fb755d81` |
| item 3 merged | RUN | `claude/run-pipeline-karnika-vq0a0k` | `a10925c92e1481319d54e5c99c165d197d4a70e5` |
| item 3 merged | FRAMEWORK | `claude/section-1b-amendments-v3-9-rzlhwo` | `70749212fe0667c2f7209316e16a552ee1c40e3c` |
| item 3 merged | OTHER | `claude/section-1b-v3-9-consumption-wiring` | `068e61806dd34f36918a4de87a09e41301689f48` |
| item 3 merged | FRAMEWORK | `claude/section1b-relative-crosscheck-1c` | `ced0db655c070ea392c214ba86312451931e649a` |
| item 3 merged | FRAMEWORK | `claude/spear-gate-framework-c7bjgd` | `1079831822e9fd68fc7cee85462906e14bb4625f` |
| item 3 merged | QUARTERLY | `claude/spra-quarterly-results-analysis-w8v26k` | `688073fb9077c6b11bbb7a328cb5f0e1c070b144` |
| item 3 merged | OTHER | `claude/stage-0-research-gitkeep-k7prfg` | `18f87f5115f1aa00b9063ca8de8e6ba1997329de` |
| item 3 merged | RUN | `claude/synthesis-pipeline-specs-yrq07e` | `b3281c69e9f750e2c955ebc866afcae4ccec0d9d` |
| item 3 merged | RUN | `claude/systango-pipeline-run-a82gb8` | `c1687ba9b06b469cc41f47c84aa0699eaebddbac` |
| item 3 merged | FRAMEWORK | `claude/team-workflow-v2-analysis-pn1u7j` | `b41604e126436d1e01d335ae4a73231156b555c7` |
| item 3 merged | RUN | `claude/three-phase-pipeline-restructure-8noaqc` | `d3312931264d7eab240b39ca3b063a3198bff560` |
| item 3 merged | RUN | `claude/ufbl-pipeline-run-lt3u5t` | `673473ae85890ef119a1d3b8dd9214ec765d94f7` |
| item 3 merged | OTHER | `claude/upbeat-carson-a9mou7` | `2334f011d093079ff756c8a9bfa2fe8e41d81014` |
| item 3 merged | FRAMEWORK | `claude/user-memory-file-setup-5mqpmx` | `bdcebf7a5a4b058bb64ca396fe2374019cc5111f` |
| item 3 merged | RUN | `claude/vinyas-investment-thesis-dywsg0` | `8c7cd24aca47d239ef718b6e2a20e230307f80f5` |
| item 3 merged | RUN | `claude/zaggle-pipeline-run-rist4h` | `b5eaca158d3899fd8aefd6c5d0d8402f76379dc8` |
| item 3 merged | FRAMEWORK | `extract/cleanmax-halt1-01` | `689574ff5bba3a2f5226172e8a9fae8b6de372db` |
| item 3 merged | OTHER | `extract/cleanmax-role1-02` | `9c436db1c967df614a45d7f738b8728a2f03b4de` |
| item 3 merged | FRAMEWORK | `fix/collector-and-preflight` | `273f917cc73eaca898907966c3a75e64e42a97f2` |
| item 3 merged | FRAMEWORK | `fix/stage0-gates-and-provenance` | `39889c28054f779fe6ac54757f39dcf65503d8bb` |
| item 3 merged | FRAMEWORK | `fix/verifier-calibration` | `eb01634f3b0533d04d611ce70a54c5a4474b6f19` |
| item 3 merged | FRAMEWORK | `framework/amendment-19-fv-cagr` | `2e3b0905860a7aaf2fc2727a48b24d0d155dabaf` |
| item 3 merged | FRAMEWORK | `framework/model-5-5` | `50d6031e1c87e52250d1f0c61179d31946b429ed` |
| item 3 merged | FRAMEWORK | `framework/v38-exit-symmetry` | `5efbebf98c418081ea08766eae21b3409f0eb690` |
| item 3 merged | FRAMEWORK | `lessons/name-pr-167` | `139cfc8c63efb850c2a1df0b108c2a8d59907bce` |
| item 3 merged | FRAMEWORK | `memory/compost-2026-09-16` | `caa54a6d39d7fac7d39aa94edaafcd0653d4c756` |
| item 3 merged | FRAMEWORK | `prompt-audit-fixes` | `29e3a99537f854b9f9f2869c150e4661ca6a0bfe` |
| item 3 merged | FRAMEWORK | `prompt/lessons-preread-closeout` | `2912bf02109ea11f20a94e611a2a9cf8924fe6b3` |
| item 3 merged | FRAMEWORK | `prompt/stage11-skill-preload` | `2b9c212a53f5d49f45fbccba80d394d7539155b3` |
| item 3 merged | RUN | `run/aequs-2026-09-05` | `d7e49841f32acd2b59f3185a86a81ec024c3adc6` |
| item 3 merged | RUN | `run/kabraextru-2026-09-05` | `8374c2f6fea6aece3c5d05d304262c5b846003d1` |
| item 3 merged | RUN | `run/pittieng-2026-09-05` | `ade4c46b90e97a60bb63c28a737e707cc4a5c17b` |
| item 3 merged | RUN | `run/shharich-2026-09-05` | `ec673557f0524a8ab49de801d4d047c4795ceb3d` |
| item 3 merged | RUN | `run/syngene-2026-09-15` | `abc4c85f7c5e30f7426b03299fdcb5ce41d2ae39` |
| item 3 merged | RUN | `run/titanbio-2026-09-10` | `007f100663d68196943af6a5b05849f24b8a55be` |
| item 3 merged | RUN | `run/totem-2026-09-09` | `bf23209a3d11e09278fa374552b578b4ecd0873b` |
| item 3 merged | FRAMEWORK | `run/totem-fttcp-2026-09-16` | `23cde6bbdd25d596ba7ba8f935253bf157773bc3` |
| item 3 merged | RUN | `run/visakaind-2026-09-05` | `65ce128d0e9c0deae087d8bb2681e7596a917acb` |
| item 3 merged | OTHER | `skill/section-1b` | `ce670ec7f0d87ad5194bc2768e863f7a52ca8ce1` |
| item 3 merged | RUN | `thesis/cleanmax-role2-role3` | `d5d841438fca9f12729bada69c4444d2ecedf756` |
| item 2 PR #178 merged (squash) | FRAMEWORK | `framework/oct-2026-model-update` | `058c6a8756a1f3a342259b728fe06a7393dfdceb` |
| item 18 nothing to recover | FRAMEWORK | `claude/damodaran-framework-amendments-2wmk1z` | `353a61e1019727149f7286cd5664d734fa7de45a` |
| item 18 nothing to recover | FRAMEWORK | `claude/pipeline-input-contract-refactor-ywsitf` | `535a116d2143f73d3f5477b47581abb59b78c70f` |
| item 18 nothing to recover | FRAMEWORK | `claude/pipeline-finalize-updates-b6gkr7` | `35b457b51e37ca12bf2ec304166cc946a6e2dd8c` |
| item 18 nothing to recover | FRAMEWORK | `claude/pipeline-repair-signal-wiring-5v31ae` | `9003143f84a4c994269b6255d2d851fec33af673` |
| item 18 nothing to recover | FRAMEWORK | `claude/section1b-banners-stage11-sync` | `83114fbd433e1dfa9eb2b05971d1d276e4cbb019` |
| item 18 nothing to recover | FRAMEWORK | `claude/narrative-writing-style-guide-ijkol4` | `76ff6606acdabf1829752055fab1e374c1b7893b` |
| item 19 nothing unique | RUN | `claude/amazing-gauss-t7h354` | `5eb7fd968304d47a5e736e0cc642c03afda5d855` |
| item 19 nothing unique | RUN | `claude/asianene-pipeline-run-1x1vxr` | `9d703a3abdec92dd752505df55635409c0c7f86e` |
| item 19 nothing unique | RUN | `claude/brave-volta-gfcki3` | `c1ca4773d5cd6de79fcef3114859319af1435068` |
| item 19 nothing unique | RUN | `claude/company-financial-analysis-fy27-p359ze` | `752f3b9a261e1e090f5c418e1968b678a4b8b817` |
| item 19 nothing unique | RUN | `claude/company-shallow-analysis-lk6ddk` | `19c56da64573fd4061415a2fb9348ca2a3d9213a` |
| item 19 nothing unique | RUN | `claude/company-shallow-analysis-y3r9le` | `2dda80cda0911a20f3b097eff557386a9816dfe6` |
| item 19 nothing unique | RUN | `claude/friendly-sagan-wnl8zv` | `ead515f690dd039509d94cfb61ccca7aba961c4e` |
| item 19 nothing unique | RUN | `claude/fttcp-autonomous-draft-j0h1jl` | `ad1425cbe810170e004b6964e41f672a06f912aa` |
| item 19 nothing unique | RUN | `claude/gifted-cerf-tj5ol3` | `274e61e1bb00fd6fe948df58c01a059f184dbc72` |
| item 19 nothing unique | OTHER | `claude/kids-game-repair-ylpv03` | `9354d72e7ca15d625ee22943d81272299a9e70fe` |
| item 19 nothing unique | RUN | `claude/obscp-pipeline-run-vbusqd` | `e823be6a98a44b90417022953426c5d6fb016382` |
| item 19 nothing unique | RUN | `claude/shallow-analysis-companies-zx79xm` | `ddaae59c3bdd575fcbcd7b31cef62def1becf156` |
| item 19 nothing unique | QUARTERLY | `claude/sona-blw-ads-analysis-wn318h` | `62482326c8d34caccaed7c894340a63d229921df` |
| item 19 nothing unique | RUN | `claude/ufbl-pipeline-run-8age4c` | `8da6da9ae8aedd62987b6ca0b1fb90509b136b1a` |
| item 19 nothing unique | RUN | `claude/zen-cannon-f5qm0s` | `c35c3156db79eb8f1c7e6b66384098422600b575` |
| item 19 nothing unique | RUN | `extract/asianene-fy26-halt1` | `ee638cd95457f9ee52913e3104ffa423b38c95de` |
| PR #186 merged (c74e7a10) | FRAMEWORK | `tools/sparse-session` | `847aef0871d1f6bce95ff2b32ff104a15a1a1460` |
| PR #187 merged (8849287e) | OTHER | `audit/oct-2026-branch-repo` | `1fb6744bea52727623d30007061fc086fc65bcc0` |
| PR #179 merged (f45327e5) | FRAMEWORK | `framework/recover-auto-compact` | `445f79555e1496916b3733a5024f5c7706a04d97` |
| PR #180 merged (4995588c) | FRAMEWORK | `framework/recover-sfl-step2e` | `a85945de5d8aca2ee87b67b6295d22a2111e1b79` |
| PR #181 merged (a146a518) | FRAMEWORK | `framework/recover-pdf-extract` | `17ba75f90ad5518328a7858ed8bdf5e132fe56b0` |
| PR #182 merged (18dc4bb6) | FRAMEWORK | `tools/recover-chartink-push` | `167a9a674de184c4ab5374baabdc47de5da76c36` |
| PR #184 merged (5f707091) | FRAMEWORK | `framework/recover-quarterly-forward-map` | `ea39cb212ce2ff9a06bd7c030373d7d6f3f0aa6e` |
| PR #183 merged (8aab014c) | FRAMEWORK | `framework/recover-steel-cap` | `2dfe87a963918ce0130607b1400186047aed7516` |
| PR #173 closed, superseded by #182 | FRAMEWORK | `tools/chartink-push-main` | `a25b9c214b6dc6bba9613ecee45cec663d7ac19f` |

## Script (run from your own machine)

```bash
#!/usr/bin/env bash
# Deletes the branches listed above from origin. Prints each tip first.
set -u
while read -r name sha; do
  echo "deleting $name (tip $sha)"
  git push origin --delete "$name" || echo "FAILED: $name"
done <<'LIST'
claude/aimtron-pipeline-run-5ws1rt 625987912827c72c48f7f2187bcc6b212cd0f8f2
claude/amagi-pipeline-run-a8dnwj 3e51dd4c73582ff6ca642b724de152452cae2128
claude/atlanta-electric-quarterly-tlhdye 9875c1667fac32dbbf3849ede17f354f9865a06a
claude/aurum-pipeline-run-hsfb25 2127c76c9ef080dd8e45f1b5865db4cf7c5e4d83
claude/azad-pipeline-run-2wm49f 93332092d87abfff3aad4ef2c04c9a1b9e10fc54
claude/claudemd-team-workflow-note-a3wcfe ca781230d3efa2ac7b55139dbb54e8a992bb1876
claude/cleanmax-equity-research-v8tes6 f481c2ecdea37603000417c606079e67cb59ca10
claude/cmsinfo-prior-year-ars a1f4bfd54afb79c3a9062f109d2ce2c428e5ca1a
claude/delta-aware-refresh-runs-edf0w3 f79c8b5b7640f55d5b0cd18464e22c58701e3b37
claude/document-review-token-fix-ump2n4 50b10bcc7d87088b2cf02292bd846ccacb842d13
claude/filename-collision-run-folders-7s4lgk 181d78b0502887dac1ea3547faa5b1b5c1133a49
claude/folder-inputs-no-concall-y19ndm 652726e82e22aadadbd44554fd09ba48a9e78e71
claude/fttcp-deliberation-command-id3dgh 1d84e656875d29f2095894c109d8168a5f2df571
claude/fttcp-handoff-dossier-xrqfwt e02c653759318efbff8a832a28363ff450e69a2b
claude/fttcp-runs-permagnet-tnfysa e2333cc12d175276e7f2a260d16d512f720dac25
claude/growth-symmetry-amendment-26-fzh816 b1cae7b722bdef3aaee552ce3d10e66b88d52c74
claude/halt1-understanding-dossier-vosrgg 0a4737714b5a0478d7ff9900b74bd03ac2429a29
claude/inflection-pipeline-setup-izdned 3606dd69d9c4750722b2430f34e22323db4aa140
claude/kcpsugind-pipeline-run-6sp4j3 40a84b03a16b91b45d72b0f180c4378fdfd5061f
claude/lessons-framework-amendments-maninds-koqpsq 50bc961bdfcae1627be2d461e5eec5a8902a40a2
claude/maninds-corppres-2026-09-quarterly 0c4af3f5f5dc372d0564c16c66bcbabb74048011
claude/merge-framework-versions-h02mnx 12940ac4ac9cb9c7ff17246ddfa75e9d29ac9a7b
claude/northarc-pipeline-run-5psvxt ac210570ab65abc0799fa595a5be0674098c9dd8
claude/operator-voice-ste c9ac72b0318a574a77ed50bb893b0e1f55d8a1b2
claude/pillar-3-entry-rules-l278il dbe82da35102119ee32f5519a7436486c3d94968
claude/pipeline-graceful-degradation-x23ex2 66c774ebb8dd56ffcbfc97fab9d11c323cc0affa
claude/pipeline-run-entero-pchzpu 1f54c81eccd4246c6e655e1d62d6eb23ab2643a5
claude/pipeline-run-smruthi-tdloc4 b3407e8af464e42cca33ac03d2f8b41ad34266f8
claude/pipeline-stage-0-empty-folders-rfslzv 287c1eb85d9292c5f204fee5e9726b52b1aef591
claude/pipeline-token-optimization-co1857 f1d1dfe6ccbe187ac0738630f6e408de29df9880
claude/prizor-pipeline-run-lzsz8c 1e897fe2d1d0a9f6759d8e3337e68f2c720ef624
claude/quarterly-results-analysis-d4p3lt 8b9abb067b732c77608bd5496e117c7030b2ebb7
claude/refine-protocol-v1-eilc5g fdc89973ffe41b9e9f2941a7fce8dc8074b7fba0
claude/relative-valuation-cross-check-f3lgaq d8eb7ee2e1753b5fb32b98ba537b1bf7cea48eb5
claude/run-jublcpl-pipeline-kyh0rr 6109df3fcceaccd79eba67801127dbfb939b1c91
claude/run-maninds-2026-08-21 894558e1b2ee4f3aacaf145a2c090abfc20e265b
claude/run-millworks-pipeline-cmygjn 23d6a558532e2c06d58a9731724a6831fb755d81
claude/run-pipeline-karnika-vq0a0k a10925c92e1481319d54e5c99c165d197d4a70e5
claude/section-1b-amendments-v3-9-rzlhwo 70749212fe0667c2f7209316e16a552ee1c40e3c
claude/section-1b-v3-9-consumption-wiring 068e61806dd34f36918a4de87a09e41301689f48
claude/section1b-relative-crosscheck-1c ced0db655c070ea392c214ba86312451931e649a
claude/spear-gate-framework-c7bjgd 1079831822e9fd68fc7cee85462906e14bb4625f
claude/spra-quarterly-results-analysis-w8v26k 688073fb9077c6b11bbb7a328cb5f0e1c070b144
claude/stage-0-research-gitkeep-k7prfg 18f87f5115f1aa00b9063ca8de8e6ba1997329de
claude/synthesis-pipeline-specs-yrq07e b3281c69e9f750e2c955ebc866afcae4ccec0d9d
claude/systango-pipeline-run-a82gb8 c1687ba9b06b469cc41f47c84aa0699eaebddbac
claude/team-workflow-v2-analysis-pn1u7j b41604e126436d1e01d335ae4a73231156b555c7
claude/three-phase-pipeline-restructure-8noaqc d3312931264d7eab240b39ca3b063a3198bff560
claude/ufbl-pipeline-run-lt3u5t 673473ae85890ef119a1d3b8dd9214ec765d94f7
claude/upbeat-carson-a9mou7 2334f011d093079ff756c8a9bfa2fe8e41d81014
claude/user-memory-file-setup-5mqpmx bdcebf7a5a4b058bb64ca396fe2374019cc5111f
claude/vinyas-investment-thesis-dywsg0 8c7cd24aca47d239ef718b6e2a20e230307f80f5
claude/zaggle-pipeline-run-rist4h b5eaca158d3899fd8aefd6c5d0d8402f76379dc8
extract/cleanmax-halt1-01 689574ff5bba3a2f5226172e8a9fae8b6de372db
extract/cleanmax-role1-02 9c436db1c967df614a45d7f738b8728a2f03b4de
fix/collector-and-preflight 273f917cc73eaca898907966c3a75e64e42a97f2
fix/stage0-gates-and-provenance 39889c28054f779fe6ac54757f39dcf65503d8bb
fix/verifier-calibration eb01634f3b0533d04d611ce70a54c5a4474b6f19
framework/amendment-19-fv-cagr 2e3b0905860a7aaf2fc2727a48b24d0d155dabaf
framework/model-5-5 50d6031e1c87e52250d1f0c61179d31946b429ed
framework/v38-exit-symmetry 5efbebf98c418081ea08766eae21b3409f0eb690
lessons/name-pr-167 139cfc8c63efb850c2a1df0b108c2a8d59907bce
memory/compost-2026-09-16 caa54a6d39d7fac7d39aa94edaafcd0653d4c756
prompt-audit-fixes 29e3a99537f854b9f9f2869c150e4661ca6a0bfe
prompt/lessons-preread-closeout 2912bf02109ea11f20a94e611a2a9cf8924fe6b3
prompt/stage11-skill-preload 2b9c212a53f5d49f45fbccba80d394d7539155b3
run/aequs-2026-09-05 d7e49841f32acd2b59f3185a86a81ec024c3adc6
run/kabraextru-2026-09-05 8374c2f6fea6aece3c5d05d304262c5b846003d1
run/pittieng-2026-09-05 ade4c46b90e97a60bb63c28a737e707cc4a5c17b
run/shharich-2026-09-05 ec673557f0524a8ab49de801d4d047c4795ceb3d
run/syngene-2026-09-15 abc4c85f7c5e30f7426b03299fdcb5ce41d2ae39
run/titanbio-2026-09-10 007f100663d68196943af6a5b05849f24b8a55be
run/totem-2026-09-09 bf23209a3d11e09278fa374552b578b4ecd0873b
run/totem-fttcp-2026-09-16 23cde6bbdd25d596ba7ba8f935253bf157773bc3
run/visakaind-2026-09-05 65ce128d0e9c0deae087d8bb2681e7596a917acb
skill/section-1b ce670ec7f0d87ad5194bc2768e863f7a52ca8ce1
thesis/cleanmax-role2-role3 d5d841438fca9f12729bada69c4444d2ecedf756
framework/oct-2026-model-update 058c6a8756a1f3a342259b728fe06a7393dfdceb
claude/damodaran-framework-amendments-2wmk1z 353a61e1019727149f7286cd5664d734fa7de45a
claude/pipeline-input-contract-refactor-ywsitf 535a116d2143f73d3f5477b47581abb59b78c70f
claude/pipeline-finalize-updates-b6gkr7 35b457b51e37ca12bf2ec304166cc946a6e2dd8c
claude/pipeline-repair-signal-wiring-5v31ae 9003143f84a4c994269b6255d2d851fec33af673
claude/section1b-banners-stage11-sync 83114fbd433e1dfa9eb2b05971d1d276e4cbb019
claude/narrative-writing-style-guide-ijkol4 76ff6606acdabf1829752055fab1e374c1b7893b
claude/amazing-gauss-t7h354 5eb7fd968304d47a5e736e0cc642c03afda5d855
claude/asianene-pipeline-run-1x1vxr 9d703a3abdec92dd752505df55635409c0c7f86e
claude/brave-volta-gfcki3 c1ca4773d5cd6de79fcef3114859319af1435068
claude/company-financial-analysis-fy27-p359ze 752f3b9a261e1e090f5c418e1968b678a4b8b817
claude/company-shallow-analysis-lk6ddk 19c56da64573fd4061415a2fb9348ca2a3d9213a
claude/company-shallow-analysis-y3r9le 2dda80cda0911a20f3b097eff557386a9816dfe6
claude/friendly-sagan-wnl8zv ead515f690dd039509d94cfb61ccca7aba961c4e
claude/fttcp-autonomous-draft-j0h1jl ad1425cbe810170e004b6964e41f672a06f912aa
claude/gifted-cerf-tj5ol3 274e61e1bb00fd6fe948df58c01a059f184dbc72
claude/kids-game-repair-ylpv03 9354d72e7ca15d625ee22943d81272299a9e70fe
claude/obscp-pipeline-run-vbusqd e823be6a98a44b90417022953426c5d6fb016382
claude/shallow-analysis-companies-zx79xm ddaae59c3bdd575fcbcd7b31cef62def1becf156
claude/sona-blw-ads-analysis-wn318h 62482326c8d34caccaed7c894340a63d229921df
claude/ufbl-pipeline-run-8age4c 8da6da9ae8aedd62987b6ca0b1fb90509b136b1a
claude/zen-cannon-f5qm0s c35c3156db79eb8f1c7e6b66384098422600b575
extract/asianene-fy26-halt1 ee638cd95457f9ee52913e3104ffa423b38c95de
tools/sparse-session 847aef0871d1f6bce95ff2b32ff104a15a1a1460
audit/oct-2026-branch-repo 1fb6744bea52727623d30007061fc086fc65bcc0
framework/recover-auto-compact 445f79555e1496916b3733a5024f5c7706a04d97
framework/recover-sfl-step2e a85945de5d8aca2ee87b67b6295d22a2111e1b79
framework/recover-pdf-extract 17ba75f90ad5518328a7858ed8bdf5e132fe56b0
tools/recover-chartink-push 167a9a674de184c4ab5374baabdc47de5da76c36
framework/recover-quarterly-forward-map ea39cb212ce2ff9a06bd7c030373d7d6f3f0aa6e
framework/recover-steel-cap 2dfe87a963918ce0130607b1400186047aed7516
tools/chartink-push-main a25b9c214b6dc6bba9613ecee45cec663d7ac19f
LIST
```
