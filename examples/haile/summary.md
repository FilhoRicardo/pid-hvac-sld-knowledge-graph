# haile: process knowledge graph summary

Built from `haile.pdf` (14 sheets) by pid-to-kg 0.1.0 on 2026-10-25. The graph has 958 nodes and 1240 edges; this summary covers equipment-level flow, instruments and control loops. Query `graph.duckdb` or `graph.json` for pipe-segment and valve detail.

| Equipment | Instruments | Valves & fittings | Pipe segments | Control loops | Off-page links |
|---|---|---|---|---|---|
| 70 | 70 | 222 | 460 | 26 | 74 |

## Sheets

| Page | Drawing | Title | Type |
|---|---|---|---|
| 1 | G-200 | Phase 0 1200 GPM Water Treatment Process Flow Diagram | pfd |
| 2 | 660-PI-200 | Phase 0 1200 GPM Water Treatment P&ID - 1st Stage Reaction Tank, Lime Reaction Tank | pid |
| 3 | 660-PI-201 | Phase 0 1200 GPM Water Treatment P&ID - Stage 1 Multiflow Clarifier | pid |
| 4 | 660-PI-202 | Phase 0 1200 GPM Water Treatment P&ID - Stage 1 Clearwell, Stage 2 Reaction Tank | pid |
| 5 | 660-PI-203 | Phase 0 1200 GPM Water Treatment P&ID - Lamella Clarifier, Lamella Transfer Pumps | pid |
| 6 | 660-PI-204 | Phase 0 1200 GPM Water Treatment P&ID - 2nd Stage Clearwell Tank and Transfer Pumps | pid |
| 7 | 660-PI-205 | Phase 0 1200 GPM Water Treatment P&ID - Microfiltration 660-MF-101 | pid |
| 8 | 660-PI-206 | Phase 0 1200 GPM Water Treatment P&ID - Microfiltration 660-MF-102 | pid |
| 9 | 660-PI-207 | Phase 0 1200 GPM Water Treatment P&ID - Backwash Tank & Adjust Tank | pid |
| 10 | 660-PI-208 | Phase 0 1200 GPM Water Treatment P&ID - Sludge Transfer Pump Box | pid |
| 11 | 660-PI-209 | Phase 0 1200 GPM Water Treatment P&ID - Treated Water Discharge Pump Box | pid |
| 12 | 660-PI-210 | Phase 0 1200 GPM Water Treatment P&ID - Oxidant Dosing, Ferric Chloride Dosing | pid |
| 13 | 660-PI-211 | Phase 0 1200 GPM Water Treatment P&ID - TMT 15 Dosing, Polymer Dosing | pid |
| 14 | 660-PI-212 | Phase 0 1200 GPM Water Treatment P&ID - SBS Dosing, Sulfuric Acid Dosing | pid |

## Process flow (equipment to equipment)

Each line reads *upstream → downstream*, with the pipe lines and in-line items between them. Pipes, valves and instruments are collapsed; use `kg_query.py path` for the full route.

- **COAGULANT** → **660-EQ-001** (TRAIN A MULTIFLO)
- **660-EQ-001** (TRAIN A MULTIFLO) → **660-PP-004** (Multiflo sludge pump): lines 4"-SG-660-001-SSB-NA, 4"-SG-660-018-SSB-NA; through gate valve
- **660-EQ-001** (TRAIN A MULTIFLO) → **660-PP-003** (Multiflo sludge pump): lines 4"-SG-660-001-SSB-NA; through manual valve
- **660-EQ-001** (TRAIN A MULTIFLO) → **660-TK-002** (1ST STAGE CLEARWELL): lines 14"-TW-660-002-CSG-NA, 14"-TW-660-002-PEA17-NA; crosses sheets
- **660-PP-004** (Multiflo sludge pump) → **660-BX-001** (SLUDGE TRANSFER BOX): lines 4"-SG-660-018-SSB-NA, 4"-SG-660-003-SSB-NA, 3"-SG-660-040-SSB-PF; through manual valve, gate valve, flexible hose, FE-0202#2; crosses sheets
- **660-PP-004** (Multiflo sludge pump) → **660-TK-008** (LIME REACTION TANK): lines 4"-SG-660-018-SSB-NA, 4"-SG-660-003-SSB-NA; through manual valve, gate valve, FE-0202; crosses sheets
- **660-PP-003** (Multiflo sludge pump) → **660-BX-001** (SLUDGE TRANSFER BOX): lines 4"-SG-660-003-SSB-NA, 3"-SG-660-040-SSB-PF; through manual valve, gate valve, flexible hose, FE-0202#2; crosses sheets
- **660-PP-003** (Multiflo sludge pump) → **660-TK-008** (LIME REACTION TANK): lines 4"-SG-660-003-SSB-NA; through manual valve, gate valve, FE-0202; crosses sheets
- **660-TK-002** (1ST STAGE CLEARWELL) → **660-PP-006**: lines 12"-TW-660-005-SSB-NA; through manual valve, reducer
- **660-TK-002** (1ST STAGE CLEARWELL) → **660-PP-005**: lines 12"-TW-660-004-SSB-NA; through manual valve, reducer
- **660-BX-001** (SLUDGE TRANSFER BOX) → **660-PP-029** (Sludge transfer pump): lines 4"-SG-660-016-HDPE-NA; through manual valve, reducer
- **660-BX-001** (SLUDGE TRANSFER BOX) → **660-PP-028** (Sludge transfer pump): lines 4"-SG-660-015-HDPE-NA; through manual valve, reducer
- **660-TK-008** (LIME REACTION TANK) → **Unlabelled outlet of 660-TK-008**
- **660-TK-008** (LIME REACTION TANK) → **660-TK-001** (1ST STAGE REACTION TANK): lines 8"-ML-660-001-CSG-NA
- **660-PP-006** → **660-TK-003** (2ND STAGE REACTION TANK): lines 12"-TW-660-007-PEA17-NA; through reducer, check valve, manual valve
- **660-PP-005** → **660-TK-003** (2ND STAGE REACTION TANK): lines 12"-TW-660-007-PEA17-NA; through reducer, check valve, manual valve
- **660-TK-001** (1ST STAGE REACTION TANK) → **660-EQ-001** (TRAIN A MULTIFLO): lines 14"-TW-660-001-CSG-NA; through FE-0201, sample point; crosses sheets
- **660-TK-003** (2ND STAGE REACTION TANK) → **660-EQ-002** (LAMELLA CLARIFIER): lines 12"-TW-660-008-PEA17-NA; through reducer; crosses sheets
- **660-EQ-002** (LAMELLA CLARIFIER) → **660-PP-012** (Lamella transfer pump): through reducer, flexible hose, manual valve, reducer
- **660-EQ-002** (LAMELLA CLARIFIER) → **660-PP-011** (Lamella transfer pump): through reducer, flexible hose, manual valve, reducer
- **660-EQ-002** (LAMELLA CLARIFIER) → **660-TK-004** (2ND STAGE CLEARWELL): lines 12"-TW-660-009-PEA17-NA; crosses sheets
- **660-PP-012** (Lamella transfer pump) → **660-BX-001** (SLUDGE TRANSFER BOX): lines 2"-SG-660-007-SSB-ET, 2"-SG-660-008-SSB-ET; through reducer, check valve, manual valve, manual valve, flexible hose, FE-0502#2, manual valve; crosses sheets
- **660-PP-012** (Lamella transfer pump) → **660-TK-003** (2ND STAGE REACTION TANK): lines 2"-SG-660-007-SSB-ET; through reducer, check valve, manual valve, FE-0502, manual valve; crosses sheets
- **660-PP-011** (Lamella transfer pump) → **660-BX-001** (SLUDGE TRANSFER BOX): lines 2"-SG-660-007-SSB-ET, 2"-SG-660-008-SSB-ET; through reducer, check valve, manual valve, manual valve, flexible hose, FE-0502#2, manual valve; crosses sheets
- **660-PP-011** (Lamella transfer pump) → **660-TK-003** (2ND STAGE REACTION TANK): lines 2"-SG-660-007-SSB-ET; through reducer, check valve, manual valve, FE-0502, manual valve; crosses sheets
- **660-TK-004** (2ND STAGE CLEARWELL) → **660-PP-010** (Clearwell transfer pump): lines 12"-TW-660-012-SSB-NA; through manual valve, reducer
- **660-TK-004** (2ND STAGE CLEARWELL) → **660-PP-009** (Clearwell transfer pump): lines 12"-TW-660-010-SSB-NA; through manual valve, reducer
- **660-PP-010** (Clearwell transfer pump) → **660-MF-101** (MF CONTAINER 55): lines 8"-TW-660-014-SSB-NA, 8"-PW-660-100-HDPE-NA, 8"-PW-660-101-HDPE-NA; through reducer, check valve, manual valve, manual valve, FE-0601, other, HV-102; crosses sheets
- **660-PP-010** (Clearwell transfer pump) → **660-MF-102** (MF CONTAINER 56): lines 8"-TW-660-014-SSB-NA, 8"-PW-660-100-HDPE-NA; through reducer, check valve, manual valve, manual valve, FE-0601, other, HV-102; crosses sheets
- **660-PP-009** (Clearwell transfer pump) → **660-MF-101** (MF CONTAINER 55): lines 8"-TW-660-014-SSB-NA, 8"-PW-660-100-HDPE-NA, 8"-PW-660-101-HDPE-NA; through reducer, check valve, manual valve, manual valve, FE-0601, other, HV-102; crosses sheets
- **660-PP-009** (Clearwell transfer pump) → **660-MF-102** (MF CONTAINER 56): lines 8"-TW-660-014-SSB-NA, 8"-PW-660-100-HDPE-NA; through reducer, check valve, manual valve, manual valve, FE-0601, other, HV-102; crosses sheets
- **660-MF-101** (MF CONTAINER 55) → **660-S-100** (SUMP): lines 4"-WW-660-110-HDPE-NA; crosses sheets
- **660-MF-101** (MF CONTAINER 55) → **660-TK-004** (2ND STAGE CLEARWELL): lines 6"-PW-660-109-HDPE-NA; crosses sheets
- **660-MF-101** (MF CONTAINER 55) → **660-TK-006** (BACKWASH TANK): lines 8"-FL-660-102-HDPE-NA; through other; crosses sheets
- **660-MF-102** (MF CONTAINER 56) → **660-S-100** (SUMP): lines 4"-WW-660-112-HDPE-NA, 4"-WW-660-110-HDPE-NA
- **660-MF-102** (MF CONTAINER 56) → **660-TK-004** (2ND STAGE CLEARWELL): lines 6"-PW-660-111-HDPE-NA, 6"-PW-660-109-HDPE-NA; crosses sheets
- **660-MF-102** (MF CONTAINER 56) → **660-TK-006** (BACKWASH TANK): lines 8"-FL-660-103-HDPE-NA, 8"-FL-660-102-HDPE-NA; through other; crosses sheets
- **660-S-100** (SUMP) → **660-SP-102**
- **660-S-100** (SUMP) → **660-SP-101**
- **660-TK-006** (BACKWASH TANK) → **660-PP-014** (Backwash pump): lines 12"-BW-660-002-SSB-NA; through manual valve, reducer
- **660-TK-006** (BACKWASH TANK) → **660-PP-013** (Backwash pump): lines 12"-BW-660-001-SSB-NA; through manual valve, reducer
- **660-TK-006** (BACKWASH TANK) → **660-TK-007** (pH NEUTRALIZATION TANK): lines 12"-FL-660-030-PLB-NA
- **660-SP-102** → **POND-A-19** (POND A-19): lines 4"-WW-660-115-HDPE-NA, 4"-WW-660-114-HDPE-NA; through HV-105, CV-101; crosses sheets
- **660-SP-101** → **POND-A-19** (POND A-19): lines 4"-WW-660-114-HDPE-NA; through HV-104, CV-100; crosses sheets
- **660-PP-014** (Backwash pump) → **660-MF-101** (MF CONTAINER 55): lines 8"-BW-660-004-SSB-NA, 8"-FL-660-104-HDPE-NA, 6"-FL-660-105-HDPE-NA; through reducer, check valve, manual valve, FE-1101, other, HV-103, reducer; crosses sheets
- **660-PP-014** (Backwash pump) → **660-MF-102** (MF CONTAINER 56): lines 8"-BW-660-004-SSB-NA, 8"-FL-660-104-HDPE-NA, 6"-FL-660-104-HDPE-NA; through reducer, check valve, manual valve, FE-1101, other, HV-103, reducer; crosses sheets
- **660-PP-013** (Backwash pump) → **660-MF-101** (MF CONTAINER 55): lines 8"-BW-660-004-SSB-NA, 8"-FL-660-104-HDPE-NA, 6"-FL-660-105-HDPE-NA; through reducer, check valve, manual valve, FE-1101, other, HV-103, reducer; crosses sheets
- **660-PP-013** (Backwash pump) → **660-MF-102** (MF CONTAINER 56): lines 8"-BW-660-004-SSB-NA, 8"-FL-660-104-HDPE-NA, 6"-FL-660-104-HDPE-NA; through reducer, check valve, manual valve, FE-1101, other, HV-103, reducer; crosses sheets
- **660-TK-007** (pH NEUTRALIZATION TANK) → **660-BX-002** (TREATED WATER DISCHARGE PUMP BOX): lines 12"-TW-660-031-PLA-NA; crosses sheets
- **POND-A-19** (POND A-19) → **660-PP-002**
- **660-BX-002** (TREATED WATER DISCHARGE PUMP BOX) → **660-PP-017** (Treated water discharge pump): lines 12"-TW-660-032-SSB-NA; through manual valve, reducer
- **660-BX-002** (TREATED WATER DISCHARGE PUMP BOX) → **660-PP-018** (Treated water discharge pump): lines 12"-TW-660-033-SSB-NA; through manual valve, reducer
- **660-PP-002** → **660-TK-001** (1ST STAGE REACTION TANK): lines 14"-CW-050-042-PEA17-NA, 14"-TW-660-001-CSG-NA; through manual valve, reducer, FE-0101, reducer
- **660-PP-017** (Treated water discharge pump) → **TREATED WATER NPDES APPROVED DISCHARGE**: lines 10"-TW-660-036-PEA11-NA; through reducer, manual valve, manual valve, FE-1802
- **660-PP-018** (Treated water discharge pump) → **TREATED WATER NPDES APPROVED DISCHARGE**: lines 10"-TW-660-036-PEA11-NA; through reducer, manual valve, manual valve, FE-1802
- **MP feed (flag unlabelled)** → **660-TK-003** (2ND STAGE REACTION TANK): lines 1/2"-MP-660-005-PLB-ET
- **HW EXIST LINE POTABLE WATER** → **SBS make-down tank (untagged)**: lines 3/4"-TW-660-XXX-XXX-ET; through XV-1401, reducer, globe valve, FI-1401
- **HW EXIST LINE POTABLE WATER** → **Polymer make-down tank (untagged)**: lines 3/4"-TW-660-XXX-XXX-ET; through XV-1601, reducer, globe valve, FI-1601
- **HW EXIST LINE POTABLE WATER** → **660-CIP-101** (MF CIP): lines 2"-HW-660-140-HDPE-NA; through BFP-100, ACV-100
- **HW EXIST LINE POTABLE WATER** → **660-CIP-102** (MF CIP): lines 2"-HW-660-140-HDPE-NA; through BFP-100, ACV-101; crosses sheets
- **SBS make-down tank (untagged)** → **660-TK-004** (2ND STAGE CLEARWELL): lines 1/2"-CH-660-202-PE-NA; through In-line device drawn as box with zig-zag, ball valve, Tie-in TIE-03; crosses sheets
- **Polymer make-down tank (untagged)** → **660-EQ-002** (LAMELLA CLARIFIER): lines 1/2"-FC-660-013-PLB-ET, 3/4"-FC-660-013-PLB-ET; through In-line device drawn as box with zig-zag, ball valve, manual valve, gate valve; crosses sheets
- **PA EXIST LINE PLANT AIR** → **PLANT AIR TO EACH AOD PUMP**: lines 1"-PA-660-120-CS-NA
- **PA EXIST LINE PLANT AIR** → **660-MF-102** (MF CONTAINER 56): lines 1"-PA-660-120-CS-NA; crosses sheets
- **FROM EXIST MULTI MEDIA FILTERS** → **660-BX-001** (SLUDGE TRANSFER BOX): lines 8"-BW-660-015-SSB-NA
- **WATER TREATMENT PLANT SUMP** → **WATER TREATMENT PLANT SUMP PUMP**
- **WATER TREATMENT PLANT SUMP PUMP** → **660-BX-001** (SLUDGE TRANSFER BOX): lines 2"-SL-660-001-CSF-NA; crosses sheets
- **BLEACH drum** → **660-CP-103** (Bleach AOD pump)
- **660-CP-103** (Bleach AOD pump) → **660-CIP-102** (MF CIP): lines 5/8"-CH-660-132-PE-NA; through HV-111, CV-105; crosses sheets
- **660-CP-103** (Bleach AOD pump) → **660-CIP-101** (MF CIP): lines 5/8"-CH-660-132-PE-NA; through HV-110
- **CAUSTIC drum** → **660-CP-102** (Caustic AOD pump)
- **660-CP-102** (Caustic AOD pump) → **660-CIP-102** (MF CIP): lines 5/8"-CH-660-131-PE-NA; through HV-109, CV-104; crosses sheets
- **660-CP-102** (Caustic AOD pump) → **660-CIP-101** (MF CIP): lines 5/8"-CH-660-131-PE-NA; through HV-108
- **CITRIC ACID drum** → **660-CP-101** (Citric acid AOD pump)
- **660-CP-101** (Citric acid AOD pump) → **660-CIP-102** (MF CIP): lines 5/8"-CH-660-130-PE-NA; through HV-107, CV-103; crosses sheets
- **660-CP-101** (Citric acid AOD pump) → **660-CIP-101** (MF CIP): lines 5/8"-CH-660-130-PE-NA; through HV-106
- **OXIDANT TOTE** → **Polymer feed pump (untagged)**: lines 1/2"-FC-660-011-PLB-ET; through ball valve
- **Polymer feed pump (untagged)** → **Polymer make-down tank (untagged)**: through flexible hose
- **SBS TOTE** → **SBS feed pump (untagged)**: lines 1/2"-FC-660-002-PLB-ET; through ball valve
- **SBS feed pump (untagged)** → **SBS make-down tank (untagged)**: through flexible hose
- **OXIDANT tote** → **660-PP-202**: lines 1/2"-CO-660-001-PLB-ET; through ball valve, strainer, ball valve
- **OXIDANT tote** → **660-PP-201**: lines 1/2"-CO-660-001-PLB-ET; through ball valve, strainer, ball valve
- **660-PP-202** → **OXIDANT tote**: lines 1/2"-CH-660-200-PE-NA, 1/2"-CO-660-002-PLB-ET; through ball valve
- **660-PP-202** → **660-TK-001** (1ST STAGE REACTION TANK): lines 1/2"-CH-660-200-PE-NA, 14"-CW-050-042-PEA17-NA, 14"-TW-660-001-CSG-NA; through ball valve, PRV-1202, ball valve, manual valve, manual valve, reducer, FE-0101, reducer; crosses sheets
- **660-PP-201** → **OXIDANT tote**: lines 1/2"-CH-660-200-PE-NA, 1/2"-CO-660-002-PLB-ET; through ball valve
- **660-PP-201** → **660-TK-001** (1ST STAGE REACTION TANK): lines 1/2"-CH-660-200-PE-NA, 14"-CW-050-042-PEA17-NA, 14"-TW-660-001-CSG-NA; through ball valve, PRV-1202, ball valve, manual valve, manual valve, reducer, FE-0101, reducer; crosses sheets
- **FeCl3 TOTE** → **660-PP-020**: lines 1/2"-CO-660-001-PLB-ET; through ball valve, strainer, ball valve
- **FeCl3 TOTE** → **660-PP-019**: lines 1/2"-CO-660-001-PLB-ET; through ball valve, strainer, ball valve
- **660-PP-020** → **FeCl3 TOTE**: lines 1/2"-CO-660-004-PLB-ET, 1/2"-CO-660-002-PLB-ET; through ball valve
- **660-PP-020** → **660-TK-001** (1ST STAGE REACTION TANK): lines 1/2"-CO-660-004-PLB-ET, 1/2"-CH-660-201-PE-NA; through ball valve, PRV-1202, ball valve, Tie-in TIE-02; crosses sheets
- **660-PP-019** → **FeCl3 TOTE**: lines 1/2"-CO-660-004-PLB-ET, 1/2"-CO-660-002-PLB-ET; through ball valve
- **660-PP-019** → **660-TK-001** (1ST STAGE REACTION TANK): lines 1/2"-CO-660-004-PLB-ET, 1/2"-CH-660-201-PE-NA; through ball valve, PRV-1202, ball valve, Tie-in TIE-02; crosses sheets
- **TMT 15 tote** → **660-PI-022**: lines 1/2"-CO-660-008-PLB-ET; through ball valve, strainer, ball valve
- **TMT 15 tote** → **660-PI-021**: lines 1/2"-CO-660-008-PLB-ET; through ball valve, strainer, ball valve
- **660-PI-022** → **TMT 15 tote**: lines 1/2"-CO-660-011-PLB-ET, 1/2"-CO-660-009-PLB-ET; through ball valve, ball valve
- **660-PI-022** → **660-TK-003** (2ND STAGE REACTION TANK): lines 1/2"-CO-660-011-PLB-ET; through ball valve, PRV-1301, ball valve; crosses sheets
- **660-PI-021** → **TMT 15 tote**: lines 1/2"-CO-660-011-PLB-ET, 1/2"-CO-660-009-PLB-ET; through ball valve, ball valve
- **660-PI-021** → **660-TK-003** (2ND STAGE REACTION TANK): lines 1/2"-CO-660-011-PLB-ET; through ball valve, PRV-1301, ball valve; crosses sheets
- **H2SO4 tote** → **660-PI-022**: lines 1/2"-CO-660-109-PLB-ET; through ball valve, strainer, ball valve
- **H2SO4 tote** → **660-PI-021**: lines 1/2"-CO-660-109-PLB-ET; through ball valve, strainer, ball valve
- **660-PI-022** → **H2SO4 tote**: lines 1/2"-CO-660-108-PLB-ET, 1/2"-CO-660-110-PLB-ET; through ball valve, ball valve
- **660-PI-022** → **660-TK-007** (pH NEUTRALIZATION TANK): lines 1/2"-CO-660-108-PLB-ET, 1/2"-SA-660-108-CSE-ET; through ball valve, PRV-1702, ball valve; crosses sheets
- **660-PI-021** → **H2SO4 tote**: lines 1/2"-CO-660-108-PLB-ET, 1/2"-CO-660-110-PLB-ET; through ball valve, ball valve
- **660-PI-021** → **660-TK-007** (pH NEUTRALIZATION TANK): lines 1/2"-CO-660-108-PLB-ET, 1/2"-SA-660-108-CSE-ET; through ball valve, PRV-1702, ball valve; crosses sheets

Drains, vents and overflows (not process flow):
- DRAIN (unlabelled) ← 660-BX-001, 660-BX-002, 660-EQ-002, 660-PP-028, 660-PP-029, 660-TK-002, 660-TK-004, 660-TK-006, Polymer make-down tank (untagged), SBS feed pump (untagged), SBS make-down tank (untagged)
- DRAIN TO SUMP ← 660-EQ-001
- VENT (MF CIP) ← 660-CIP-101, 660-CIP-102

## Equipment

| Tag | Kind | Description | Fed by | Feeds | Status | Sheets |
|---|---|---|---|---|---|---|
| 1st stage clearwell transfer pump (untagged on PFD) | centrifugal_pump | 1st stage clearwell transfer pump (untagged on PFD) |  |  |  | G-200 |
| 2nd stage clearwell transfer pump (untagged on PFD) | centrifugal_pump | 2nd stage clearwell transfer pump (untagged on PFD) |  |  |  | G-200 |
| 660-BX-001 | box | SLUDGE TRANSFER BOX | 660-PP-003, 660-PP-004, 660-PP-011, 660-PP-012, FROM EXIST MULTI MEDIA FILTERS, WATER TREATMENT PLANT SUMP PUMP | 660-PP-028, 660-PP-029, DRAIN (unlabelled) |  | 660-PI-208 |
| 660-BX-002 | box | TREATED WATER DISCHARGE PUMP BOX | 660-TK-007 | 660-PP-017, 660-PP-018, DRAIN (unlabelled) |  | 660-PI-209, G-200 |
| 660-CIP-101 | package_unit | MF CIP | 660-CP-101, 660-CP-102, 660-CP-103, HW EXIST LINE POTABLE WATER | VENT (MF CIP) |  | 660-PI-205 |
| 660-CIP-102 | package_unit | MF CIP | 660-CP-101, 660-CP-102, 660-CP-103, HW EXIST LINE POTABLE WATER | VENT (MF CIP) |  | 660-PI-206 |
| 660-CP-101 | positive_displacement_pump | Citric acid AOD pump | CITRIC ACID drum | 660-CIP-101, 660-CIP-102 |  | 660-PI-205 |
| 660-CP-102 | positive_displacement_pump | Caustic AOD pump | CAUSTIC drum | 660-CIP-101, 660-CIP-102 |  | 660-PI-205 |
| 660-CP-103 | positive_displacement_pump | Bleach AOD pump | BLEACH drum | 660-CIP-101, 660-CIP-102 |  | 660-PI-205 |
| 660-EQ-001 | clarifier | TRAIN A MULTIFLO | 660-TK-001, COAGULANT | 660-PP-003, 660-PP-004, 660-TK-002, DRAIN TO SUMP |  | 660-PI-201, G-200 |
| 660-EQ-002 | clarifier | LAMELLA CLARIFIER | 660-TK-003, Polymer make-down tank (untagged) | 660-PP-011, 660-PP-012, 660-TK-004, DRAIN (unlabelled) |  | 660-PI-203, G-200 |
| 660-MF-101 | membrane_filter | MF CONTAINER 55 | 660-PP-009, 660-PP-010, 660-PP-013, 660-PP-014 | 660-S-100, 660-TK-004, 660-TK-006 |  | 660-PI-205 |
| 660-MF-101/102 | membrane_filter | MF CONTAINER 55 & 56 |  |  |  | G-200 |
| 660-MF-102 | membrane_filter | MF CONTAINER 56 | 660-PP-009, 660-PP-010, 660-PP-013, 660-PP-014, PA EXIST LINE PLANT AIR | 660-S-100, 660-TK-004, 660-TK-006 |  | 660-PI-206 |
| 660-PI-021 | metering_pump |  | TMT 15 tote | 660-TK-003, TMT 15 tote |  | 660-PI-211 |
| 660-PI-021 | metering_pump |  | H2SO4 tote | 660-TK-007, H2SO4 tote |  | 660-PI-212 |
| 660-PI-022 | metering_pump |  | TMT 15 tote | 660-TK-003, TMT 15 tote |  | 660-PI-211 |
| 660-PI-022 | metering_pump |  | H2SO4 tote | 660-TK-007, H2SO4 tote |  | 660-PI-212 |
| 660-PP-002 | centrifugal_pump |  | POND-A-19 | 660-TK-001 |  | 660-PI-200 |
| 660-PP-003 | centrifugal_pump | Multiflo sludge pump | 660-EQ-001 | 660-BX-001, 660-TK-008 |  | 660-PI-201 |
| 660-PP-004 | centrifugal_pump | Multiflo sludge pump | 660-EQ-001 | 660-BX-001, 660-TK-008 |  | 660-PI-201 |
| 660-PP-005 | centrifugal_pump |  | 660-TK-002 | 660-TK-003 |  | 660-PI-202 |
| 660-PP-006 | centrifugal_pump |  | 660-TK-002 | 660-TK-003 |  | 660-PI-202 |
| 660-PP-009 | centrifugal_pump | Clearwell transfer pump | 660-TK-004 | 660-MF-101, 660-MF-102 |  | 660-PI-204 |
| 660-PP-010 | centrifugal_pump | Clearwell transfer pump | 660-TK-004 | 660-MF-101, 660-MF-102 |  | 660-PI-204 |
| 660-PP-011 | centrifugal_pump | Lamella transfer pump | 660-EQ-002 | 660-BX-001, 660-TK-003 |  | 660-PI-203 |
| 660-PP-012 | centrifugal_pump | Lamella transfer pump | 660-EQ-002 | 660-BX-001, 660-TK-003 |  | 660-PI-203 |
| 660-PP-013 | centrifugal_pump | Backwash pump | 660-TK-006 | 660-MF-101, 660-MF-102 |  | 660-PI-207 |
| 660-PP-014 | centrifugal_pump | Backwash pump | 660-TK-006 | 660-MF-101, 660-MF-102 |  | 660-PI-207 |
| 660-PP-017 | centrifugal_pump | Treated water discharge pump | 660-BX-002 | TREATED WATER NPDES APPROVED DISCHARGE |  | 660-PI-209 |
| 660-PP-018 | centrifugal_pump | Treated water discharge pump | 660-BX-002 | TREATED WATER NPDES APPROVED DISCHARGE |  | 660-PI-209 |
| 660-PP-019 | metering_pump |  | FeCl3 TOTE | 660-TK-001, FeCl3 TOTE |  | 660-PI-210 |
| 660-PP-020 | metering_pump |  | FeCl3 TOTE | 660-TK-001, FeCl3 TOTE |  | 660-PI-210 |
| 660-PP-028 | slurry_pump | Sludge transfer pump | 660-BX-001 | DRAIN (unlabelled) |  | 660-PI-208 |
| 660-PP-029 | slurry_pump | Sludge transfer pump | 660-BX-001 | DRAIN (unlabelled) |  | 660-PI-208 |
| 660-PP-201 | metering_pump |  | OXIDANT tote | 660-TK-001, OXIDANT tote |  | 660-PI-210 |
| 660-PP-202 | metering_pump |  | OXIDANT tote | 660-TK-001, OXIDANT tote |  | 660-PI-210 |
| 660-S-100 | sump | SUMP | 660-MF-101, 660-MF-102 | 660-SP-101, 660-SP-102 |  | 660-PI-206 |
| 660-SP-101 | sump_pump |  | 660-S-100 | POND-A-19 |  | 660-PI-206 |
| 660-SP-102 | sump_pump |  | 660-S-100 | POND-A-19 |  | 660-PI-206 |
| 660-TK-001 | agitated_tank | 1ST STAGE REACTION TANK | 660-PP-002, 660-PP-019, 660-PP-020, 660-PP-201, 660-PP-202, 660-TK-008 | 660-EQ-001 |  | 660-PI-200, G-200 |
| 660-TK-002 | tank | 1ST STAGE CLEARWELL | 660-EQ-001 | 660-PP-005, 660-PP-006, DRAIN (unlabelled) |  | 660-PI-202, G-200 |
| 660-TK-003 | agitated_tank | 2ND STAGE REACTION TANK | 660-PI-021, 660-PI-022, 660-PP-005, 660-PP-006, 660-PP-011, 660-PP-012, MP feed (flag unlabelled) | 660-EQ-002 |  | 660-PI-202, G-200 |
| 660-TK-004 | tank | 2ND STAGE CLEARWELL | 660-EQ-002, 660-MF-101, 660-MF-102, SBS make-down tank (untagged) | 660-PP-009, 660-PP-010, DRAIN (unlabelled) |  | 660-PI-204, G-200 |
| 660-TK-006 | tank | BACKWASH TANK | 660-MF-101, 660-MF-102 | 660-PP-013, 660-PP-014, 660-TK-007, DRAIN (unlabelled) |  | 660-PI-207 |
| 660-TK-007 | agitated_tank | pH NEUTRALIZATION TANK | 660-PI-021, 660-PI-022, 660-TK-006 | 660-BX-002 |  | 660-PI-207 |
| 660-TK-008 | agitated_tank | LIME REACTION TANK | 660-PP-003, 660-PP-004 | 660-TK-001, Unlabelled outlet of 660-TK-008 |  | 660-PI-200, G-200 |
| 660-TK-06 | tank | BACKWASH TANK |  |  |  | G-200 |
| 660-TK-07 | tank | pH ADJUST TANK |  |  |  | G-200 |
| BLEACH drum | tank | BLEACH drum |  | 660-CP-103 |  | 660-PI-205 |
| CAUSTIC drum | tank | CAUSTIC drum |  | 660-CP-102 |  | 660-PI-205 |
| CITRIC ACID drum | tank | CITRIC ACID drum |  | 660-CP-101 |  | 660-PI-205 |
| FeCl3 TOTE | tank | FeCl3 TOTE | 660-PP-019, 660-PP-020 | 660-PP-019, 660-PP-020 |  | 660-PI-210 |
| Feed pump (untagged on PFD) | centrifugal_pump | Feed pump (untagged on PFD) |  |  |  | G-200 |
| H2SO4 tote | tank | H2SO4 tote | 660-PI-021, 660-PI-022 | 660-PI-021, 660-PI-022 |  | 660-PI-212 |
| OXIDANT TOTE | tank | OXIDANT TOTE |  | Polymer feed pump (untagged) |  | 660-PI-211 |
| OXIDANT tote | tank | OXIDANT tote | 660-PP-201, 660-PP-202 | 660-PP-201, 660-PP-202 |  | 660-PI-210 |
| POND-A-19 | pond | POND A-19 | 660-SP-101, 660-SP-102 | 660-PP-002 |  | 660-PI-200, G-200 |
| Polymer feed pump (untagged) | metering_pump | Polymer feed pump (untagged) | OXIDANT TOTE | Polymer make-down tank (untagged) |  | 660-PI-211 |
| Polymer make-down tank (untagged) | agitated_tank | Polymer make-down tank (untagged) | HW EXIST LINE POTABLE WATER, Polymer feed pump (untagged) | 660-EQ-002, DRAIN (unlabelled) |  | 660-PI-211 |
| SBS TOTE | tank | SBS TOTE |  | SBS feed pump (untagged) |  | 660-PI-212 |
| SBS feed pump (untagged) | metering_pump | SBS feed pump (untagged) | SBS TOTE | DRAIN (unlabelled), SBS make-down tank (untagged) |  | 660-PI-212 |
| SBS make-down tank (untagged) | agitated_tank | SBS make-down tank (untagged) | HW EXIST LINE POTABLE WATER, SBS feed pump (untagged) | 660-TK-004, DRAIN (unlabelled) |  | 660-PI-212 |
| SUMP | sump | SUMP |  |  |  | G-200 |
| Sludge transfer pump (untagged on PFD) | centrifugal_pump | Sludge transfer pump (untagged on PFD) |  |  |  | G-200 |
| Sump pump (untagged on PFD) | sump_pump | Sump pump (untagged on PFD) |  |  |  | G-200 |
| TMT 15 tote | tank | TMT 15 tote | 660-PI-021, 660-PI-022 | 660-PI-021, 660-PI-022 |  | 660-PI-211 |
| Treated water discharge pump (untagged on PFD) | centrifugal_pump | Treated water discharge pump (untagged on PFD) |  |  |  | G-200 |
| WATER TREATMENT PLANT SUMP | sump | WATER TREATMENT PLANT SUMP |  | WATER TREATMENT PLANT SUMP PUMP |  | 660-PI-200 |
| WATER TREATMENT PLANT SUMP PUMP | sump_pump | WATER TREATMENT PLANT SUMP PUMP | WATER TREATMENT PLANT SUMP | 660-BX-001 |  | 660-PI-200 |

## Instruments

Location is where the instrument senses the process. Pipe locations read `line (upstream item -> downstream item)`.

| Tag | Variable | Function | Mounted | Senses | Loop |
|---|---|---|---|---|---|
| AE-0101@660-PI-200 | analysis | element | field | 660-TK-001 | A-0101@660-PI-200 |
| AE-0101@660-PI-202 | analysis | element | field | 660-TK-003 | A-0101@660-PI-202 |
| AE-0601 | analysis | element | field | 8"-TW-660-014-SSB-NA (manual valve -> manual valve) | A-0601 |
| AE-1001 | analysis | element | field | 660-TK-007 | A-1001 |
| AE-201 | analysis | element | field | 660-TK-001 | A-201 |
| AIT-0101@660-PI-200 | analysis | transmitter | field | 660-TK-001 | A-0101@660-PI-200 |
| AIT-0101@660-PI-202 | analysis | transmitter | field | 660-TK-003 | A-0101@660-PI-202 |
| AIT-0601 | analysis | transmitter | field | 8"-TW-660-014-SSB-NA (manual valve -> manual valve) | A-0601 |
| AIT-1001 | analysis | transmitter | field | 660-TK-007 | A-1001 |
| AIT-201 | analysis | transmitter | field | 660-TK-001 | A-201 |
| FE-0101 | flow | element | field | in-line on 14"-TW-660-001-CSG-NA (reducer -> reducer) |  |
| FE-0201 | flow | element | field | in-line on 14"-TW-660-001-CSG-NA (TW 1ST STAGE REACTION TANK 660-TK-001 -> sample point) | F-0201 |
| FE-0202 | flow | element | field | in-line on 4"-SG-660-003-SSB-NA (gate valve -> SLUDGE LIME REACTION TANK 660-TK-008) | F-0202 |
| FE-0202#2 | flow | element | field | in-line on 3"-SG-660-040-SSB-PF (flexible hose -> SG 660-BX-001) | F-0202#2 |
| FE-0502 | flow | element | field | in-line on 2"-SG-660-007-SSB-ET (manual valve -> manual valve) | F-0502 |
| FE-0502#2 | flow | element | field | in-line on 2"-SG-660-008-SSB-ET (flexible hose -> manual valve) | F-0502#2 |
| FE-0601 | flow | element | field | in-line on 8"-TW-660-014-SSB-NA (manual valve -> other) | F-0601 |
| FE-1101 | flow | element | field | in-line on 8"-BW-660-004-SSB-NA (manual valve -> other) | F-1101 |
| FE-1701 | flow | element | field | in-line on line (ball valve -> SLUDGE CYANIDE RECOVERY THICKENER FEED BOX 600-BX-001) | F-1701 |
| FE-1801 | flow | element | field | in-line on 8"-TW-660-038-PEA11-NA (manual valve -> TREATED WATER TRAIN A REACTION TANK 650-TK-001 (DISCHARGE BY-PASS)) | F-1801 |
| FE-1802 | flow | element | field | in-line on 10"-TW-660-036-PEA11-NA (manual valve -> TREATED WATER NPDES APPROVED DISCHARGE) | F-1802 |
| FE-1803 | flow | element | field | in-line on 10"-TW-660-037-CSG-NA (manual valve -> TREATED WATER CYANIDE RECOVERY THICKENER FEED BOX 600-BX-001) | F-1803 |
| FE-1804 | flow | element | field | in-line on line (manual valve -> TREATED WATER INTERNAL RECLAIM WATER TANK 650-TK-002) | F-1804 |
| FE-1805 | flow | element | field | in-line on 10"-TW-660-045-PEA11-NA (manual valve -> TREATED WATER 19 POND FLOW DISTRIBUTION BOX 050-BX-001) | F-1805 |
| FI-1401 | flow | indicator | field | in-line on 3/4"-TW-660-XXX-XXX-ET (globe valve -> SBS make-down tank (untagged)) | F-1401 |
| FI-1601 | flow | indicator | field | in-line on 3/4"-TW-660-XXX-XXX-ET (globe valve -> Polymer make-down tank (untagged)) | F-1601 |
| FIT-0201 | flow | transmitter | field | in-line on 14"-TW-660-001-CSG-NA (TW 1ST STAGE REACTION TANK 660-TK-001 -> sample point) | F-0201 |
| FIT-0202 | flow | transmitter | field | in-line on 4"-SG-660-003-SSB-NA (gate valve -> SLUDGE LIME REACTION TANK 660-TK-008) | F-0202 |
| FIT-0202#2 | flow | transmitter | field | in-line on 3"-SG-660-040-SSB-PF (flexible hose -> SG 660-BX-001) | F-0202#2 |
| FIT-0502 | flow | transmitter | field | in-line on 2"-SG-660-007-SSB-ET (manual valve -> manual valve) | F-0502 |
| FIT-0502#2 | flow | transmitter | field | in-line on 2"-SG-660-008-SSB-ET (flexible hose -> manual valve) | F-0502#2 |
| FIT-0601 | flow | transmitter | field | in-line on 8"-TW-660-014-SSB-NA (manual valve -> other) | F-0601 |
| FIT-1101 | flow | transmitter | field | in-line on 8"-BW-660-004-SSB-NA (manual valve -> other) | F-1101 |
| FIT-1701 | flow | transmitter | field | in-line on line (ball valve -> SLUDGE CYANIDE RECOVERY THICKENER FEED BOX 600-BX-001) | F-1701 |
| FIT-1801 | flow | transmitter | field | in-line on 8"-TW-660-038-PEA11-NA (manual valve -> TREATED WATER TRAIN A REACTION TANK 650-TK-001 (DISCHARGE BY-PASS)) | F-1801 |
| FIT-1802 | flow | transmitter | field | in-line on 10"-TW-660-036-PEA11-NA (manual valve -> TREATED WATER NPDES APPROVED DISCHARGE) | F-1802 |
| FIT-1803 | flow | transmitter | field | in-line on 10"-TW-660-037-CSG-NA (manual valve -> TREATED WATER CYANIDE RECOVERY THICKENER FEED BOX 600-BX-001) | F-1803 |
| FIT-1804 | flow | transmitter | field | in-line on line (manual valve -> TREATED WATER INTERNAL RECLAIM WATER TANK 650-TK-002) | F-1804 |
| FIT-1805 | flow | transmitter | field | in-line on 10"-TW-660-045-PEA11-NA (manual valve -> TREATED WATER 19 POND FLOW DISTRIBUTION BOX 050-BX-001) | F-1805 |
| FSH-1401 | flow | switch | field | 3/4"-TW-660-XXX-XXX-ET (FI-1401 -> SBS make-down tank (untagged)) | F-1401 |
| FSH-1601 | flow | switch | field | 3/4"-TW-660-XXX-XXX-ET (FI-1601 -> Polymer make-down tank (untagged)) | F-1601 |
| HHL |  | other | field | 660-S-100 |  |
| HL |  | other | field | 660-S-100 |  |
| LE-0101@660-PI-200 | level | element | field | 660-TK-001 | L-0101@660-PI-200 |
| LE-0101@660-PI-202 | level | element | field | 660-TK-003 | L-0101@660-PI-202 |
| LIT-0101@660-PI-200 | level | transmitter | field | 660-TK-001 | L-0101@660-PI-200 |
| LIT-0101@660-PI-202 | level | transmitter | field | 660-TK-003 | L-0101@660-PI-202 |
| LIT-0301 | level | transmitter | field | 660-TK-002 |  |
| LIT-0601 | level | transmitter | field | 660-TK-004 |  |
| LIT-1001 | level | transmitter | field | 660-TK-006 |  |
| LIT-1002 | level | transmitter | field | 660-TK-007 |  |
| LIT-1701 | level | transmitter | field | 660-BX-001 |  |
| LL |  | other | field | 660-S-100 |  |
| PI-0204 | pressure | indicator | field | 4"-SG-660-018-SSB-NA (660-PP-004 -> manual valve) |  |
| PI-0208 | pressure | indicator | field | 4"-SG-660-003-SSB-NA (660-PP-003 -> manual valve) |  |
| PI-0501 | pressure | indicator | field | line (check valve -> manual valve) |  |
| PI-0502@660-PI-202 | pressure | indicator | field | 12"-TW-660-007-PEA17-NA (check valve -> manual valve) |  |
| PI-0502@660-PI-202#2 | pressure | indicator | field | line (check valve -> manual valve) |  |
| PI-0502@660-PI-203 | pressure | indicator | field | 2"-SG-660-007-SSB-ET (check valve -> manual valve) |  |
| PI-0602 | pressure | indicator | field | 8"-TW-660-014-SSB-NA (check valve -> manual valve) |  |
| PI-0602#2 | pressure | indicator | field | line (check valve -> manual valve) |  |
| PI-1102 | pressure | indicator | field | 8"-BW-660-004-SSB-NA (check valve -> manual valve) |  |
| PI-1102#2 | pressure | indicator | field | line (check valve -> manual valve) |  |
| PI-1202 | pressure | indicator | field | 1/2"-CH-660-200-PE-NA (ball valve -> PRV-1202) | P-1202 |
| PI-1202#2 | pressure | indicator | field | 1/2"-CO-660-004-PLB-ET (ball valve -> PRV-1202) |  |
| PI-1301 | pressure | indicator | field | 1/2"-CO-660-011-PLB-ET (ball valve -> PRV-1301) | P-1301 |
| PI-1401 | pressure | indicator | field | 1/2"-CH-660-202-PE-NA (SBS make-down tank (untagged) -> In-line device drawn as box with zig-zag) |  |
| PI-1601 | pressure | indicator | field | 1/2"-FC-660-013-PLB-ET (Polymer make-down tank (untagged) -> In-line device drawn as box with zig-zag) |  |
| PI-1702 | pressure | indicator | field | 1/2"-CO-660-108-PLB-ET (ball valve -> PRV-1702) | P-1702 |
| PIT-100 | pressure | transmitter | field | 8"-PW-660-100-HDPE-NA (HV-102 -> PW 660-MF-102) |  |

## Control loops

| Loop | Type | Sensor(s) | Controller(s) | Final element(s) | Description |
|---|---|---|---|---|---|
| A-0101@660-PI-200 | control | AE-0101@660-PI-200, AIT-0101@660-PI-200 |  | ACV-0101 | Control loop A-0101@660-PI-200 (analysis). Sensed by AE-0101@660-PI-200, AIT-0101@660-PI-200 (660-TK-001). Acts on ACV-0101 on 1"-ML-800-016-CSF-ET. |
| A-0101@660-PI-202 | monitoring | AIT-0101@660-PI-202, AE-0101@660-PI-202 |  |  | Monitoring loop A-0101@660-PI-202 (analysis). Sensed by AIT-0101@660-PI-202, AE-0101@660-PI-202 (660-TK-003). |
| A-0601 | monitoring | AE-0601, AIT-0601 |  |  | Monitoring loop A-0601 (analysis). Sensed by AE-0601, AIT-0601 (8"-TW-660-014-SSB-NA (manual valve -> manual valve)). |
| A-1001 | monitoring | AE-1001, AIT-1001 |  |  | Monitoring loop A-1001 (analysis). Sensed by AE-1001, AIT-1001 (660-TK-007). |
| A-201 | monitoring | AE-201, AIT-201 |  |  | Monitoring loop A-201 (analysis). Sensed by AE-201, AIT-201 (660-TK-001). |
| F-0201 | monitoring | FE-0201, FIT-0201 |  |  | Monitoring loop F-0201 (flow). Sensed by FE-0201, FIT-0201 (in-line on 14"-TW-660-001-CSG-NA (TW 1ST STAGE REACTION TANK 660-TK-001 -> sample point)). |
| F-0202 | monitoring | FE-0202, FIT-0202 |  |  | Monitoring loop F-0202 (flow). Sensed by FE-0202, FIT-0202 (in-line on 4"-SG-660-003-SSB-NA (gate valve -> SLUDGE LIME REACTION TANK 660-TK-008)). |
| F-0202#2 | monitoring | FE-0202#2, FIT-0202#2 |  |  | Monitoring loop F-0202#2 (flow). Sensed by FE-0202#2, FIT-0202#2 (in-line on 3"-SG-660-040-SSB-PF (flexible hose -> SG 660-BX-001)). |
| F-0502 | monitoring | FE-0502, FIT-0502 |  |  | Monitoring loop F-0502 (flow). Sensed by FE-0502, FIT-0502 (in-line on 2"-SG-660-007-SSB-ET (manual valve -> manual valve)). |
| F-0502#2 | monitoring | FE-0502#2, FIT-0502#2 |  |  | Monitoring loop F-0502#2 (flow). Sensed by FE-0502#2, FIT-0502#2 (in-line on 2"-SG-660-008-SSB-ET (flexible hose -> manual valve)). |
| F-0601 | monitoring | FE-0601, FIT-0601 |  |  | Monitoring loop F-0601 (flow). Sensed by FE-0601, FIT-0601 (in-line on 8"-TW-660-014-SSB-NA (manual valve -> other)). |
| F-1101 | monitoring | FE-1101, FIT-1101 |  |  | Monitoring loop F-1101 (flow). Sensed by FE-1101, FIT-1101 (in-line on 8"-BW-660-004-SSB-NA (manual valve -> other)). |
| F-1401 | monitoring | FI-1401, FSH-1401 |  |  | Monitoring loop F-1401 (flow). Sensed by FI-1401, FSH-1401 (in-line on 3/4"-TW-660-XXX-XXX-ET (globe valve -> SBS make-down tank (untagged)); 3/4"-TW-660-XXX-XXX-ET (FI-1401 -> SBS make-down tank (untagged))). |
| F-1601 | monitoring | FI-1601, FSH-1601 |  |  | Monitoring loop F-1601 (flow). Sensed by FI-1601, FSH-1601 (in-line on 3/4"-TW-660-XXX-XXX-ET (globe valve -> Polymer make-down tank (untagged)); 3/4"-TW-660-XXX-XXX-ET (FI-1601 -> Polymer make-down tank (untagged))). |
| F-1701 | monitoring | FE-1701, FIT-1701 |  |  | Monitoring loop F-1701 (flow). Sensed by FE-1701, FIT-1701 (in-line on line (ball valve -> SLUDGE CYANIDE RECOVERY THICKENER FEED BOX 600-BX-001)). |
| F-1801 | monitoring | FE-1801, FIT-1801 |  |  | Monitoring loop F-1801 (flow). Sensed by FE-1801, FIT-1801 (in-line on 8"-TW-660-038-PEA11-NA (manual valve -> TREATED WATER TRAIN A REACTION TANK 650-TK-001 (DISCHARGE BY-PASS))). |
| F-1802 | monitoring | FE-1802, FIT-1802 |  |  | Monitoring loop F-1802 (flow). Sensed by FE-1802, FIT-1802 (in-line on 10"-TW-660-036-PEA11-NA (manual valve -> TREATED WATER NPDES APPROVED DISCHARGE)). |
| F-1803 | monitoring | FE-1803, FIT-1803 |  |  | Monitoring loop F-1803 (flow). Sensed by FE-1803, FIT-1803 (in-line on 10"-TW-660-037-CSG-NA (manual valve -> TREATED WATER CYANIDE RECOVERY THICKENER FEED BOX 600-BX-001)). |
| F-1804 | monitoring | FE-1804, FIT-1804 |  |  | Monitoring loop F-1804 (flow). Sensed by FE-1804, FIT-1804 (in-line on line (manual valve -> TREATED WATER INTERNAL RECLAIM WATER TANK 650-TK-002)). |
| F-1805 | monitoring | FE-1805, FIT-1805 |  |  | Monitoring loop F-1805 (flow). Sensed by FE-1805, FIT-1805 (in-line on 10"-TW-660-045-PEA11-NA (manual valve -> TREATED WATER 19 POND FLOW DISTRIBUTION BOX 050-BX-001)). |
| L-0101@660-PI-200 | monitoring | LE-0101@660-PI-200, LIT-0101@660-PI-200 |  |  | Monitoring loop L-0101@660-PI-200 (level). Sensed by LE-0101@660-PI-200, LIT-0101@660-PI-200 (660-TK-001). |
| L-0101@660-PI-202 | monitoring | LIT-0101@660-PI-202, LE-0101@660-PI-202 |  |  | Monitoring loop L-0101@660-PI-202 (level). Sensed by LIT-0101@660-PI-202, LE-0101@660-PI-202 (660-TK-003). |
| P-1201 | monitoring |  |  |  | Monitoring loop P-1201 (pressure). |
| P-1202 | monitoring | PI-1202 |  |  | Monitoring loop P-1202 (pressure). Sensed by PI-1202 (1/2"-CH-660-200-PE-NA (ball valve -> PRV-1202)). |
| P-1301 | monitoring | PI-1301 |  |  | Monitoring loop P-1301 (pressure). Sensed by PI-1301 (1/2"-CO-660-011-PLB-ET (ball valve -> PRV-1301)). |
| P-1702 | monitoring | PI-1702 |  |  | Monitoring loop P-1702 (pressure). Sensed by PI-1702 (1/2"-CO-660-108-PLB-ET (ball valve -> PRV-1702)). |

## Off-page connections

| Sheet | Connector | Direction | Other drawing | Linked to |
|---|---|---|---|---|
| 660-PI-200 | TW SLUDGE DISPOSAL PUMP BOX 660-BX-001 | out | 660-PI-208 | FROM EXIST SUMP PUMP (660-PI-208) |
| 660-PI-200 | TW TREATED WATER DISCHARGE PUMPS 660-PP-017/018 (DISCHARGE BYPASS) | in | 660-PI-209 | unmatched |
| 660-PI-200 | CONTACT WATER | out | 600-PI-001 | unmatched |
| 660-PI-200 | TW 660-EQ-001 | out | 660-PI-201 | TW 1ST STAGE REACTION TANK 660-TK-001 (660-PI-201) |
| 660-PI-200 | CH FERRIC CHLORIDE | in | 660-PI-210 | CH 660-TK-001 (ferric chloride) (660-PI-210) |
| 660-PI-200 | MILK OF LIME FEED LOOP | in | 800-PI-016 | unmatched |
| 660-PI-200 | CH NaOCl (OXIDANT) | in | 660-PI-210 | CH 660-TK-001 (oxidant) (660-PI-210) |
| 660-PI-200 | SLUDGE - MULTIFLO SLUDGE RECYCLE | in | 660-PI-201 | SLUDGE LIME REACTION TANK 660-TK-008 (660-PI-201) |
| 660-PI-201 | SG 660-BX-001 | out | 660-PI-208 | SG 660-EQ-001 (660-PI-208) |
| 660-PI-201 | TW 1ST STAGE REACTION TANK 660-TK-001 | in | 660-PI-200 | TW 660-EQ-001 (660-PI-200) |
| 660-PI-201 | TW 660-TK-002 | out | 660-PI-202 | TW 660-EQ-001 (660-PI-202) |
| 660-PI-201 | SLUDGE LIME REACTION TANK 660-TK-008 | out | 660-PI-200 | SLUDGE - MULTIFLO SLUDGE RECYCLE (660-PI-200) |
| 660-PI-202 | TW 660-PI-203 | out | 660-PI-203 | TW 660-TK-003 (660-PI-203) |
| 660-PI-202 | TW 660-EQ-001 | in | 660-PI-201 | TW 660-TK-002 (660-PI-201) |
| 660-PI-202 | SLUDGE - LAMELLA SLUDGE RECYCLE | in | 660-PI-203 | SG 660-PI-202 (660-PI-203) |
| 660-PI-202 | MILK OF LIME - LIME FEED LOOP | in | 800-PI-016 | unmatched |
| 660-PI-202 | METAL PRECIPITANT TMT-15 | in | 660-PI-211 | CH 660-TK-003 (TMT-15) (660-PI-211) |
| 660-PI-203 | SG 660-PI-202 | out | 660-PI-202 | SLUDGE - LAMELLA SLUDGE RECYCLE (660-PI-202) |
| 660-PI-203 | SG 660-BX-001 | out | 660-PI-208 | SG 660-EQ-002 (660-PI-208) |
| 660-PI-203 | CH POLYMER | in | 660-PI-211 | CH 660-EQ-002 (polymer) (660-PI-211) |
| 660-PI-203 | TW 660-TK-003 | in | 660-PI-202 | TW 660-PI-203 (660-PI-202) |
| 660-PI-203 | TW 660-TK-004 | out | 660-PI-204 | TW 660-EQ-002 (660-PI-204) |
| 660-PI-204 | TW 660-EQ-002 | in | 660-PI-203 | TW 660-TK-004 (660-PI-203) |
| 660-PI-204 | TW 660-MF-101/102 | out | 660-PI-205 | PW 660-PI-204 8"-TW-660-014-SSB-NA (660-PI-205) |
| 660-PI-204 | CH SBS SUPPLY | in | 660-PI-202A | CH 660-TK-004 (SBS) (660-PI-212) |
| 660-PI-204 | PW 660-MF-101/102 (XR) | in | 660-PI-206 | PW 660-TK-004 (XR) (660-PI-206) |
| 660-PI-205 | WW 660-S-100 (AS/RF) | out | 660-PI-206 | WW MF-101 (660-PI-206) |
| 660-PI-205 | CH BLEACH | out | 660-PI-206 | CH BLEACH (660-PI-206) |
| 660-PI-205 | CH CAUSTIC | out | 660-PI-206 | CH CAUSTIC (660-PI-206) |
| 660-PI-205 | WW 660-S-100 (CIP DRAIN) | out | 660-PI-206 | WW MF-101 (660-PI-206) |
| 660-PI-205 | WW 660-S-100 (CIP OVERFLOW) | out | 660-PI-206 | WW CIP OVERFLOW (660-PI-206) |
| 660-PI-205 | CH CITRIC | out | 660-PI-206 | CH CITRIC (660-PI-206) |
| 660-PI-205 | PW 660-PI-204 8"-TW-660-014-SSB-NA | in | 660-PI-204 | TW 660-MF-101/102 (660-PI-204) |
| 660-PI-205 | FL 660-MF-102 (FILTRATE) | out | 660-PI-206 | FL MF-101 (660-PI-206) |
| 660-PI-205 | FL 660-MF-102 | out | 660-PI-206 | FL 660-PU-13/14 (660-PI-206) |
| 660-PI-205 | FL 660-PU-13/14 | in | 660-PI-208 | FL MF-101/102 (backwash) (660-PI-207) |
| 660-PI-205 | HW POTABLE | out | 660-PI-206 | HW POTABLE WATER (660-PI-206) |
| 660-PI-205 | PW 660-MF-102 | out | 660-PI-206 | PW 660-PP-009/010 (660-PI-206) |
| 660-PI-205 | PA 660-MF-102 | out | 660-PI-206 | 660-MF-102 (660-PI-206) |
| 660-PI-205 | PW 660-TK-004 (XR) | out | 660-PI-206 | PW MF-101 (660-PI-206) |
| 660-PI-206 | WW MF-101 | in | 660-PI-205 | WW 660-S-100 (AS/RF) (660-PI-205) |
| 660-PI-206 | CH BLEACH | in | 660-PI-205 | CH BLEACH (660-PI-205) |
| 660-PI-206 | CH CAUSTIC | in | 660-PI-205 | CH CAUSTIC (660-PI-205) |
| 660-PI-206 | WW MF-101 | in | 660-PI-205 | WW 660-S-100 (CIP DRAIN) (660-PI-205) |
| 660-PI-206 | WW CIP OVERFLOW | in | 660-PI-205 | WW 660-S-100 (CIP OVERFLOW) (660-PI-205) |
| 660-PI-206 | CH CITRIC | in | 660-PI-205 | CH CITRIC (660-PI-205) |
| 660-PI-206 | PW 660-PP-009/010 | in | 660-PI-205 | PW 660-MF-102 (660-PI-205) |
| 660-PI-206 | FL MF-101 | in | 660-PI-205 | FL 660-MF-102 (FILTRATE) (660-PI-205) |
| 660-PI-206 | FL 660-PU-13/14 | in | 660-PI-205 | FL 660-MF-102 (660-PI-205) |
| 660-PI-206 | HW POTABLE WATER | in | 660-PI-205 | HW POTABLE (660-PI-205) |
| 660-PI-206 | TO POND A-19 | out |  | POND-A-19 (660-PI-200, G-200) |
| 660-PI-206 | PW 660-TK-004 (XR) | out | 660-PI-204 | PW 660-MF-101/102 (XR) (660-PI-204) |
| 660-PI-206 | FL 660-TK-006 (FILTRATE) | out | 660-PI-207 | CH MF-101/102 (filtrate) (660-PI-207) |
| 660-PI-206 | PW MF-101 | in | 660-PI-205 | PW 660-TK-004 (XR) (660-PI-205) |
| 660-PI-207 | TE 660-BX-002 | out | 660-PI-209 | TW 660-TK-007 (660-PI-209) |
| 660-PI-207 | CH MF-101/102 (filtrate) | in | 660-PI-206 | FL 660-TK-006 (FILTRATE) (660-PI-206) |
| 660-PI-207 | FL MF-101/102 (backwash) | out | 660-PI-205 | FL 660-PU-13/14 (660-PI-205) |
| 660-PI-207 | CH pH ADJUST | in | 660-PI-212 | CH 660-TK-007 (sulfuric acid) (660-PI-212) |
| 660-PI-208 | SG 660-EQ-001 | in | 660-PI-201 | SG 660-BX-001 (660-PI-201) |
| 660-PI-208 | SG 660-EQ-002 | in | 660-PI-203 | SG 660-BX-001 (660-PI-203) |
| 660-PI-208 | SLUDGE PROCESS EVENTS POND | out | 600-PI-005 | unmatched |
| 660-PI-208 | FROM EXIST SUMP PUMP | in | 660-PI-200 | TW SLUDGE DISPOSAL PUMP BOX 660-BX-001 (660-PI-200) |
| 660-PI-208 | SLUDGE CYANIDE RECOVERY THICKENER FEED BOX 600-BX-001 | out | 600-PI-001 | unmatched |
| 660-PI-209 | TREATED WATER 19 POND FLOW DISTRIBUTION BOX 050-BX-001 | out | 050-PI-004 | unmatched |
| 660-PI-209 | TREATED WATER CYANIDE RECOVERY THICKENER FEED BOX 600-BX-001 | out | 600-PI-001 | unmatched |
| 660-PI-209 | TREATED WATER INTERNAL RECLAIM WATER TANK 650-TK-002 | out | 650-PI-002 | unmatched |
| 660-PI-209 | TREATED WATER TRAIN A REACTION TANK 650-TK-001 (DISCHARGE BY-PASS) | out | 660-PI-001 | unmatched |
| 660-PI-209 | TW 660-TK-007 | in | 660-PI-208 | TE 660-BX-002 (660-PI-207) |
| 660-PI-210 | CH 660-TK-001 (ferric chloride) | out | 660-PI-200 | CH FERRIC CHLORIDE (660-PI-200) |
| 660-PI-210 | CH 660-TK-001 (oxidant) | out | 660-PI-200 | CH NaOCl (OXIDANT) (660-PI-200) |
| 660-PI-211 | CH 660-EQ-002 (polymer) | out | 660-PI-203 | CH POLYMER (660-PI-203) |
| 660-PI-211 | CH 660-TK-003 (TMT-15) | out | 660-PI-202 | METAL PRECIPITANT TMT-15 (660-PI-202) |
| 660-PI-212 | CH 660-TK-007 (sulfuric acid) | out | 660-PI-207 | CH pH ADJUST (660-PI-207) |
| 660-PI-212 | CH 660-TK-004 (SBS) | out | 660-PI-204 | CH SBS SUPPLY (660-PI-204) |

## Data quality

0 errors, 28 warnings and 22 informational items; see `qa_report.md`. Every node carries `confidence` and the sheet region it was read from (`provenance`). This graph was machine-extracted from drawings and must be verified by a qualified engineer before use in design, operations or safety work.
