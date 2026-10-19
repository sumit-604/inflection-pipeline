# A2 LEDGER: HFCL Q2 FY27 Monitoring Agency Reports (mareport)

ids_in_structured: 411 | ids_referenced_in_ledger: 411 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: all_rows        grep_count: 411  sweep_count: 411  match: yes
category: type_NUMBER   grep_count: 172  sweep_count: 172  match: yes
category: type_ENTITY   grep_count: 65  sweep_count: 65  match: yes
category: type_ENTITY-SUMMARY   grep_count: 1  sweep_count: 1  match: yes
category: type_FORWARD   grep_count: 11  sweep_count: 11  match: yes
category: type_DATE   grep_count: 59  sweep_count: 59  match: yes
category: type_QUALIFIER   grep_count: 103  sweep_count: 103  match: yes
category: zero_standing   grep_count(A1-tagged ZERO_STANDING): 31  sweep_count(ledger flag, incl. A2-added nil/blank/0.00 rows): 45  match: A2 superset (A2 added the rest, see below)
category: slides(pages)   grep_count(fulltext page markers): 25  sweep_count(distinct pages in structured): 25  match: yes
category: superseded_ids   grep_count: 10  sweep_count: 10  match: yes
category: superseding_ids   grep_count(SUPERSEDES): 10  sweep_count: 10  match: yes
gate_a2: pass
=== END COUNT TEST ===

Per-category row counts: cover_letter=40; image_pass_corrections=21; page_footer=9; pref_cost_of_objects=16; pref_delay_in_implementation=36; pref_gcp_and_disclaimer=9; pref_ma_letter=7; pref_other_info_and_deviation=34; pref_report_header_declarations=9; pref_totals_and_deployment=25; pref_utilisation_progress=22; qip_cost_of_objects=18; qip_delay_and_gcp=30; qip_deployment_unutilised=22; qip_disclaimer=2; qip_ma_letter=8; qip_object_summary_table=15; qip_other_info_and_notes=13; qip_report_header_declarations=25; qip_utilisation_progress=45; signature_blocks=5

A2-added ZERO_STANDING (A1 did not tag): R128, R218, R252, R295, R296, R301, R305, R311, R330, R344, R350, R353, R371, R392

Superseded-ID accounting (each listed, superseded row kept on ledger; read the superseding row for the value): R138->R391, R148->R393, R149->R394, R150->R395, R294->R396, R299->R399, R303->R402, R304->R409, R306->R408, R314->R405.

Doctype note: one-off disclosure (two CARE Monitoring Agency reports). No results-filing or concall categories apply; categories are the report sections. Entities in the document: issuer, CARE, SBI FD accounts, subsidiaries HFCL Advance Systems Pvt Ltd and HFCL Technologies Pvt Ltd (no prior list, ENTITY_CHANGE not testable). No MISSING_FROM_STRUCTURED units found.

## LEDGER (ROW_ID | page/line | type | category | A2 flags | cross-ref / materiality)
R001 | p1 L18 | DATE | cover_letter | - | -
R002 | p1 L18 | ENTITY | cover_letter | - | -
R003 | p1 L20 | ENTITY | cover_letter | - | -
R004 | p1 L20 | ENTITY | cover_letter | - | -
R005 | p1 L25 | NUMBER | cover_letter | - | -
R006 | p1 L25 | NUMBER | cover_letter | - | -
R007 | p1 L27 | ENTITY | cover_letter | - | -
R008 | p1 L30 | DATE | cover_letter | - | -
R009 | p1 L35 | NUMBER | cover_letter | RESTATED | RESTATED R046,R070,R121,R163
R010 | p1 L35 | NUMBER | cover_letter | - | -
R011 | p1 L36 | NUMBER | cover_letter | - | -
R012 | p1 L37 | NUMBER | cover_letter | - | -
R013 | p1 L37 | NUMBER | cover_letter | - | -
R014 | p1 L37 | NUMBER | cover_letter | - | -
R015 | p1 L37 | NUMBER | cover_letter | - | -
R016 | p1 L38 | NUMBER | cover_letter | - | -
R017 | p1 L36 | ENTITY | cover_letter | - | -
R018 | p1 L39 | ENTITY | cover_letter | - | -
R019 | p1 L38 | DATE | cover_letter | - | -
R020 | p1 L39 | DATE | cover_letter | - | -
R021 | p1 L40 | DATE | cover_letter | - | -
R022 | p1 L40 | DATE | cover_letter | - | -
R023 | p1 L41 | DATE | cover_letter | - | -
R024 | p1 L41 | ENTITY | cover_letter | - | -
R025 | p1 L44 | DATE | cover_letter | - | -
R026 | p1 L44 | DATE | cover_letter | - | -
R027 | p1 L45 | NUMBER | cover_letter | - | -
R028 | p1 L45 | NUMBER | cover_letter | - | -
R029 | p1 L45 | ENTITY | cover_letter | - | -
R030 | p1 L47 | ENTITY | cover_letter | - | -
R031 | p1 L47 | ENTITY | cover_letter | - | -
R032 | p1 L48 | ENTITY | cover_letter | - | -
R033 | p1 L48 | DATE | cover_letter | - | -
R034 | p1 L49 | NUMBER | cover_letter | - | -
R035 | p1 L49 | NUMBER | cover_letter | - | -
R036 | p1 L50 | NUMBER | cover_letter | RESTATED | RESTATED R317,R325
R037 | p1 L52 | ENTITY | cover_letter | - | -
R038 | p1 L54 | ENTITY | cover_letter | - | -
R039 | p1 L65 | ENTITY | signature_blocks | - | -
R040 | p1 L67 | DATE | signature_blocks | - | -
R041 | p1 L75 | ENTITY | cover_letter | - | -
R042 | p1 L76 | ENTITY | cover_letter | - | -
R043 | p2 L78 | ENTITY | qip_ma_letter | - | -
R044 | p2 L80 | DATE | qip_ma_letter | - | -
R045 | p2 L81 | ENTITY | qip_ma_letter | - | -
R046 | p2 L93 | NUMBER | qip_ma_letter | RESTATED | RESTATED R009,R070
R047 | p2 L94 | ENTITY | qip_ma_letter | - | -
R048 | p2 L97 | DATE | qip_ma_letter | - | -
R049 | p2 L98 | DATE | qip_ma_letter | - | -
R050 | p2 L105 | ENTITY | signature_blocks | - | -
R051 | p2 L109 | ENTITY-SUMMARY | qip_ma_letter | - | -
R052 | p3 L119 | ENTITY | qip_report_header_declarations | - | -
R053 | p3 L120 | DATE | qip_report_header_declarations | - | -
R054 | p3 L121 | ENTITY | qip_report_header_declarations | - | -
R055 | p3 L122 | QUALIFIER | qip_report_header_declarations | - | -
R056 | p3 L123 | QUALIFIER | qip_report_header_declarations | - | -
R057 | p3 L126 | QUALIFIER | qip_report_header_declarations | - | -
R058 | p3 L130 | QUALIFIER | qip_report_header_declarations | - | -
R059 | p3 L135 | ENTITY | qip_report_header_declarations | RESTATED | RESTATED R222,R238
R060 | p3 L137 | QUALIFIER | qip_report_header_declarations | - | -
R061 | p3 L143 | QUALIFIER | qip_report_header_declarations | - | -
R062 | p3 L151 | ENTITY | signature_blocks | - | -
R063 | p4 L163 | ENTITY | qip_report_header_declarations | - | -
R064 | p4 L164 | ENTITY | qip_report_header_declarations | - | -
R065 | p4 L165 | ENTITY | qip_report_header_declarations | - | -
R066 | p4 L167 | DATE | qip_report_header_declarations | - | -
R067 | p4 L168 | ENTITY | qip_report_header_declarations | - | -
R068 | p4 L169 | ENTITY | qip_report_header_declarations | - | -
R069 | p4 L170 | ENTITY | qip_report_header_declarations | - | -
R070 | p4 L171 | NUMBER | qip_report_header_declarations | RESTATED | RESTATED R009,R046
R071 | p4 L179 | QUALIFIER | qip_report_header_declarations | - | -
R072 | p4 L181 | QUALIFIER | qip_report_header_declarations | - | -
R073 | p4 L182 | QUALIFIER | qip_report_header_declarations | - | -
R074 | p4 L186 | QUALIFIER | qip_report_header_declarations | - | -
R075 | p4 L188 | QUALIFIER | qip_report_header_declarations | - | -
R076 | p4 L190 | QUALIFIER | qip_report_header_declarations | - | -
R077 | p4 L184 | QUALIFIER | qip_report_header_declarations | - | -
R078 | p5 L215 | QUALIFIER | qip_other_info_and_notes | - | -
R079 | p5 L217 | QUALIFIER | qip_other_info_and_notes | - | -
R080 | p5 L220 | QUALIFIER | qip_other_info_and_notes | - | -
R081 | p5 L223 | QUALIFIER | qip_other_info_and_notes | RESTATED | RESTATED R122,R167
R082 | p5 L223 | ENTITY | qip_other_info_and_notes | - | -
R083 | p5 L223 | DATE | qip_other_info_and_notes | - | -
R084 | p5 L226 | QUALIFIER | qip_other_info_and_notes | RESTATED | RESTATED R273
R085 | p5 L228 | QUALIFIER | qip_other_info_and_notes | - | -
R086 | p5 L228 | NUMBER | qip_other_info_and_notes | RESTATED | RESTATED R275
R087 | p5 L230 | QUALIFIER | qip_other_info_and_notes | COMMINGLING | COMMINGLING
R088 | p5 L234 | QUALIFIER | qip_other_info_and_notes | COMMINGLING | COMMINGLING; MA could not ascertain directly
R089 | p5 L230 | DATE | qip_other_info_and_notes | - | -
R090 | p5 L238 | QUALIFIER | qip_other_info_and_notes | - | -
R091 | p5 L242 | NUMBER | qip_object_summary_table | - | -
R092 | p5 L242 | NUMBER | qip_object_summary_table | - | -
R093 | p5 L242 | NUMBER | qip_object_summary_table | - | -
R094 | p5 L243 | NUMBER | qip_object_summary_table | - | -
R095 | p5 L244 | NUMBER | qip_object_summary_table | - | -
R096 | p5 L248 | NUMBER | qip_object_summary_table | - | -
R097 | p5 L249 | NUMBER | qip_object_summary_table | - | -
R098 | p5 L248 | NUMBER | qip_object_summary_table | - | -
R099 | p5 L249 | NUMBER | qip_object_summary_table | - | -
R100 | p5 L251 | NUMBER | qip_object_summary_table | - | -
R101 | p5 L242 | ENTITY | qip_object_summary_table | - | -
R102 | p5 L248 | ENTITY | qip_object_summary_table | - | -
R103 | p5 L242 | DATE | qip_object_summary_table | - | -
R104 | p5 L243 | DATE | qip_object_summary_table | - | -
R105 | p5 L248 | DATE | qip_object_summary_table | - | -
R106 | p6 L266 | NUMBER | qip_cost_of_objects | - | -
R107 | p6 L273 | NUMBER | qip_cost_of_objects | - | -
R108 | p6 L275 | NUMBER | qip_cost_of_objects | - | -
R109 | p6 L300 | NUMBER | qip_cost_of_objects | - | -
R110 | p6 L300 | NUMBER | qip_cost_of_objects | - | -
R111 | p6 L266 | NUMBER | qip_cost_of_objects | - | -
R112 | p6 L276 | QUALIFIER | qip_cost_of_objects | - | -
R113 | p6 L274 | QUALIFIER | qip_cost_of_objects | - | -
R114 | p6 L274 | ENTITY | qip_cost_of_objects | - | -
R115 | p6 L282 | ENTITY | qip_cost_of_objects | - | -
R116 | p6 L292 | ENTITY | qip_cost_of_objects | - | -
R117 | p6 L297 | ENTITY | qip_cost_of_objects | - | -
R118 | p6 L302 | ENTITY | qip_cost_of_objects | - | -
R119 | p7 L317 | ENTITY | qip_cost_of_objects | - | -
R120 | p7 L317 | NUMBER | qip_cost_of_objects | - | -
R121 | p7 L321 | NUMBER | qip_cost_of_objects | - | -
R122 | p7 L323 | QUALIFIER | qip_cost_of_objects | RESTATED | RESTATED R081
R123 | p7 L317 | QUALIFIER | qip_cost_of_objects | - | -
R124 | p7 L351 | NUMBER | qip_utilisation_progress | - | -
R125 | p7 L350 | NUMBER | qip_utilisation_progress | - | -
R126 | p7 L350 | NUMBER | qip_utilisation_progress | - | -
R127 | p7 L350 | NUMBER | qip_utilisation_progress | - | -
R128 | p7 L351 | NUMBER | qip_utilisation_progress | ZERO_STANDING | -
R129 | p7 L338 | QUALIFIER | qip_utilisation_progress | - | -
R130 | p7 L342 | NUMBER | qip_utilisation_progress | - | -
R131 | p7 L327 | QUALIFIER | qip_utilisation_progress | - | -
R132 | p7 L349 | QUALIFIER | qip_utilisation_progress | - | -
R133 | p8 L396 | NUMBER | qip_utilisation_progress | - | -
R134 | p8 L396 | NUMBER | qip_utilisation_progress | - | -
R135 | p8 L396 | NUMBER | qip_utilisation_progress | - | -
R136 | p8 L396 | NUMBER | qip_utilisation_progress | - | -
R137 | p8 L382 | NUMBER | qip_utilisation_progress | - | -
R138 | p8 L384 | NUMBER | qip_utilisation_progress | ZERO_STANDING, SUPERSEDED_BY R391 | -
R139 | p8 L388 | NUMBER | qip_utilisation_progress | - | -
R140 | p8 L385 | QUALIFIER | qip_utilisation_progress | - | -
R141 | p8 L401 | NUMBER | qip_utilisation_progress | COMMINGLING | COMMINGLING; R141+R142 = R135 (10.98)
R142 | p8 L406 | NUMBER | qip_utilisation_progress | COMMINGLING | COMMINGLING; R141+R142 = R135
R143 | p8 L406 | QUALIFIER | qip_utilisation_progress | COMMINGLING | COMMINGLING
R144 | p8 L414 | NUMBER | qip_utilisation_progress | - | -
R145 | p8 L414 | NUMBER | qip_utilisation_progress | - | -
R146 | p8 L414 | NUMBER | qip_utilisation_progress | ZERO_STANDING | -
R147 | p8 L414 | NUMBER | qip_utilisation_progress | - | -
R148 | p9 L435 | NUMBER | qip_utilisation_progress | ZERO_STANDING, SUPERSEDED_BY R393 | -
R149 | p9 L436 | NUMBER | qip_utilisation_progress | SUPERSEDED_BY R394 | -
R150 | p9 L437 | NUMBER | qip_utilisation_progress | SUPERSEDED_BY R395 | -
R151 | p9 L448 | NUMBER | qip_utilisation_progress | - | -
R152 | p9 L448 | NUMBER | qip_utilisation_progress | - | -
R153 | p9 L448 | NUMBER | qip_utilisation_progress | ZERO_STANDING | -
R154 | p9 L448 | NUMBER | qip_utilisation_progress | - | -
R155 | p9 L456 | NUMBER | qip_utilisation_progress | - | -
R156 | p9 L456 | NUMBER | qip_utilisation_progress | - | -
R157 | p9 L456 | NUMBER | qip_utilisation_progress | ZERO_STANDING | -
R158 | p9 L456 | NUMBER | qip_utilisation_progress | - | -
R159 | p9 L468 | NUMBER | qip_utilisation_progress | - | -
R160 | p9 L468 | NUMBER | qip_utilisation_progress | - | -
R161 | p9 L468 | NUMBER | qip_utilisation_progress | ZERO_STANDING | -
R162 | p9 L468 | NUMBER | qip_utilisation_progress | - | -
R163 | p9 L473 | NUMBER | qip_utilisation_progress | - | -
R164 | p9 L473 | NUMBER | qip_utilisation_progress | - | -
R165 | p9 L473 | NUMBER | qip_utilisation_progress | - | -
R166 | p9 L473 | NUMBER | qip_utilisation_progress | - | -
R167 | p9 L475 | QUALIFIER | qip_utilisation_progress | RESTATED | RESTATED R081
R168 | p9 L438 | QUALIFIER | qip_utilisation_progress | - | -
R169 | p10 L486 | QUALIFIER | qip_deployment_unutilised | - | -
R170 | p10 L491 | NUMBER | qip_deployment_unutilised | - | -
R171 | p10 L491 | ENTITY | qip_deployment_unutilised | - | -
R172 | p10 L494 | NUMBER | qip_deployment_unutilised | - | -
R173 | p10 L494 | DATE | qip_deployment_unutilised | - | -
R174 | p10 L494 | NUMBER | qip_deployment_unutilised | - | -
R175 | p10 L494 | ENTITY | qip_deployment_unutilised | - | -
R176 | p10 L497 | NUMBER | qip_deployment_unutilised | - | -
R177 | p10 L497 | DATE | qip_deployment_unutilised | - | FD matures Oct 9 2026, before report date Oct 19 2026 (R001); status of proceeds after maturity not stated
R178 | p10 L497 | NUMBER | qip_deployment_unutilised | - | -
R179 | p10 L497 | ENTITY | qip_deployment_unutilised | - | -
R180 | p10 L499 | NUMBER | qip_deployment_unutilised | - | -
R181 | p10 L499 | DATE | qip_deployment_unutilised | - | -
R182 | p10 L499 | NUMBER | qip_deployment_unutilised | - | -
R183 | p10 L499 | ENTITY | qip_deployment_unutilised | - | -
R184 | p10 L501 | NUMBER | qip_deployment_unutilised | - | CHECK: R172+R176+R180+R170 = 24.53 vs R395 unutilised 24.33; gap 0.20 = R188 FDR interest
R185 | p10 L491 | NUMBER | qip_deployment_unutilised | - | -
R186 | p10 L503 | QUALIFIER | qip_deployment_unutilised | - | explains 24.53 vs 24.33 gap (R188)
R187 | p10 L503 | NUMBER | qip_deployment_unutilised | - | -
R188 | p10 L503 | NUMBER | qip_deployment_unutilised | - | -
R189 | p10 L503 | DATE | qip_deployment_unutilised | - | -
R190 | p10 L504 | NUMBER | qip_deployment_unutilised | - | -
R191 | p10 L506 | QUALIFIER | qip_delay_and_gcp | - | -
R192 | p10 L510 | QUALIFIER | qip_delay_and_gcp | - | -
R193 | p10 L511 | DATE | qip_delay_and_gcp | - | -
R194 | p10 L511 | NUMBER | qip_delay_and_gcp | - | -
R195 | p10 L517 | FORWARD | qip_delay_and_gcp | - | R&D Rs 24.27 cr (R137) left against FY27 deadline (R211)
R196 | p10 L520 | NUMBER | qip_delay_and_gcp | - | -
R197 | p10 L522 | QUALIFIER | qip_delay_and_gcp | - | -
R198 | p11 L550 | DATE | qip_delay_and_gcp | - | -
R199 | p11 L550 | DATE | qip_delay_and_gcp | - | -
R200 | p11 L550 | QUALIFIER | qip_delay_and_gcp | - | -
R201 | p11 L553 | DATE | qip_delay_and_gcp | - | -
R202 | p11 L553 | DATE | qip_delay_and_gcp | - | -
R203 | p11 L553 | QUALIFIER | qip_delay_and_gcp | - | -
R204 | p11 L556 | DATE | qip_delay_and_gcp | - | -
R205 | p11 L556 | DATE | qip_delay_and_gcp | - | -
R206 | p11 L556 | QUALIFIER | qip_delay_and_gcp | - | -
R207 | p11 L559 | NUMBER | qip_delay_and_gcp | - | -
R208 | p11 L559 | QUALIFIER | qip_delay_and_gcp | - | -
R209 | p11 L563 | QUALIFIER | qip_delay_and_gcp | - | -
R210 | p11 L563 | NUMBER | qip_delay_and_gcp | - | -
R211 | p11 L563 | FORWARD | qip_delay_and_gcp | - | -
R212 | p11 L563 | DATE | qip_delay_and_gcp | - | -
R213 | p11 L565 | NUMBER | qip_delay_and_gcp | - | -
R214 | p11 L567 | FORWARD | qip_delay_and_gcp | - | -
R215 | p11 L572 | QUALIFIER | qip_delay_and_gcp | - | -
R216 | p11 L572 | NUMBER | qip_delay_and_gcp | ZERO_STANDING | -
R217 | p11 L579 | NUMBER | qip_delay_and_gcp | ZERO_STANDING | -
R218 | p11 L579 | QUALIFIER | qip_delay_and_gcp | ZERO_STANDING | -
R219 | p11 L577 | QUALIFIER | qip_delay_and_gcp | - | -
R220 | p11 L574 | QUALIFIER | qip_delay_and_gcp | FOOTNOTE_UNRESOLVED | FOOTNOTE_UNRESOLVED (QIP p11); preferential analogue ^ defined at R386
R221 | p12 L592 | QUALIFIER | qip_disclaimer | - | -
R222 | p12 L607 | ENTITY | qip_disclaimer | RESTATED | RESTATED R059,R238
R223 | p13 L626 | ENTITY | pref_ma_letter | - | -
R224 | p13 L636 | DATE | pref_ma_letter | - | -
R225 | p13 L643 | NUMBER | pref_ma_letter | - | -
R226 | p13 L644 | ENTITY | pref_ma_letter | - | -
R227 | p13 L647 | DATE | pref_ma_letter | - | -
R228 | p13 L648 | DATE | pref_ma_letter | - | -
R229 | p13 L655 | ENTITY | signature_blocks | - | -
R230 | p13 L629 | ENTITY | pref_ma_letter | - | -
R231 | p13 L659 | NUMBER | page_footer | - | -
R232 | p14 L662 | ENTITY | pref_report_header_declarations | - | -
R233 | p14 L663 | DATE | pref_report_header_declarations | - | -
R234 | p14 L665 | QUALIFIER | pref_report_header_declarations | - | -
R235 | p14 L666 | QUALIFIER | pref_report_header_declarations | - | -
R236 | p14 L669 | QUALIFIER | pref_report_header_declarations | - | -
R237 | p14 L672 | QUALIFIER | pref_report_header_declarations | - | -
R238 | p14 L677 | ENTITY | pref_report_header_declarations | RESTATED | RESTATED R059,R222
R239 | p14 L679 | QUALIFIER | pref_report_header_declarations | - | -
R240 | p14 L684 | QUALIFIER | pref_report_header_declarations | - | -
R241 | p14 L694 | NUMBER | page_footer | - | -
R242 | p15 L696 | ENTITY | pref_other_info_and_deviation | - | -
R243 | p15 L697 | ENTITY | pref_other_info_and_deviation | - | -
R244 | p15 L698 | ENTITY | pref_other_info_and_deviation | - | -
R245 | p15 L701 | DATE | pref_other_info_and_deviation | - | -
R246 | p15 L702 | ENTITY | pref_other_info_and_deviation | - | -
R247 | p15 L703 | ENTITY | pref_other_info_and_deviation | - | -
R248 | p15 L704 | ENTITY | pref_other_info_and_deviation | - | -
R249 | p15 L705 | NUMBER | pref_other_info_and_deviation | - | -
R250 | p15 L716 | QUALIFIER | pref_other_info_and_deviation | - | answer No driven by object 3 delay (R253-R258)
R251 | p15 L716 | QUALIFIER | pref_other_info_and_deviation | - | -
R252 | p15 L717 | QUALIFIER | pref_other_info_and_deviation | ZERO_STANDING | zero receipt Q2FY27; cf R330
R253 | p15 L718 | NUMBER | pref_other_info_and_deviation | RESTATED, DELAY | RESTATED R255,R359,R374; DELAY
R254 | p15 L720 | DATE | pref_other_info_and_deviation | RESTATED, DELAY | DELAY; RESTATED R262,R375
R255 | p15 L722 | NUMBER | pref_other_info_and_deviation | RESTATED, DELAY | DELAY; RESTATED R253
R256 | p15 L723 | QUALIFIER | pref_other_info_and_deviation | - | -
R257 | p15 L719 | ENTITY | pref_other_info_and_deviation | - | -
R258 | p15 L725 | DATE | pref_other_info_and_deviation | RESTATED | RESTATED R360,R376
R259 | p15 L719 | ENTITY | pref_other_info_and_deviation | - | -
R260 | p16 L743 | FORWARD | pref_other_info_and_deviation | - | -
R261 | p16 L745 | DATE | pref_other_info_and_deviation | RESTATED | RESTATED R361,R377
R262 | p16 L745 | DATE | pref_other_info_and_deviation | - | -
R263 | p16 L747 | QUALIFIER | pref_other_info_and_deviation | - | -
R264 | p16 L751 | QUALIFIER | pref_other_info_and_deviation | - | -
R265 | p16 L753 | QUALIFIER | pref_other_info_and_deviation | - | -
R266 | p16 L758 | QUALIFIER | pref_other_info_and_deviation | - | -
R267 | p16 L761 | QUALIFIER | pref_other_info_and_deviation | - | -
R268 | p16 L765 | QUALIFIER | pref_other_info_and_deviation | - | -
R269 | p16 L768 | QUALIFIER | pref_other_info_and_deviation | - | -
R270 | p16 L771 | QUALIFIER | pref_other_info_and_deviation | - | -
R271 | p16 L771 | ENTITY | pref_other_info_and_deviation | - | -
R272 | p16 L759 | DATE | pref_other_info_and_deviation | - | -
R273 | p16 L773 | QUALIFIER | pref_other_info_and_deviation | RESTATED | RESTATED R084
R274 | p16 L776 | QUALIFIER | pref_other_info_and_deviation | - | -
R275 | p16 L776 | NUMBER | pref_other_info_and_deviation | RESTATED | RESTATED R086
R276 | p16 L778 | NUMBER | page_footer | - | -
R277 | p17 L796 | NUMBER | pref_cost_of_objects | - | -
R278 | p17 L798 | NUMBER | pref_cost_of_objects | - | -
R279 | p17 L800 | NUMBER | pref_cost_of_objects | - | -
R280 | p17 L802 | NUMBER | pref_cost_of_objects | - | -
R281 | p17 L804 | NUMBER | pref_cost_of_objects | - | -
R282 | p17 L800 | QUALIFIER | pref_cost_of_objects | - | -
R283 | p17 L808 | ENTITY | pref_cost_of_objects | - | -
R284 | p17 L820 | ENTITY | pref_cost_of_objects | - | -
R285 | p17 L827 | ENTITY | pref_cost_of_objects | - | -
R286 | p17 L836 | ENTITY | pref_cost_of_objects | - | -
R287 | p17 L805 | QUALIFIER | pref_cost_of_objects | - | -
R288 | p18 L850 | NUMBER | pref_cost_of_objects | - | -
R289 | p18 L847 | ENTITY | pref_cost_of_objects | - | -
R290 | p18 L860 | NUMBER | pref_cost_of_objects | - | -
R291 | p18 L862 | QUALIFIER | pref_cost_of_objects | - | -
R292 | p18 L862 | DATE | pref_cost_of_objects | - | -
R293 | p18 L875 | NUMBER | pref_utilisation_progress | - | -
R294 | p18 L879 | NUMBER | pref_utilisation_progress | ZERO_STANDING, SUPERSEDED_BY R396 | -
R295 | p18 L874 | QUALIFIER | pref_utilisation_progress | ZERO_STANDING | -
R296 | p18 L877 | DATE | pref_utilisation_progress | ZERO_STANDING | -
R297 | p18 L879 | QUALIFIER | pref_utilisation_progress | - | -
R298 | p19 L934 | NUMBER | pref_utilisation_progress | - | -
R299 | p19 L934 | NUMBER | pref_utilisation_progress | ZERO_STANDING, SUPERSEDED_BY R399 | -
R300 | p19 L926 | QUALIFIER | pref_utilisation_progress | - | -
R301 | p19 L909 | QUALIFIER | pref_utilisation_progress | ZERO_STANDING | -
R302 | p19 L944 | NUMBER | pref_utilisation_progress | - | -
R303 | p19 L944 | NUMBER | pref_utilisation_progress | ZERO_STANDING, SUPERSEDED_BY R402 | -
R304 | p20 L968 | NUMBER | pref_utilisation_progress | SUPERSEDED_BY R409 | -
R305 | p20 L970 | QUALIFIER | pref_utilisation_progress | ZERO_STANDING | -
R306 | p20 L977 | NUMBER | pref_utilisation_progress | SUPERSEDED_BY R408 | -
R307 | p20 L981 | NUMBER | pref_utilisation_progress | - | -
R308 | p20 L981 | NUMBER | pref_utilisation_progress | - | -
R309 | p20 L981 | NUMBER | pref_utilisation_progress | ZERO_STANDING | -
R310 | p20 L981 | NUMBER | pref_utilisation_progress | - | -
R311 | p20 L977 | QUALIFIER | pref_utilisation_progress | ZERO_STANDING | -
R312 | p20 L988 | QUALIFIER | pref_utilisation_progress | - | -
R313 | p20 L1000 | NUMBER | pref_utilisation_progress | - | -
R314 | p20 L1000 | NUMBER | pref_utilisation_progress | ZERO_STANDING, SUPERSEDED_BY R405 | -
R315 | p20 L1016 | NUMBER | page_footer | - | -
R316 | p21 L1052 | NUMBER | pref_totals_and_deployment | - | -
R317 | p21 L1052 | NUMBER | pref_totals_and_deployment | RESTATED | RESTATED R036,R325
R318 | p21 L1052 | NUMBER | pref_totals_and_deployment | - | -
R319 | p21 L1052 | NUMBER | pref_totals_and_deployment | ZERO_STANDING | -
R320 | p21 L1052 | NUMBER | pref_totals_and_deployment | - | -
R321 | p21 L1052 | NUMBER | pref_totals_and_deployment | - | -
R322 | p21 L1054 | QUALIFIER | pref_totals_and_deployment | - | -
R323 | p21 L1056 | QUALIFIER | pref_totals_and_deployment | - | -
R324 | p21 L1056 | NUMBER | pref_totals_and_deployment | - | -
R325 | p21 L1056 | NUMBER | pref_totals_and_deployment | RESTATED | RESTATED R036,R317
R326 | p21 L1056 | NUMBER | pref_totals_and_deployment | - | -
R327 | p21 L1056 | FORWARD | pref_totals_and_deployment | - | warrant conversion window ends ~Nov 2027 (25.05.2026 + 18 months); computed from stated terms
R328 | p21 L1056 | DATE | pref_totals_and_deployment | - | -
R329 | p21 L1056 | NUMBER | pref_totals_and_deployment | - | -
R330 | p21 L1058 | QUALIFIER | pref_totals_and_deployment | ZERO_STANDING | -
R331 | p21 L1060 | QUALIFIER | pref_totals_and_deployment | - | 506.25 = 555.00-48.75; dependent on 416.25 receipt (R326)
R332 | p21 L1060 | NUMBER | pref_totals_and_deployment | - | -
R333 | p21 L1060 | NUMBER | pref_totals_and_deployment | - | -
R334 | p21 L1062 | QUALIFIER | pref_totals_and_deployment | - | -
R335 | p21 L1066 | NUMBER | pref_totals_and_deployment | - | -
R336 | p21 L1065 | DATE | pref_totals_and_deployment | - | -
R337 | p21 L1067 | NUMBER | pref_totals_and_deployment | - | -
R338 | p21 L1067 | NUMBER | pref_totals_and_deployment | - | -
R339 | p21 L1067 | ENTITY | pref_totals_and_deployment | - | -
R340 | p21 L1065 | NUMBER | pref_totals_and_deployment | - | -
R341 | p21 L1070 | NUMBER | page_footer | - | -
R342 | p22 L1079 | QUALIFIER | pref_delay_in_implementation | - | -
R343 | p22 L1085 | DATE | pref_delay_in_implementation | - | -
R344 | p22 L1086 | FORWARD | pref_delay_in_implementation | ZERO_STANDING | -
R345 | p22 L1083 | QUALIFIER | pref_delay_in_implementation | - | -
R346 | p22 L1088 | NUMBER | pref_delay_in_implementation | - | -
R347 | p22 L1089 | DATE | pref_delay_in_implementation | - | -
R348 | p22 L1090 | NUMBER | pref_delay_in_implementation | - | -
R349 | p22 L1091 | DATE | pref_delay_in_implementation | - | -
R350 | p22 L1088 | FORWARD | pref_delay_in_implementation | ZERO_STANDING | -
R351 | p22 L1089 | QUALIFIER | pref_delay_in_implementation | - | -
R352 | p22 L1107 | DATE | pref_delay_in_implementation | - | -
R353 | p22 L1107 | FORWARD | pref_delay_in_implementation | ZERO_STANDING | -
R354 | p22 L1107 | QUALIFIER | pref_delay_in_implementation | - | Delay: Yes, Not Ascertainable; object 3 past original deadline in same quarter
R355 | p22 L1093 | QUALIFIER | pref_delay_in_implementation | - | -
R356 | p22 L1115 | DATE | pref_delay_in_implementation | - | defence consolidation conditions precedent drive object 3 delay
R357 | p22 L1121 | FORWARD | pref_delay_in_implementation | - | -
R358 | p22 L1095 | QUALIFIER | pref_delay_in_implementation | - | -
R359 | p22 L1101 | NUMBER | pref_delay_in_implementation | - | -
R360 | p22 L1098 | DATE | pref_delay_in_implementation | RESTATED | RESTATED R258,R376
R361 | p22 L1108 | DATE | pref_delay_in_implementation | RESTATED | RESTATED R261,R377
R362 | p22 L1127 | NUMBER | page_footer | - | -
R363 | p23 L1140 | QUALIFIER | pref_delay_in_implementation | - | -
R364 | p23 L1148 | DATE | pref_delay_in_implementation | - | -
R365 | p23 L1149 | NUMBER | pref_delay_in_implementation | - | -
R366 | p23 L1150 | NUMBER | pref_delay_in_implementation | - | -
R367 | p23 L1152 | NUMBER | pref_delay_in_implementation | ZERO_STANDING | -
R368 | p23 L1148 | FORWARD | pref_delay_in_implementation | - | -
R369 | p23 L1151 | QUALIFIER | pref_delay_in_implementation | - | -
R370 | p23 L1154 | DATE | pref_delay_in_implementation | - | -
R371 | p23 L1154 | FORWARD | pref_delay_in_implementation | ZERO_STANDING | -
R372 | p23 L1157 | QUALIFIER | pref_delay_in_implementation | - | -
R373 | p23 L1166 | QUALIFIER | pref_delay_in_implementation | - | -
R374 | p23 L1166 | NUMBER | pref_delay_in_implementation | - | -
R375 | p23 L1166 | DATE | pref_delay_in_implementation | - | -
R376 | p23 L1167 | DATE | pref_delay_in_implementation | RESTATED | RESTATED R258,R360
R377 | p23 L1167 | DATE | pref_delay_in_implementation | RESTATED | RESTATED R261,R361
R378 | p23 L1169 | QUALIFIER | pref_delay_in_implementation | - | -
R379 | p23 L1171 | NUMBER | page_footer | - | -
R380 | p24 L1180 | QUALIFIER | pref_gcp_and_disclaimer | - | cf R386 definition of ^
R381 | p24 L1185 | NUMBER | pref_gcp_and_disclaimer | ZERO_STANDING | -
R382 | p24 L1185 | QUALIFIER | pref_gcp_and_disclaimer | - | -
R383 | p24 L1185 | QUALIFIER | pref_gcp_and_disclaimer | - | -
R384 | p24 L1188 | NUMBER | pref_gcp_and_disclaimer | ZERO_STANDING | -
R385 | p24 L1190 | QUALIFIER | pref_gcp_and_disclaimer | - | -
R386 | p24 L1192 | QUALIFIER | pref_gcp_and_disclaimer | - | -
R387 | p24 L1198 | NUMBER | page_footer | - | -
R388 | p25 L1207 | QUALIFIER | pref_gcp_and_disclaimer | - | -
R389 | p25 L1214 | QUALIFIER | pref_gcp_and_disclaimer | - | -
R390 | p25 L1230 | NUMBER | page_footer | - | -
R391 | p8 L1254 | NUMBER | image_pass_corrections | ZERO_STANDING, SUPERSEDING | -
R392 | p9 L1256 | NUMBER | image_pass_corrections | ZERO_STANDING | blank cell; 260.00-260.00=0 per A1
R393 | p9 L1257 | NUMBER | image_pass_corrections | ZERO_STANDING, SUPERSEDING | -
R394 | p9 L1258 | NUMBER | image_pass_corrections | SUPERSEDING | -
R395 | p9 L1259 | NUMBER | image_pass_corrections | SUPERSEDING | cf R184 (24.53); gap 0.20
R396 | p19 L1272 | NUMBER | image_pass_corrections | ZERO_STANDING, SUPERSEDING | -
R397 | p19 L1272 | NUMBER | image_pass_corrections | ZERO_STANDING | -
R398 | p19 L1272 | NUMBER | image_pass_corrections | ZERO_STANDING | -
R399 | p19 L1273 | NUMBER | image_pass_corrections | ZERO_STANDING, SUPERSEDING | -
R400 | p19 L1273 | NUMBER | image_pass_corrections | ZERO_STANDING | -
R401 | p19 L1273 | NUMBER | image_pass_corrections | ZERO_STANDING | -
R402 | p19 L1274 | NUMBER | image_pass_corrections | ZERO_STANDING, SUPERSEDING | -
R403 | p19 L1274 | NUMBER | image_pass_corrections | ZERO_STANDING | -
R404 | p19 L1274 | NUMBER | image_pass_corrections | ZERO_STANDING | -
R405 | p20 L1278 | NUMBER | image_pass_corrections | ZERO_STANDING, SUPERSEDING | -
R406 | p20 L1278 | NUMBER | image_pass_corrections | ZERO_STANDING | -
R407 | p20 L1278 | NUMBER | image_pass_corrections | ZERO_STANDING | -
R408 | p20 L1276 | NUMBER | image_pass_corrections | SUPERSEDING | merged cell; per-object receipt not stated
R409 | p20 L1276 | NUMBER | image_pass_corrections | SUPERSEDING | merged cell; per-object unutilised not stated
R410 | p20 L1276 | QUALIFIER | image_pass_corrections | - | -
R411 | p19 L1271 | QUALIFIER | image_pass_corrections | - | -
