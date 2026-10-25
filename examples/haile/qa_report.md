# QA report: haile

Generated 2026-10-25T21:05:52+00:00 by pid-to-kg 0.1.0.

**0 errors, 28 warnings, 22 info.**

Errors must be fixed in the page extraction files before the graph is trusted. Warnings are things to re-check on the drawing (the *Re-check* column names the tiles). Info items are for the record.

| Severity | Code | Count |
|---|---|---|
| warning | `duplicate_tag` | 11 |
| warning | `name_conflict` | 1 |
| warning | `near_duplicate_tags` | 2 |
| warning | `off_page_reference_mismatch` | 3 |
| warning | `possible_missed_tags` | 1 |
| warning | `unmatched_off_page` | 10 |
| info | `inferred_flow_direction` | 1 |
| info | `low_confidence` | 3 |
| info | `non_isa_tag` | 3 |
| info | `tag_reused` | 15 |

## Details

| Severity | Page | Code | Item | Message | Re-check |
|---|---|---|---|---|---|
| warning | 2 | `name_conflict` | 660-TK-008 | '660-TK-008' is described as 'LIME REACTION TANK' on SHEET:660-PI-200 and as 'SLUDGE TRANSFER BOX' on SHEET:G-200 | r2c2 |
| warning | 2 | `unmatched_off_page` | P02.OPC_CW | off-page connector 'CONTACT WATER' (to 600-PI-001) has no matching connector or item | r1c4 |
| warning | 2 | `unmatched_off_page` | P02.OPC_MOL | off-page connector 'MILK OF LIME FEED LOOP' (from 800-PI-016) has no matching connector or item | r1c1, r2c1 |
| warning | 2 | `unmatched_off_page` | P02.OPC_BYPASS | off-page connector 'TW TREATED WATER DISCHARGE PUMPS 660-PP-017/018 (DISCHARGE BYPASS)' (from 660-PI-209) has no matching connector or item | r2c1, r3c1 |
| warning | 3 | `duplicate_tag` | FE-0202#2 | tag 'FE-0202' is used by more than one item on this sheet; the copy 'FE-0202B' was kept separate as 'FE-0202#2' | r2c4 |
| warning | 3 | `duplicate_tag` | FIT-0202#2 | tag 'FIT-0202' is used by more than one item on this sheet; the copy 'FIT-0202B' was kept separate as 'FIT-0202#2' | r2c4 |
| warning | 4 | `duplicate_tag` | PI-0502@660-PI-202#2 | tag 'PI-0502@660-PI-202' is used by more than one item on this sheet; the copy 'PI-0502B' was kept separate as 'PI-0502@660-PI-202#2' | r3c2, r3c3 |
| warning | 4 | `unmatched_off_page` | P04.OPC_MOL | off-page connector 'MILK OF LIME - LIME FEED LOOP' (from 800-PI-016) has no matching connector or item | r1c1 |
| warning | 5 | `duplicate_tag` | FE-0502#2 | tag 'FE-0502' is used by more than one item on this sheet; the copy 'FE-0502B' was kept separate as 'FE-0502#2' | r2c3, r2c4 |
| warning | 5 | `duplicate_tag` | FIT-0502#2 | tag 'FIT-0502' is used by more than one item on this sheet; the copy 'FIT-0502B' was kept separate as 'FIT-0502#2' | r2c3, r2c4 |
| warning | 6 | `duplicate_tag` | PI-0602#2 | tag 'PI-0602' is used by more than one item on this sheet; the copy 'PI-0602B' was kept separate as 'PI-0602#2' | r2c2 |
| warning | 9 | `duplicate_tag` | PI-1102#2 | tag 'PI-1102' is used by more than one item on this sheet; the copy 'PI-1102B' was kept separate as 'PI-1102#2' | r3c3 |
| warning | 9 | `near_duplicate_tags` | 660-TK-006 | tags 660-TK-006, 660-TK-06 differ only in zero padding; probably one item drawn with inconsistent tags (check the sheets) | r2c2 |
| warning | 9 | `near_duplicate_tags` | 660-TK-007 | tags 660-TK-007, 660-TK-07 differ only in zero padding; probably one item drawn with inconsistent tags (check the sheets) | r2c3 |
| warning | 9 | `off_page_reference_mismatch` | P09.OPC_MF | 'FL MF-101/102 (backwash)' (660-PI-207) and 'FL 660-PU-13/14' (660-PI-205) were paired by line number 8"-FL-660-104-HDPE-NA, but their flags name other drawings (660-PI-205 / 660-PI-208) | r2c4, r3c4 |
| warning | 9 | `off_page_reference_mismatch` | P09.OPC_BX002 | 'TE 660-BX-002' (660-PI-207) and 'TW 660-TK-007' (660-PI-209) were paired by line number 12"-TW-660-031-PLA-NA, but their flags name other drawings (660-PI-209 / 660-PI-208) | r2c4 |
| warning | 10 | `possible_missed_tags` |  | 1 tags found by ocr are not in the graph: OT-1 |  |
| warning | 10 | `unmatched_off_page` | P10.OPC_PEP | off-page connector 'SLUDGE PROCESS EVENTS POND' (to 600-PI-005) has no matching connector or item | r1c4, r2c4 |
| warning | 10 | `unmatched_off_page` | P10.OPC_THK | off-page connector 'SLUDGE CYANIDE RECOVERY THICKENER FEED BOX 600-BX-001' (to 600-PI-001) has no matching connector or item | r2c4 |
| warning | 11 | `unmatched_off_page` | P11.OPC_650TK002 | off-page connector 'TREATED WATER INTERNAL RECLAIM WATER TANK 650-TK-002' (to 650-PI-002) has no matching connector or item | r1c4 |
| warning | 11 | `unmatched_off_page` | P11.OPC_600BX001 | off-page connector 'TREATED WATER CYANIDE RECOVERY THICKENER FEED BOX 600-BX-001' (to 600-PI-001) has no matching connector or item | r1c4, r2c4 |
| warning | 11 | `unmatched_off_page` | P11.OPC_BYPASS | off-page connector 'TREATED WATER TRAIN A REACTION TANK 650-TK-001 (DISCHARGE BY-PASS)' (to 660-PI-001) has no matching connector or item | r2c4 |
| warning | 11 | `unmatched_off_page` | P11.OPC_050BX001 | off-page connector 'TREATED WATER 19 POND FLOW DISTRIBUTION BOX 050-BX-001' (to 050-PI-004) has no matching connector or item | r2c4 |
| warning | 12 | `duplicate_tag` | PSV-1202#2 | tag 'PSV-1202' is used by more than one item on this sheet; the copy 'FE_PSV-1202' was kept separate as 'PSV-1202#2' | r2c2 |
| warning | 12 | `duplicate_tag` | PSV-1201#2 | tag 'PSV-1201' is used by more than one item on this sheet; the copy 'FE_PSV-1201' was kept separate as 'PSV-1201#2' | r2c2, r3c2 |
| warning | 12 | `duplicate_tag` | PRV-1202#2 | tag 'PRV-1202' is used by more than one item on this sheet; the copy 'FE_PRV-1202' was kept separate as 'PRV-1202#2' | r2c3, r3c3 |
| warning | 12 | `duplicate_tag` | PI-1202#2 | tag 'PI-1202' is used by more than one item on this sheet; the copy 'FE_PI-1202' was kept separate as 'PI-1202#2' | r2c3 |
| warning | 14 | `off_page_reference_mismatch` | P14.OPC_SBS | 'CH 660-TK-004 (SBS)' (660-PI-212) and 'CH SBS SUPPLY' (660-PI-204) were paired by line number 1/2"-CH-660-202-PE-NA, but their flags name other drawings (660-PI-204 / 660-PI-202A) | r1c4 |
| info |  | `inferred_flow_direction` |  | 32 flow edges have inferred (not drawn) direction |  |
| info | 2 | `tag_reused` | ACV-0101@660-PI-200 | 'ACV-0101' identifies different items on different sheets; kept as 'ACV-0101@660-PI-200' | r1c2, r2c2 |
| info | 2 | `tag_reused` | AE-0101@660-PI-200 | 'AE-0101' identifies different items on different sheets; kept as 'AE-0101@660-PI-200' | r2c3, r3c3 |
| info | 2 | `tag_reused` | AIT-0101@660-PI-200 | 'AIT-0101' identifies different items on different sheets; kept as 'AIT-0101@660-PI-200' | r2c3, r3c3 |
| info | 2 | `tag_reused` | LE-0101@660-PI-200 | 'LE-0101' identifies different items on different sheets; kept as 'LE-0101@660-PI-200' | r3c3 |
| info | 2 | `tag_reused` | LIT-0101@660-PI-200 | 'LIT-0101' identifies different items on different sheets; kept as 'LIT-0101@660-PI-200' | r3c3 |
| info | 4 | `tag_reused` | AE-0101@660-PI-202 | 'AE-0101' identifies different items on different sheets; kept as 'AE-0101@660-PI-202' | r1c3, r1c4 |
| info | 4 | `tag_reused` | AIT-0101@660-PI-202 | 'AIT-0101' identifies different items on different sheets; kept as 'AIT-0101@660-PI-202' | r1c3, r1c4 |
| info | 4 | `tag_reused` | LE-0101@660-PI-202 | 'LE-0101' identifies different items on different sheets; kept as 'LE-0101@660-PI-202' | r1c3, r1c4 |
| info | 4 | `tag_reused` | LIT-0101@660-PI-202 | 'LIT-0101' identifies different items on different sheets; kept as 'LIT-0101@660-PI-202' | r1c3, r1c4 |
| info | 4 | `tag_reused` | PI-0502@660-PI-202 | 'PI-0502' identifies different items on different sheets; kept as 'PI-0502@660-PI-202' | r2c2, r2c3 |
| info | 5 | `tag_reused` | PI-0502@660-PI-203 | 'PI-0502' identifies different items on different sheets; kept as 'PI-0502@660-PI-203' | r2c3 |
| info | 8 | `non_isa_tag` | HHL | instrument tag 'HHL' does not parse as ISA-5.1 | r3c3, r3c4 |
| info | 8 | `non_isa_tag` | HL | instrument tag 'HL' does not parse as ISA-5.1 | r3c3, r3c4 |
| info | 8 | `non_isa_tag` | LL | instrument tag 'LL' does not parse as ISA-5.1 | r3c3, r3c4 |
| info | 10 | `low_confidence` | P10.SG_BD | sight glass was read with confidence 0.50 | r2c2 |
| info | 13 | `low_confidence` | P13.PO_DEV | In-line device drawn as box with zig-zag was read with confidence 0.50 | r2c3, r3c3 |
| info | 13 | `tag_reused` | 660-PI-021@660-PI-211 | '660-PI-021' identifies different items on different sheets; kept as '660-PI-021@660-PI-211' | r1c2 |
| info | 13 | `tag_reused` | 660-PI-022@660-PI-211 | '660-PI-022' identifies different items on different sheets; kept as '660-PI-022@660-PI-211' | r1c2, r2c2 |
| info | 14 | `low_confidence` | P14.SB_DEV | In-line device drawn as box with zig-zag was read with confidence 0.50 | r1c3 |
| info | 14 | `tag_reused` | 660-PI-021@660-PI-212 | '660-PI-021' identifies different items on different sheets; kept as '660-PI-021@660-PI-212' | r2c2, r3c2 |
| info | 14 | `tag_reused` | 660-PI-022@660-PI-212 | '660-PI-022' identifies different items on different sheets; kept as '660-PI-022@660-PI-212' | r3c2 |
