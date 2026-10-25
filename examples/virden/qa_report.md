# QA report: virden

Generated 2026-10-25T21:06:01+00:00 by pid-to-kg 0.1.0.

**0 errors, 22 warnings, 26 info.**

Errors must be fixed in the page extraction files before the graph is trusted. Warnings are things to re-check on the drawing (the *Re-check* column names the tiles). Info items are for the record.

| Severity | Code | Count |
|---|---|---|
| warning | `duplicate_tag` | 11 |
| warning | `loop_no_final_element` | 1 |
| warning | `possible_missed_tags` | 10 |
| info | `inferred_flow_direction` | 1 |
| info | `isolated_instrument` | 13 |
| info | `loop_no_sensor` | 8 |
| info | `loop_no_signals` | 2 |
| info | `low_confidence` | 2 |

## Details

| Severity | Page | Code | Item | Message | Re-check |
|---|---|---|---|---|---|
| warning |  | `loop_no_final_element` | LOOP:Y-1600 | control loop Y-1600 has a controller but no final element |  |
| warning | 1 | `duplicate_tag` | XA-1001#2 | tag 'XA-1001' is used by more than one item on this sheet; the copy 'XA-1001B' was kept separate as 'XA-1001#2' | r1c2, r1c3 |
| warning | 1 | `duplicate_tag` | LAH-1201#2 | tag 'LAH-1201' is used by more than one item on this sheet; the copy 'LAH-1201B' was kept separate as 'LAH-1201#2' | r1c3, r1c4 |
| warning | 1 | `possible_missed_tags` |  | 14 tags found by ocr are not in the graph: POWER-1200A, FAULT-1200C, EL-12000, EL-12008, VALVE-12100, RESET-12008, HS-12008, HS-12100, TTYPOF-2, CHV-1301, BAVT-1OR, MEV-8151, MEV-51161, TVAROO-1 |  |
| warning | 2 | `duplicate_tag` | XAH-1621#2 | tag 'XAH-1621' is used by more than one item on this sheet; the copy 'XAH-1621B' was kept separate as 'XAH-1621#2' | r1c1 |
| warning | 2 | `duplicate_tag` | XAH-1622#2 | tag 'XAH-1622' is used by more than one item on this sheet; the copy 'XAH-1622B' was kept separate as 'XAH-1622#2' | r1c1 |
| warning | 2 | `duplicate_tag` | YI-1600#2 | tag 'YI-1600' is used by more than one item on this sheet; the copy 'YI-1600B' was kept separate as 'YI-1600#2' | r1c2 |
| warning | 2 | `possible_missed_tags` |  | 8 tags found by ocr are not in the graph: CP-1620-GRI, EL-16204, EL-16208, TTYPOF-2, LH-3A-00, ZC-3611, D-000, CHV-1051 |  |
| warning | 3 | `duplicate_tag` | HS-2000B#2 | tag 'HS-2000B' is used by more than one item on this sheet; the copy 'HS-2000B-MX' was kept separate as 'HS-2000B#2' | r1c4, r2c4 |
| warning | 3 | `duplicate_tag` | HS-2000B#3 | tag 'HS-2000B' is used by more than one item on this sheet; the copy 'HS-2000B' was kept separate as 'HS-2000B#3' | r1c4, r1c5 |
| warning | 3 | `duplicate_tag` | XAH-1721#2 | tag 'XAH-1721' is used by more than one item on this sheet; the copy 'XAH-1721B' was kept separate as 'XAH-1721#2' | r1c1, r1c2 |
| warning | 3 | `duplicate_tag` | XAH-1722#2 | tag 'XAH-1722' is used by more than one item on this sheet; the copy 'XAH-1722B' was kept separate as 'XAH-1722#2' | r1c1, r1c2 |
| warning | 3 | `duplicate_tag` | XS-1700#2 | tag 'XS-1700' is used by more than one item on this sheet; the copy 'XS-1700' was kept separate as 'XS-1700#2' | r1c3, r2c3 |
| warning | 3 | `possible_missed_tags` |  | 11 tags found by ocr are not in the graph: R-3L, ALARM-17008, FAULT-17018, FAULT-19008, EL-19008, HS-1000, AE-721, LT-3701, ARV-191S, RV-191S, SHEET-65 |  |
| warning | 4 | `duplicate_tag` | LALL-2301#2 | tag 'LALL-2301' is used by more than one item on this sheet; the copy 'LALL-2301' was kept separate as 'LALL-2301#2' | r1c2, r2c2 |
| warning | 4 | `possible_missed_tags` |  | 5 tags found by ocr are not in the graph: PLC-0001, HS-23104, HS-23106, BAV-23X, SHEET-66 |  |
| warning | 5 | `possible_missed_tags` |  | 38 tags found by ocr are not in the graph: HLZ-74, CP-2620A, CP-26OO-SBR, CP-2720A, EL-27208, EL-27204, HS-2630, HS-01, EL-2001A, HS-2401, EL-2810, HS-2510, EL-2430, EL-28018, M-01B, HOA-10, CP-26208, CP-27208, HS-2730, HS-2710, EL-2730, EL-27016, HS-2701, EL-2710, EL-27018, EL-2701A, EL-6200, EL-17200, SP-430KP, S-6R, UT-3111, UT-2601, SBR-1, ITF-2801, ARV-250, BUV-2706, HSW-00, FLOAT-1 |  |
| warning | 6 | `possible_missed_tags` |  | 12 tags found by ocr are not in the graph: XSO-3051, LA-301, HS-38208, TTYPOF-4, IYPOF-3, BUV-3021, BAV-3802, PRV-354, PSH-3622, IV-3821, LE-3001, DO-15 |  |
| warning | 7 | `possible_missed_tags` |  | 10 tags found by ocr are not in the graph: EL-3020, EL-3030, EL-3010, HS-0930, F-8S, WZ-7MO, CHV-3021, SER-2, CHV-3311, CHV-331 |  |
| warning | 8 | `possible_missed_tags` |  | 4 tags found by ocr are not in the graph: CP-26OO-SBR, TTYPOF-2, LSH-4901, IH-03 |  |
| warning | 9 | `possible_missed_tags` |  | 12 tags found by ocr are not in the graph: HS-48028, HS-03300, HS-4808, EL-5302, HS-4832, HS-4831, HS-4003, HS-47103, PI-4541, WEH-1, BAV-4631, SHEET-71 |  |
| warning | 10 | `possible_missed_tags` |  | 5 tags found by ocr are not in the graph: HS-55008, S-500A, S-5018, S-501B, CHV-5581 |  |
| info |  | `inferred_flow_direction` |  | 16 flow edges have inferred (not drawn) direction |  |
| info |  | `loop_no_sensor` | LOOP:F-5300 | control loop F-5300 has a controller but no sensor |  |
| info |  | `loop_no_sensor` | LOOP:S-3820 | control loop S-3820 has a controller but no sensor |  |
| info |  | `loop_no_sensor` | LOOP:S-4700 | control loop S-4700 has a controller but no sensor |  |
| info |  | `loop_no_sensor` | LOOP:S-4710 | control loop S-4710 has a controller but no sensor |  |
| info |  | `loop_no_sensor` | LOOP:S-5300 | control loop S-5300 has a controller but no sensor |  |
| info |  | `loop_no_sensor` | LOOP:S-5500 | control loop S-5500 has a controller but no sensor |  |
| info |  | `loop_no_sensor` | LOOP:Y-1600 | control loop Y-1600 has a controller but no sensor |  |
| info |  | `loop_no_sensor` | LOOP:Z-3201 | control loop Z-3201 has a controller but no sensor |  |
| info | 1 | `low_confidence` | FY-1200 | FY-1200 was read with confidence 0.50 | r1c1, r1c2 |
| info | 2 | `isolated_instrument` | EL-1640 | EL-1640 has no connections at all | r1c3 |
| info | 2 | `isolated_instrument` | XAH-1621#2 | XAH-1621#2 has no connections at all | r1c1 |
| info | 2 | `isolated_instrument` | XAH-1622#2 | XAH-1622#2 has no connections at all | r1c1 |
| info | 2 | `isolated_instrument` | YI-1600#2 | YI-1600#2 has no connections at all | r1c2 |
| info | 2 | `isolated_instrument` | ZH-1600 | ZH-1600 has no connections at all | r1c2 |
| info | 2 | `isolated_instrument` | XA-1600 | XA-1600 has no connections at all | r1c2 |
| info | 2 | `loop_no_signals` | YC-1600 | controller YC-1600 has no signal lines; loop Y-1600 built from tag numbers only | r1c2 |
| info | 2 | `loop_no_signals` | ZAC-1611 | controller ZAC-1611 has no signal lines; loop Z-1611 built from tag numbers only | r1c2 |
| info | 3 | `isolated_instrument` | HS-1700 | HS-1700 has no connections at all | r1c2, r1c3 |
| info | 3 | `isolated_instrument` | XAH-1721#2 | XAH-1721#2 has no connections at all | r1c1, r1c2 |
| info | 3 | `isolated_instrument` | XAH-1722#2 | XAH-1722#2 has no connections at all | r1c1, r1c2 |
| info | 4 | `isolated_instrument` | EL-2310 | EL-2310 has no connections at all | r1c3, r2c3 |
| info | 8 | `low_confidence` | P08.L_AAS3.1 | 150-AAS-H1 was read with confidence 0.50 |  |
| info | 9 | `isolated_instrument` | EL-5300 | EL-5300 has no connections at all | r1c2, r2c2 |
| info | 9 | `isolated_instrument` | HSI-4700 | HSI-4700 has no connections at all | r1c3 |
| info | 9 | `isolated_instrument` | XI-4800 | XI-4800 has no connections at all | r1c3 |
