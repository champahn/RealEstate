# READABLE v1.1 RED-to-GREEN Metrics

status: PASS
base_v1_0_sha256: 97295f7b7b25f2d100ef8202a5b88176fd1c31465b732591f6acce6ee9cbad20
base_v1_0_preserved: True
old_v1_1_tables: 0
new_tables: 97
old_v1_1_pages: 9
new_pages: 42
old_v1_1_chars: 9256
new_chars: 38772
phase_count: 8
v1_0_title_count_in_new: 0
metadata_scrubbed: True
old_v1_1_docx_xml_well_formed: True
new_docx_xml_well_formed: True
toc_static_page_verified: True
png_count: 42
blank_like_pages: []

term_counts:
- PF: 97
- HUG: 22
- VDR: 26
- RACI: 14
- Gate Evidence: 22
- Stop-or-Approve: 19
- Training Scenario: 12
- 책임준공: 30
- 신탁: 31
- 72시간: 12
- 사고대응: 9
- 개인정보 사고: 10
- WS-00: 2
- WS-01: 4
- WS-02: 5
- WS-03: 4
- WS-04: 4
- WS-05: 4
- WS-06: 5
- WS-07: 2
- WS-08: 6
- WS-09: 6
- WS-10: 2
- WS-11: 3
- WS-12: 4

GREEN conditions: base SHA preserved, new DOCX/MD exist, 8 Phase headings present, tables >= 20, new page count > current v1.1 baseline, rendered PNG count equals PDF pages, no blank-like pages, required control terms and WS anchors present, static TOC page range matches render, DOCX XML is well-formed, and DOCX/PDF personal-name metadata is scrubbed.

note: The pre-existing v1.1_DRAFT DOCX content was not expanded; its DOCX XML placeholders and metadata were repaired for public repository hygiene and file integrity, so its exact SHA changed after the original preservation check.
