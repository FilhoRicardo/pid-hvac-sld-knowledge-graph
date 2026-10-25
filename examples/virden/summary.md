# virden: process knowledge graph summary

Built from `virden.pdf` (10 sheets) by pid-to-kg 0.1.0 on 2026-10-25. The graph has 1699 nodes and 2538 edges; this summary covers equipment-level flow, instruments and control loops. Query `graph.duckdb` or `graph.json` for pipe-segment and valve detail.

| Equipment | Instruments | Valves & fittings | Pipe segments | Control loops | Off-page links |
|---|---|---|---|---|---|
| 87 | 452 | 342 | 574 | 164 | 36 |

## Sheets

| Page | Drawing | Title | Type |
|---|---|---|---|
| 1 | D-007-0 | Process Headworks P&ID (Virden Phase 2 Wastewater Treatment Facility Upgrades) | pid |
| 2 | D-008-0 | Process Septage Receiving Station P&ID | pid |
| 3 | D-009-0 | Process Grit Removal P&ID | pid |
| 4 | D-010-0 | Process Plant Lift Station P&ID | pid |
| 5 | D-011-0 | Process SBR and Equalization Tank P&ID | pid |
| 6 | D-012-0 | Process UV and Plant Service Water Station P&ID | pid |
| 7 | D-013-0 | Process Blowers P&ID | pid |
| 8 | D-014-0 | Process Digesters P&ID | pid |
| 9 | D-015-0 | Process Sludge Dewatering P&ID | pid |
| 10 | D-016-0 | Process Alum P&ID | pid |

## Process flow (equipment to equipment)

Each line reads *upstream → downstream*, with the pipe lines and in-line items between them. Pipes, valves and instruments are collapsed; use `kg_query.py path` for the full route.

- **HW HOT WATER SYSTEM** → **FIL-1101** (EXISTING SALSNES FILTER PACKAGE): lines 15-HW-H1; through BAV-1102, STR-1102, NEV-1102
- **FIL-1101** (EXISTING SALSNES FILTER PACKAGE) → **DRN TO SUMP PUMP**: lines 100-DRN-H1; through GAV-1101, PLV-1004
- **FIL-1101** (EXISTING SALSNES FILTER PACKAGE) → **SCP-1101** (SLUDGE SCREW)
- **FIL-1101** (EXISTING SALSNES FILTER PACKAGE) → **TK-2300** (WET WELL #2): lines 400-OF-E1, 400-RWW-H1, 400-PPE-E1, 300-PPE-E1; through KGV-1702, reducer, KGV-2301; crosses sheets
- **FIL-1101** (EXISTING SALSNES FILTER PACKAGE) → **TK-2200** (WET WELL #1): lines 400-OF-E1, 400-RWW-H1, 400-PPE-E1, 300-PPE-E1; through KGV-1702, KGV-2201; crosses sheets
- **FIL-1101** (EXISTING SALSNES FILTER PACKAGE) → **GCB-1700** (Grit chamber (vortex) with mixer MX-1701): lines 400-OF-E1, 400-RWW-H1; through KGV-1701; crosses sheets
- **SCP-1101** (SLUDGE SCREW) → **DRN TO SUMP PUMP**: lines 100-DRN-H1; through PLV-1005
- **SCP-1101** (SLUDGE SCREW) → **BIN-1102** (Sludge bin)
- **TK-2300** (WET WELL #2) → **RWP-2330** (RAW SEWAGE PUMP #3): lines 250-PPE-E1, 200-PPE-E1; through KGV-2306, KGV-2331, reducer
- **TK-2300** (WET WELL #2) → **RWP-2320** (RAW SEWAGE PUMP #2): lines 250-PPE-E1, 200-PPE-E1; through KGV-2306, KGV-2321, reducer
- **TK-2300** (WET WELL #2) → **RWP-2310** (RAW SEWAGE PUMP #1): lines 250-PPE-E1; through KGV-2306, KGV-2311, reducer
- **TK-2300** (WET WELL #2) → **PSF-3300** (PARSHALL FLUME): lines 400-OV-E1; crosses sheets
- **TK-2200** (WET WELL #1) → **RWP-2330** (RAW SEWAGE PUMP #3): lines 250-PPE-H1, 250-PPE-E1, 200-PPE-E1; through KGV-2206, KGV-2306, KGV-2331, reducer
- **TK-2200** (WET WELL #1) → **RWP-2320** (RAW SEWAGE PUMP #2): lines 250-PPE-H1, 250-PPE-E1, 200-PPE-E1; through KGV-2206, KGV-2306, KGV-2321, reducer
- **TK-2200** (WET WELL #1) → **RWP-2310** (RAW SEWAGE PUMP #1): lines 250-PPE-H1, 250-PPE-E1; through KGV-2206, KGV-2306, KGV-2311, reducer
- **TK-2200** (WET WELL #1) → **TK-2300** (WET WELL #2)
- **GCB-1700** (Grit chamber (vortex) with mixer MX-1701) → **GTP-1920** (Grit pump): lines 100-GT-F3-C; through PLV-1920
- **GCB-1700** (Grit chamber (vortex) with mixer MX-1701) → **GTP-1910** (Grit pump): lines 100-GT-F3-C; through PLV-1910
- **GCB-1700** (Grit chamber (vortex) with mixer MX-1701) → **TK-2300** (WET WELL #2): lines 400-PPE-E1, 300-PPE-E1; through KGV-1703, reducer, KGV-2301; crosses sheets
- **GCB-1700** (Grit chamber (vortex) with mixer MX-1701) → **TK-2200** (WET WELL #1): lines 400-PPE-E1, 300-PPE-E1; through KGV-1703, KGV-2201; crosses sheets
- **BIN-1102** (Sludge bin) → **SLD TRUCK OUT**
- **RWP-2330** (RAW SEWAGE PUMP #3) → **SB-2500** (SBR INFLUENT SPLITTER BOX): lines 200-PPE-E1, 250-PPE-H1; through reducer, Diaphragm seal, CHV-2330, KGV-2332, FE-2352, reducer, Injection quill; crosses sheets
- **RWP-2320** (RAW SEWAGE PUMP #2) → **SB-2500** (SBR INFLUENT SPLITTER BOX): lines 200-PPE-E1, 250-PPE-H1; through reducer, Diaphragm seal, CHV-2320, KGV-2322, FE-2352, reducer, Injection quill; crosses sheets
- **RWP-2310** (RAW SEWAGE PUMP #1) → **SB-2500** (SBR INFLUENT SPLITTER BOX): lines 200-PPE-E1, 250-PPE-H1; through reducer, Diaphragm seal, CHV-2310, KGV-2312, FE-2352, reducer, Injection quill; crosses sheets
- **PSF-3300** (PARSHALL FLUME) → **TK-3800** (Plant service water wet well): lines 150-PSW-H1
- **PSF-3300** (PARSHALL FLUME) → **SMP-3310** (EFFLUENT COMPOSITE SAMPLER): lines 25-SAM-E1; through BAV-3311, reducer, SNV-3312
- **PSF-3300** (PARSHALL FLUME) → **PE TO OUTFALL**: lines 400-PE-H1
- **GTP-1920** (Grit pump) → **GCL-2000** (Grit classifier (cyclone + screw)): lines 100-ARL-F3-C; through Diaphragm seal, BCV-1920, PLV-1922
- **GTP-1910** (Grit pump) → **GCL-2000** (Grit classifier (cyclone + screw)): lines 100-ARL-F3-C; through Diaphragm seal, BCV-1910, PLV-1912
- **SB-2500** (SBR INFLUENT SPLITTER BOX) → **SBR-2600** (SBR #1 (sequencing batch reactor)): lines 400-OV-H1
- **SB-2500** (SBR INFLUENT SPLITTER BOX) → **SBR-2700** (SBR #2 (sequencing batch reactor)): lines 400-PPE-H1; through PLV-2701
- **TK-3800** (Plant service water wet well) → **SP-4830** (BOOSTER PUMP (supplied by dewatering equipment supplier)): lines 80-PSW-H1; through BUV-4831, reducer, BAV-4831; crosses sheets
- **GCL-2000** (Grit classifier (cyclone + screw)) → **BIN-2000** (Grit bin)
- **GCL-2000** (Grit classifier (cyclone + screw)) → **TK-2200** (WET WELL #1): lines 50-DRN-E1, 150-SUP-E1, 150-DR-E1; through BAV-2001, reducer; crosses sheets
- **SBR-2600** (SBR #1 (sequencing batch reactor)) → **SLP-2610** (Sludge (WAS) pump)
- **SBR-2600** (SBR #1 (sequencing batch reactor)) → **TK-3110** (EQUALIZATION TANK #1): lines 400-SE-H1
- **SBR-2700** (SBR #2 (sequencing batch reactor)) → **SLP-2710** (Sludge (WAS) pump)
- **SBR-2700** (SBR #2 (sequencing batch reactor)) → **TK-3120** (EQUALIZATION TANK #2): lines 400-SE-H1
- **SP-4830** (BOOSTER PUMP (supplied by dewatering equipment supplier)) → **SCP-4800** (SCREW PRESS (screw press system)): lines 80-PSW-H1, 25-PSW-H1; through reducer, CHV-4831, BUV-4832, BAV-4835, SNV-4831
- **SP-4830** (BOOSTER PUMP (supplied by dewatering equipment supplier)) → **Screw press wash water header**: lines 80-PSW-H1; through reducer, CHV-4831, BUV-4832
- **BIN-2000** (Grit bin) → **SLD TRUCK OUT**
- **SLP-2610** (Sludge (WAS) pump) → **SSD-4200** (DIGESTER #2 (aerobic sludge digester)): lines 100-WAS-H1; through reducer, CHV-2611, PLV-2612, BAV-2802, reducer, FE-2801, reducer, KGV-4201; crosses sheets
- **SLP-2610** (Sludge (WAS) pump) → **SSD-4100** (DIGESTER #1 (aerobic sludge digester)): lines 100-WAS-H1; through reducer, CHV-2611, PLV-2612, BAV-2802, reducer, FE-2801, reducer, KGV-4101; crosses sheets
- **TK-3110** (EQUALIZATION TANK #1) → **TK-3120** (EQUALIZATION TANK #2)
- **TK-3110** (EQUALIZATION TANK #1) → **UV-3200** (UV CHANNEL (UV package)): lines 400-SE-H1, 300-SE-H1; through BUV-3110, reducer, FE-3201, BUV-3201; crosses sheets
- **SLP-2710** (Sludge (WAS) pump) → **SSD-4200** (DIGESTER #2 (aerobic sludge digester)): lines 100-WAS-H1; through reducer, CHV-2711, PLV-2712, BAV-2802, reducer, FE-2801, reducer, KGV-4201; crosses sheets
- **SLP-2710** (Sludge (WAS) pump) → **SSD-4100** (DIGESTER #1 (aerobic sludge digester)): lines 100-WAS-H1; through reducer, CHV-2711, PLV-2712, BAV-2802, reducer, FE-2801, reducer, KGV-4101; crosses sheets
- **TK-3120** (EQUALIZATION TANK #2) → **PSF-3300** (PARSHALL FLUME): lines 400-OV-E1; crosses sheets
- **TK-3120** (EQUALIZATION TANK #2) → **UV-3200** (UV CHANNEL (UV package)): lines 400-SE-H1, 300-SE-H1; through BUV-3120, reducer, FE-3201, BUV-3201; crosses sheets
- **SCP-4800** (SCREW PRESS (screw press system)) → **TK-2300** (WET WELL #2): lines 200-DR-E1; through KGV-2303; crosses sheets
- **SCP-4800** (SCREW PRESS (screw press system)) → **TK-2200** (WET WELL #1): lines 200-DR-E1; through KGV-2203; crosses sheets
- **SCP-4800** (SCREW PRESS (screw press system)) → **SCC-4900** (SCREW CONVEYOR (cake))
- **SSD-4200** (DIGESTER #2 (aerobic sludge digester)) → **DT-4300** (DAY TANK): lines 150-DS-H1; through PLV-4202
- **SSD-4100** (DIGESTER #1 (aerobic sludge digester)) → **DT-4300** (DAY TANK): lines 150-DS-H1; through PLV-4101, PLV-4102
- **SSD-4100** (DIGESTER #1 (aerobic sludge digester)) → **SSD-4200** (DIGESTER #2 (aerobic sludge digester))
- **UV-3200** (UV CHANNEL (UV package)) → **PSF-3300** (PARSHALL FLUME)
- **SCC-4900** (SCREW CONVEYOR (cake)) → **BIN-4910** (ROLL OFF BIN (supplied by the owner))
- **DT-4300** (DAY TANK) → **SLP-4720** (Sludge feed pump (VFD)): lines 150-DS-E1; through PLV-4711, PLV-4721, Diaphragm seal, reducer; crosses sheets
- **DT-4300** (DAY TANK) → **SLP-4710** (Sludge feed pump (VFD)): lines 150-DS-E1; through PLV-4711, Diaphragm seal, reducer; crosses sheets
- **SLP-4720** (Sludge feed pump (VFD)) → **MX-4810** (Sludge / polymer flocculation mixer): lines 100-DS-E1; through Diaphragm seal, CHV-4721, PLV-4722, BAV-4731, reducer, FE-4731, reducer, Polymer injection ring, reducer
- **SLP-4710** (Sludge feed pump (VFD)) → **MX-4810** (Sludge / polymer flocculation mixer): lines 100-DS-E1; through Diaphragm seal, CHV-4711, PLV-4712, BAV-4731, reducer, FE-4731, reducer, Polymer injection ring, reducer
- **MX-4810** (Sludge / polymer flocculation mixer) → **SCP-4800** (SCREW PRESS (screw press system)): lines 150-DS-E1; through Diaphragm seal
- **PSW PLANT SERVICE WATER** → **GCB-1700** (Grit chamber (vortex) with mixer MX-1701): lines 40-PSW-E1; through BAV-1701, STR-1701, SNV-1701, BAV-1702
- **PSW PLANT SERVICE WATER** → **RT-1610** (Rock trap (septage receiving station package)): lines 50-PSW-E1; through BAV-1615
- **PSW PLANT SERVICE WATER** → **SCR-1001** (Spiral screen No. 1): lines 50-PSW-E1, 25-PSW-H1; through BAV-1204, BAV-1001, SNV-1001
- **PSW PLANT SERVICE WATER** → **SCR-1201** (SPIRAL SCREEN (No. 2)): lines 50-PSW-E1; through BAV-1204, BAV-1201, SNV-1201
- **PSW PLANT SERVICE WATER** → **TO HOSE BIB**: lines 50-PSW-E1, 25-PSW-E1
- **PSW PLANT SERVICE WATER** → **FIL-1101** (EXISTING SALSNES FILTER PACKAGE): lines 50-PSW-E1; through BAV-1101, STR-1101, TW-1101, NEV-1101
- **RT-1610** (Rock trap (septage receiving station package)) → **GRD-1620** (Grinder (septage receiving station package)): lines 100-SEPS-H1
- **SCR-1001** (Spiral screen No. 1) → **BIN-1001** (Screenings bin)
- **SCR-1001** (Spiral screen No. 1) → **FIL-1101** (EXISTING SALSNES FILTER PACKAGE): lines 350-RWW-H1, 400-RWW-H1; through KGV-1011, reducer, KGV-1002
- **SCR-1001** (Spiral screen No. 1) → **TK-2300** (WET WELL #2): lines 350-RWW-H1, 400-RWW-H1, 400-PPE-E1, 300-PPE-E1; through KGV-1011, reducer, KGV-1003, KGV-1702, reducer, KGV-2301; crosses sheets
- **SCR-1001** (Spiral screen No. 1) → **TK-2200** (WET WELL #1): lines 350-RWW-H1, 400-RWW-H1, 400-PPE-E1, 300-PPE-E1; through KGV-1011, reducer, KGV-1003, KGV-1702, KGV-2201; crosses sheets
- **SCR-1001** (Spiral screen No. 1) → **GCB-1700** (Grit chamber (vortex) with mixer MX-1701): lines 350-RWW-H1, 400-RWW-H1; through KGV-1011, reducer, KGV-1003, KGV-1701; crosses sheets
- **SCR-1201** (SPIRAL SCREEN (No. 2)) → **BIN-1201** (Screenings bin)
- **SCR-1201** (SPIRAL SCREEN (No. 2)) → **FIL-1101** (EXISTING SALSNES FILTER PACKAGE): lines 400-RWW-H1; through KGV-1211, reducer, KGV-1002
- **SCR-1201** (SPIRAL SCREEN (No. 2)) → **TK-2300** (WET WELL #2): lines 400-RWW-H1, 400-PPE-E1, 300-PPE-E1; through KGV-1211, reducer, KGV-1003, KGV-1702, reducer, KGV-2301; crosses sheets
- **SCR-1201** (SPIRAL SCREEN (No. 2)) → **TK-2200** (WET WELL #1): lines 400-RWW-H1, 400-PPE-E1, 300-PPE-E1; through KGV-1211, reducer, KGV-1003, KGV-1702, KGV-2201; crosses sheets
- **SCR-1201** (SPIRAL SCREEN (No. 2)) → **GCB-1700** (Grit chamber (vortex) with mixer MX-1701): lines 400-RWW-H1; through KGV-1211, reducer, KGV-1003, KGV-1701; crosses sheets
- **GRD-1620** (Grinder (septage receiving station package)) → **FOR SAMPLER (FUTURE)**: lines 100-SEPS-H1, 50-SAM-H1; through FE-1601
- **GRD-1620** (Grinder (septage receiving station package)) → **TK-1630** (SEPTAGE TANK): lines 100-SEPS-H1; through FE-1601, BAV-1605
- **TK-1630** (SEPTAGE TANK) → **SEP-1650** (Septage pump): lines 100-SEPS-E1; through PLV-1651, Diaphragm seal
- **TK-1630** (SEPTAGE TANK) → **SEP-1640** (Septage pump): lines 100-SEPS-E1; through PLV-1641, Diaphragm seal
- **SEP-1650** (Septage pump) → **GCB-1700** (Grit chamber (vortex) with mixer MX-1701): lines 100-SEPS-E1; through Diaphragm seal, CHV-1651, PLV-1652, reducer, FE-1641, reducer; crosses sheets
- **SEP-1640** (Septage pump) → **GCB-1700** (Grit chamber (vortex) with mixer MX-1701): lines 100-SEPS-E1; through Diaphragm seal, CHV-1641, PLV-1642, reducer, FE-1641, reducer; crosses sheets
- **RSW FROM LIFT STATION #1** → **SB-1200** (SCREEN SPLITTER BOX): lines 200-RWW-E1; through FE-1001, KGV-1001
- **SB-1200** (SCREEN SPLITTER BOX) → **SMP-1001** (INFLUENT COMPOSITE SAMPLER (OUTSIDE)): through BAV-1005, reducer, BAV-1006, SNV-1005
- **SB-1200** (SCREEN SPLITTER BOX) → **SCR-1001** (Spiral screen No. 1): lines 250-RWW-H1; through KGV-1007
- **SB-1200** (SCREEN SPLITTER BOX) → **SCR-1201** (SPIRAL SCREEN (No. 2)): lines 250-RWW-H1; through KGV-1207
- **RSW FROM LIFT STATION #2** → **SB-1200** (SCREEN SPLITTER BOX): lines 200-RWW-H1; through FE-1201, KGV-1201
- **RWW SUMP PUMP** → **SB-1200** (SCREEN SPLITTER BOX): lines 30-RWW-E1
- **PSW PLANT SERVICE WATER (see D-002)** → **SBR-2700** (SBR #2 (sequencing batch reactor)): lines 25-PSW-H1; through BAV-2521, PRV-2521, BAV-2721, SNV-2722, Foam control nozzles (SBR #2)
- **PSW PLANT SERVICE WATER (see D-002)** → **SBR-2600** (SBR #1 (sequencing batch reactor)): lines 25-PSW-H1; through BAV-2521, PRV-2521, BAV-2621, SNV-2622, Foam control nozzles (SBR #1)
- **PSW PLANT SERVICE WATER (see D-002)** → **SB-2500** (SBR INFLUENT SPLITTER BOX): lines 25-PSW-H1; through BAV-2521, PRV-2521
- **ALTERNATIVE PROCESS SERVICE WATER FROM POTABLE WATER SYSTEM** → **PSW TO PSW NETWORK**: lines 100-PW-E1, 100-PSW-E1; through BUV-3851, reducer, FE-3831, reducer, BUV-3833
- **ATMOSPHERIC AIR (blower intakes)** → **BLO-3910** (SBR blower package blower (VFD)): lines 150-AAS-H1; through filter, Inlet silencer
- **ATMOSPHERIC AIR (blower intakes)** → **BLO-3920** (SBR blower package blower (VFD)): lines 150-AAS-H1; through filter, Inlet silencer
- **ATMOSPHERIC AIR (blower intakes)** → **BLO-3930** (SBR blower package blower (VFD)): lines 150-AAS-H1; through filter, Inlet silencer
- **ATMOSPHERIC AIR (blower intakes)** → **BLO-4010** (Digester blower package blower (VFD)): lines 150-AAS-H1; through filter, Inlet silencer
- **ATMOSPHERIC AIR (blower intakes)** → **BLO-4020** (Digester blower package blower (VFD)): lines 150-AAS-H1; through filter, Inlet silencer
- **BLO-3910** (SBR blower package blower (VFD)) → **Relief to atmosphere**: lines 200-AAS-H1, 50-ARL-H1; through expansion joint, Discharge silencer, expansion joint, PRV-3911
- **BLO-3910** (SBR blower package blower (VFD)) → **AID-2701** (Aeration diffuser grid): lines 200-AAS-H1, 150-AAS-H1, 100-AAS-H1; through expansion joint, Discharge silencer, expansion joint, CHV-3911, BUV-3911, BUV-2701, BUV-2703; crosses sheets
- **BLO-3910** (SBR blower package blower (VFD)) → **AID-2702** (Aeration diffuser grid): lines 200-AAS-H1, 150-AAS-H1, 100-AAS-H1; through expansion joint, Discharge silencer, expansion joint, CHV-3911, BUV-3911, BUV-2701, reducer, BUV-2705; crosses sheets
- **BLO-3910** (SBR blower package blower (VFD)) → **AID-2601** (Aeration diffuser grid): lines 200-AAS-H1, 100-AAS-H1, 150-AAS-H1; through expansion joint, Discharge silencer, expansion joint, CHV-3911, BUV-3911, BUV-2601, BUV-2603; crosses sheets
- **BLO-3910** (SBR blower package blower (VFD)) → **AID-2602** (Aeration diffuser grid): lines 200-AAS-H1, 100-AAS-H1; through expansion joint, Discharge silencer, expansion joint, CHV-3911, BUV-3911, BUV-2601, reducer, BUV-2605; crosses sheets
- **BLO-3920** (SBR blower package blower (VFD)) → **Relief to atmosphere**: lines 150-AAS-H1, 50-ARL-H1; through expansion joint, Discharge silencer, expansion joint, PRV-3921
- **BLO-3920** (SBR blower package blower (VFD)) → **AID-2701** (Aeration diffuser grid): lines 150-AAS-H1, 200-AAS-H1, 100-AAS-H1; through expansion joint, Discharge silencer, expansion joint, CHV-3921, BUV-3921, BUV-2701, BUV-2703; crosses sheets
- **BLO-3920** (SBR blower package blower (VFD)) → **AID-2702** (Aeration diffuser grid): lines 150-AAS-H1, 200-AAS-H1, 100-AAS-H1; through expansion joint, Discharge silencer, expansion joint, CHV-3921, BUV-3921, BUV-2701, reducer, BUV-2705; crosses sheets
- **BLO-3920** (SBR blower package blower (VFD)) → **AID-2601** (Aeration diffuser grid): lines 150-AAS-H1, 200-AAS-H1, 100-AAS-H1; through expansion joint, Discharge silencer, expansion joint, CHV-3921, BUV-3921, BUV-2601, BUV-2603; crosses sheets
- **BLO-3920** (SBR blower package blower (VFD)) → **AID-2602** (Aeration diffuser grid): lines 150-AAS-H1, 200-AAS-H1, 100-AAS-H1; through expansion joint, Discharge silencer, expansion joint, CHV-3921, BUV-3921, BUV-2601, reducer, BUV-2605; crosses sheets
- **BLO-3930** (SBR blower package blower (VFD)) → **Relief to atmosphere**: lines 200-AAS-H1, 50-ARL-H1; through expansion joint, Discharge silencer, expansion joint, PRV-3931
- **BLO-3930** (SBR blower package blower (VFD)) → **AID-2701** (Aeration diffuser grid): lines 200-AAS-H1, 150-AAS-H1, 100-AAS-H1; through expansion joint, Discharge silencer, expansion joint, CHV-3931, BUV-3931, BUV-3951, BUV-2701, BUV-2703; crosses sheets
- **BLO-3930** (SBR blower package blower (VFD)) → **AID-2702** (Aeration diffuser grid): lines 200-AAS-H1, 150-AAS-H1, 100-AAS-H1; through expansion joint, Discharge silencer, expansion joint, CHV-3931, BUV-3931, BUV-3951, BUV-2701, reducer, BUV-2705; crosses sheets
- **BLO-3930** (SBR blower package blower (VFD)) → **AID-2601** (Aeration diffuser grid): lines 200-AAS-H1, 100-AAS-H1, 150-AAS-H1; through expansion joint, Discharge silencer, expansion joint, CHV-3931, BUV-3931, BUV-3951, BUV-2601, BUV-2603; crosses sheets
- **BLO-3930** (SBR blower package blower (VFD)) → **AID-2602** (Aeration diffuser grid): lines 200-AAS-H1, 100-AAS-H1; through expansion joint, Discharge silencer, expansion joint, CHV-3931, BUV-3931, BUV-3951, BUV-2601, reducer, BUV-2605; crosses sheets
- **BLO-3930** (SBR blower package blower (VFD)) → **AID-4101** (Aeration diffuser grid): lines 200-AAS-H1, 150-AAS-H1, 100-AAS-H1; through expansion joint, Discharge silencer, expansion joint, CHV-3931, BUV-3931, BUV-3952, reducer, BUV-4051, BUV-4101; crosses sheets
- **BLO-3930** (SBR blower package blower (VFD)) → **MX-4310** (Day tank mixer): lines 200-AAS-H1, 150-AAS-H1, 100-AAS-H1; through expansion joint, Discharge silencer, expansion joint, CHV-3931, BUV-3931, BUV-3952, reducer; crosses sheets
- **BLO-3930** (SBR blower package blower (VFD)) → **AID-4201** (Aeration diffuser grid): lines 200-AAS-H1, 150-AAS-H1, 100-AAS-H1; through expansion joint, Discharge silencer, expansion joint, CHV-3931, BUV-3931, BUV-3952, reducer, BUV-4201; crosses sheets
- **BLO-4010** (Digester blower package blower (VFD)) → **Relief to atmosphere**: lines 150-AAS-H1, 50-ARL-H1; through expansion joint, Discharge silencer, expansion joint, PRV-4011
- **BLO-4010** (Digester blower package blower (VFD)) → **AID-4101** (Aeration diffuser grid): lines 150-AAS-H1, 100-AAS-H1; through expansion joint, Discharge silencer, expansion joint, CHV-4011, BUV-4011, BUV-4051, BUV-4101; crosses sheets
- **BLO-4010** (Digester blower package blower (VFD)) → **MX-4310** (Day tank mixer): lines 150-AAS-H1, 100-AAS-H1; through expansion joint, Discharge silencer, expansion joint, CHV-4011, BUV-4011; crosses sheets
- **BLO-4010** (Digester blower package blower (VFD)) → **AID-4201** (Aeration diffuser grid): lines 150-AAS-H1, 100-AAS-H1; through expansion joint, Discharge silencer, expansion joint, CHV-4011, BUV-4011, BUV-4201; crosses sheets
- **BLO-4020** (Digester blower package blower (VFD)) → **Relief to atmosphere**: lines 150-AAS-H1, 50-ARL-H1; through expansion joint, Discharge silencer, expansion joint, PRV-4021
- **BLO-4020** (Digester blower package blower (VFD)) → **AID-4101** (Aeration diffuser grid): lines 150-AAS-H1, 100-AAS-H1; through expansion joint, Discharge silencer, expansion joint, CHV-4021, BUV-4021, BUV-4101; crosses sheets
- **PW POTABLE WATER** → **MX-5330** (Polymer make-down mixing chamber (polymer skid)): lines 25-PW-E1; through BAV-5341, SNV-5342, PRV-5342, FE-5342
- **MX-5330** (Polymer make-down mixing chamber (polymer skid)) → **MX-4810** (Sludge / polymer flocculation mixer): lines 40-PLY-E1, 100-DS-E1; through reducer, FE-4812, BAV-4811, Polymer injection ring, reducer
- **BLO-1101** (BLOWER (Salsnes air knife)) → **FIL-1101** (EXISTING SALSNES FILTER PACKAGE): through CHV-1101, strainer
- **SEPTAGE-TRUCK** (SEPTAGE TRUCK (septage loading area)) → **FOR SAMPLER (FUTURE)**: lines 100-SEPS-H1, 50-SAM-H1; through BAV-1602
- **SEPTAGE-TRUCK** (SEPTAGE TRUCK (septage loading area)) → **RT-1610** (Rock trap (septage receiving station package)): lines 100-SEPS-H1; through BAV-1602, PLV-1611
- **PSWP-3810** (Plant service water pump (VFD)) → **TK-3800** (Plant service water wet well): lines 100-PSW-E1; through CHV-3811, BUV-3811, BUV-3801
- **PSWP-3810** (Plant service water pump (VFD)) → **TK-3840** (PLANT SERVICE WATER PRESSURE TANK): lines 100-PSW-E1, 32-PSW-H1; through CHV-3811, BUV-3811, STR-3831, BAV-3841, BAV-3844, reducer
- **PSWP-3810** (Plant service water pump (VFD)) → **PSW TO PSW NETWORK**: lines 100-PSW-E1; through CHV-3811, BUV-3811, STR-3831, BUV-3831, reducer, FE-3831, reducer, BUV-3833
- **TK-3840** (PLANT SERVICE WATER PRESSURE TANK) → **TK-3800** (Plant service water wet well): through PRV-3841
- **PSWP-3820** (Plant service water pump (VFD)) → **TK-3800** (Plant service water wet well): lines 100-ARL-H1, 100-PSW-E1; through CHV-3821, BUV-3821, BUV-3801
- **PSWP-3820** (Plant service water pump (VFD)) → **TK-3840** (PLANT SERVICE WATER PRESSURE TANK): lines 100-ARL-H1, 100-PSW-E1, 32-PSW-H1; through CHV-3821, BUV-3821, STR-3831, BAV-3841, BAV-3844, reducer
- **PSWP-3820** (Plant service water pump (VFD)) → **PSW TO PSW NETWORK**: lines 100-ARL-H1, 100-PSW-E1; through CHV-3821, BUV-3821, STR-3831, BUV-3831, reducer, FE-3831, reducer, BUV-3833
- **DCT-4110** (Decanter (VFD driven)) → **TK-2300** (WET WELL #2): lines 200-SUP-E1, 150-SUP-E1; through reducer, FE-4410, reducer, KGV-2302; crosses sheets
- **DCT-4110** (Decanter (VFD driven)) → **TK-2200** (WET WELL #1): lines 200-SUP-E1, 150-SUP-E1; through reducer, FE-4410, reducer, KGV-2202; crosses sheets
- **DCT-4210** (Decanter (VFD driven)) → **TK-2300** (WET WELL #2): lines 200-SUP-H1, 200-SUP-E1, 150-SUP-E1; through reducer, FE-4410, reducer, KGV-2302; crosses sheets
- **DCT-4210** (Decanter (VFD driven)) → **TK-2200** (WET WELL #1): lines 200-SUP-H1, 200-SUP-E1, 150-SUP-E1; through reducer, FE-4410, reducer, KGV-2202; crosses sheets
- **COMP-4820** (Screw press air compressor) → **SCP-4800** (SCREW PRESS (screw press system)): through PRV-4841, STR-4841, SNV-4841
- **PYST-5301** (POLYMER TOTE) → **PLP-5320** (Polymer pump (polymer skid)): lines 25-PLY-E1; through reducer, BAV-5302, BAV-5304, BAV-5321
- **PYST-5301** (POLYMER TOTE) → **PLP-5310** (Polymer pump (polymer skid)): lines 25-PLY-E1; through reducer, BAV-5302, BAV-5311
- **PLP-5320** (Polymer pump (polymer skid)) → **MX-5330** (Polymer make-down mixing chamber (polymer skid)): through PRV-5321, BAV-5325, FS-5331
- **PLP-5310** (Polymer pump (polymer skid)) → **MX-5330** (Polymer make-down mixing chamber (polymer skid)): through PRV-5311, BAV-5315
- **ALUM-TRUCK** (ALUM TRUCK (chemical loading area)) → **SPILL CONTAINMENT SUMP (outside building)**: lines 50-AL-H1, 25-DR-H1; through DIV-5521, CHV-5522, BAV-5523
- **ALUM-TRUCK** (ALUM TRUCK (chemical loading area)) → **AT-5520** (ALUM TANK #2): lines 50-AL-H1; through DIV-5521, CHV-5522, BAV-5524
- **ALUM-TRUCK** (ALUM TRUCK (chemical loading area)) → **AT-5510** (ALUM TANK #1): lines 50-AL-H1; through DIV-5511, CHV-5512, BAV-5514
- **AT-5520** (ALUM TANK #2) → **ASP-5560** (Alum metering pump (peristaltic, alum skid package)): lines 25-AL-E4; through BAV-5526, SG-5520, BAV-5527, reducer, BAV-5529, BAV-5541, STR-5541, BAV-5561, reducer
- **AT-5520** (ALUM TANK #2) → **ASP-5550** (Alum metering pump (peristaltic, alum skid package)): lines 25-AL-E4; through BAV-5526, SG-5520, BAV-5527, reducer, BAV-5529, BAV-5541, STR-5541, BAV-5551, reducer
- **AT-5520** (ALUM TANK #2) → **ALUM SYSTEM SECONDARY CONTAINMENT AREA / TO SPILL CONTAINMENT**: lines 25-AL-E4; through BAV-5526, SG-5520, BAV-5527, reducer, BAV-5529
- **AT-5510** (ALUM TANK #1) → **ASP-5560** (Alum metering pump (peristaltic, alum skid package)): lines 25-AL-E4; through BAV-5516, SG-5510, BAV-5517, reducer, BAV-5519, BAV-5541, STR-5541, BAV-5561, reducer
- **AT-5510** (ALUM TANK #1) → **ASP-5550** (Alum metering pump (peristaltic, alum skid package)): lines 25-AL-E4; through BAV-5516, SG-5510, BAV-5517, reducer, BAV-5519, BAV-5541, STR-5541, BAV-5551, reducer
- **AT-5510** (ALUM TANK #1) → **ALUM SYSTEM SECONDARY CONTAINMENT AREA / TO SPILL CONTAINMENT**: lines 25-AL-E4; through BAV-5516, SG-5510, BAV-5517, reducer, BAV-5519
- **ASP-5560** (Alum metering pump (peristaltic, alum skid package)) → **SB-2500** (SBR INFLUENT SPLITTER BOX): lines 25-AL-E4, 25-AL-E1, 200-PPE-E1, 250-PPE-H1; through CHV-5561, PRV-5561, BAV-5563, BAV-5583, BPV-5581, BAV-5581, BAV-5584, BAV-5585, BPV-5586, Injection quill; crosses sheets
- **ASP-5550** (Alum metering pump (peristaltic, alum skid package)) → **SB-2500** (SBR INFLUENT SPLITTER BOX): lines 25-AL-E4, 25-AL-E1, 200-PPE-E1, 250-PPE-H1; through CHV-5551, BAV-5552, BAV-5562, PRV-5561, BAV-5563, BAV-5583, BPV-5581, BAV-5581, BAV-5584, BAV-5585, BPV-5586, Injection quill; crosses sheets
- **ASP-5550** (Alum metering pump (peristaltic, alum skid package)) → **AT-5520** (ALUM TANK #2): lines 25-AL-E4, 25-PRL-E4; through CHV-5551, PRV-5551, BAV-5515, BAV-5525, reducer
- **ASP-5550** (Alum metering pump (peristaltic, alum skid package)) → **AT-5510** (ALUM TANK #1): lines 25-AL-E4, 25-PRL-E4; through CHV-5551, PRV-5551, BAV-5515, reducer

Drains, vents and overflows (not process flow):
- Air release (vent) ← GTP-1910, GTP-1920
- Air valve vent ← PSWP-3810, PSWP-3820
- Atmosphere (relief / vent) ← BLO-1101
- DRAIN ← ASP-5550, ASP-5560, DT-4300, GCB-1700, MX-4810, MX-5330, PSW PLANT SERVICE WATER, PYST-5301, RSW FROM LIFT STATION #1, RSW FROM LIFT STATION #2, RWP-2310, RWP-2320, RWP-2330, SB-1200, SCC-4900, SCP-4800, SEP-1640, SEP-1650, SLP-4710, SLP-4720, SP-4830, TK-1630, TK-2200, TK-2300
- SAMPLE DRAIN ← SLP-2610, SLP-2710
- VENT ← DT-4300, SSD-4200
- VENT (outside building) ← AT-5510, AT-5520
- VENT / ATMOSPHERE ← AID-2601, AID-2602, AID-2701, AID-2702, SBR-2700, SLP-2610, SLP-2710, TK-3120
- VENT / RELIEF ← COMP-4820, MX-5330, SLP-4710, SLP-4720
- VENT TO ROOF ← PSW PLANT SERVICE WATER, RWP-2310, RWP-2320, RWP-2330, SEP-1640, SEP-1650, TK-2200

## Equipment

| Tag | Kind | Description | Fed by | Feeds | Status | Sheets |
|---|---|---|---|---|---|---|
| AID-2601 | other | Aeration diffuser grid | BLO-3910, BLO-3920, BLO-3930 | VENT / ATMOSPHERE |  | D-011-0 |
| AID-2602 | other | Aeration diffuser grid | BLO-3910, BLO-3920, BLO-3930 | VENT / ATMOSPHERE |  | D-011-0 |
| AID-2701 | other | Aeration diffuser grid | BLO-3910, BLO-3920, BLO-3930 | VENT / ATMOSPHERE |  | D-011-0 |
| AID-2702 | other | Aeration diffuser grid | BLO-3910, BLO-3920, BLO-3930 | VENT / ATMOSPHERE |  | D-011-0 |
| AID-4101 | other | Aeration diffuser grid | BLO-3930, BLO-4010, BLO-4020 |  |  | D-014-0 |
| AID-4201 | other | Aeration diffuser grid | BLO-3930, BLO-4010 |  |  | D-014-0 |
| ALUM-TRUCK | other | ALUM TRUCK (chemical loading area) |  | AT-5510, AT-5520, SPILL CONTAINMENT SUMP (outside building) |  | D-016-0 |
| ASP-5550 | metering_pump | Alum metering pump (peristaltic, alum skid package) | AT-5510, AT-5520 | AT-5510, AT-5520, DRAIN, SB-2500 |  | D-016-0 |
| ASP-5560 | metering_pump | Alum metering pump (peristaltic, alum skid package) | AT-5510, AT-5520 | DRAIN, SB-2500 |  | D-016-0 |
| AT-5510 | tank | ALUM TANK #1 | ALUM-TRUCK, ASP-5550 | ALUM SYSTEM SECONDARY CONTAINMENT AREA / TO SPILL CONTAINMENT, ASP-5550, ASP-5560, VENT (outside building) |  | D-016-0 |
| AT-5520 | tank | ALUM TANK #2 | ALUM-TRUCK, ASP-5550 | ALUM SYSTEM SECONDARY CONTAINMENT AREA / TO SPILL CONTAINMENT, ASP-5550, ASP-5560, VENT (outside building) |  | D-016-0 |
| BIN-1001 | bin | Screenings bin | SCR-1001 |  | existing | D-007-0 |
| BIN-1102 | bin | Sludge bin | SCP-1101 | SLD TRUCK OUT | existing | D-007-0 |
| BIN-1201 | bin | Screenings bin | SCR-1201 |  |  | D-007-0 |
| BIN-2000 | bin | Grit bin | GCL-2000 | SLD TRUCK OUT |  | D-009-0 |
| BIN-4910 | bin | ROLL OFF BIN (supplied by the owner) | SCC-4900 |  |  | D-015-0 |
| BLO-1101 | blower | BLOWER (Salsnes air knife) |  | Atmosphere (relief / vent), FIL-1101 | existing | D-007-0 |
| BLO-3910 | blower | SBR blower package blower (VFD) | ATMOSPHERIC AIR (blower intakes) | AID-2601, AID-2602, AID-2701, AID-2702, Relief to atmosphere |  | D-013-0 |
| BLO-3920 | blower | SBR blower package blower (VFD) | ATMOSPHERIC AIR (blower intakes) | AID-2601, AID-2602, AID-2701, AID-2702, Relief to atmosphere |  | D-013-0 |
| BLO-3930 | blower | SBR blower package blower (VFD) | ATMOSPHERIC AIR (blower intakes) | AID-2601, AID-2602, AID-2701, AID-2702, AID-4101, AID-4201, MX-4310, Relief to atmosphere |  | D-013-0 |
| BLO-4010 | blower | Digester blower package blower (VFD) | ATMOSPHERIC AIR (blower intakes) | AID-4101, AID-4201, MX-4310, Relief to atmosphere |  | D-013-0 |
| BLO-4020 | blower | Digester blower package blower (VFD) | ATMOSPHERIC AIR (blower intakes) | AID-4101, Relief to atmosphere |  | D-013-0 |
| COMP-4820 | compressor | Screw press air compressor |  | SCP-4800, VENT / RELIEF |  | D-015-0 |
| DCT-2620 | other | Decanter (VFD driven) |  |  |  | D-011-0 |
| DCT-2720 | other | Decanter (VFD driven) |  |  |  | D-011-0 |
| DCT-4110 | other | Decanter (VFD driven) |  | TK-2200, TK-2300 |  | D-014-0 |
| DCT-4210 | other | Decanter (VFD driven) |  | TK-2200, TK-2300 |  | D-014-0 |
| DT-4300 | agitated_tank | DAY TANK | SSD-4100, SSD-4200 | DRAIN, SLP-4710, SLP-4720, VENT |  | D-014-0 |
| FIL-1101 | filter | EXISTING SALSNES FILTER PACKAGE | BLO-1101, HW HOT WATER SYSTEM, PSW PLANT SERVICE WATER, SCR-1001, SCR-1201 | DRN TO SUMP PUMP, GCB-1700, SCP-1101, TK-2200, TK-2300 | existing | D-007-0 |
| FN-1101 | fan | BLOWER COOLING FAN |  |  | existing | D-007-0 |
| GCB-1700 | separator | Grit chamber (vortex) with mixer MX-1701 | FIL-1101, PSW PLANT SERVICE WATER, SCR-1001, SCR-1201, SEP-1640, SEP-1650 | DRAIN, GTP-1910, GTP-1920, TK-2200, TK-2300 |  | D-009-0 |
| GCL-2000 | screen | Grit classifier (cyclone + screw) | GTP-1910, GTP-1920 | BIN-2000, TK-2200 |  | D-009-0 |
| GRD-1620 | mill | Grinder (septage receiving station package) | RT-1610 | FOR SAMPLER (FUTURE), TK-1630 |  | D-008-0 |
| GTP-1910 | slurry_pump | Grit pump | GCB-1700 | Air release (vent), GCL-2000 |  | D-009-0 |
| GTP-1920 | slurry_pump | Grit pump | GCB-1700 | Air release (vent), GCL-2000 |  | D-009-0 |
| M-4802 | motor | Screw press spray arm motor |  |  |  | D-015-0 |
| MX-1701 | agitator | Grit chamber mixer |  |  |  | D-009-0 |
| MX-2630 | mixer | SBR mixer |  |  |  | D-011-0 |
| MX-2730 | mixer | SBR mixer |  |  |  | D-011-0 |
| MX-4120 | agitator | Digester #1 mixer |  |  |  | D-014-0 |
| MX-4130 | agitator | Digester #1 mixer |  |  |  | D-014-0 |
| MX-4220 | agitator | Digester #2 mixer |  |  |  | D-014-0 |
| MX-4310 | agitator | Day tank mixer | BLO-3930, BLO-4010 |  |  | D-014-0 |
| MX-4810 | static_mixer | Sludge / polymer flocculation mixer | MX-5330, SLP-4710, SLP-4720 | DRAIN, SCP-4800 |  | D-015-0 |
| MX-5330 | mixer | Polymer make-down mixing chamber (polymer skid) | PLP-5310, PLP-5320, PW POTABLE WATER | DRAIN, MX-4810, VENT / RELIEF |  | D-015-0 |
| PLP-5310 | positive_displacement_pump | Polymer pump (polymer skid) | PYST-5301 | MX-5330 |  | D-015-0 |
| PLP-5320 | positive_displacement_pump | Polymer pump (polymer skid) | PYST-5301 | MX-5330 |  | D-015-0 |
| PSF-3300 | other | PARSHALL FLUME | TK-2300, TK-3120, UV-3200 | PE TO OUTFALL, SMP-3310, TK-3800 |  | D-012-0 |
| PSWP-3810 | sump_pump | Plant service water pump (VFD) |  | Air valve vent, PSW TO PSW NETWORK, TK-3800, TK-3840 |  | D-012-0 |
| PSWP-3820 | sump_pump | Plant service water pump (VFD) |  | Air valve vent, PSW TO PSW NETWORK, TK-3800, TK-3840 |  | D-012-0 |
| PYST-5301 | tank | POLYMER TOTE |  | DRAIN, PLP-5310, PLP-5320 |  | D-015-0 |
| RT-1610 | screen | Rock trap (septage receiving station package) | PSW PLANT SERVICE WATER, SEPTAGE-TRUCK | GRD-1620 |  | D-008-0 |
| RWP-2310 | centrifugal_pump | RAW SEWAGE PUMP #1 | TK-2200, TK-2300 | DRAIN, SB-2500, VENT TO ROOF |  | D-010-0 |
| RWP-2320 | centrifugal_pump | RAW SEWAGE PUMP #2 | TK-2200, TK-2300 | DRAIN, SB-2500, VENT TO ROOF |  | D-010-0 |
| RWP-2330 | centrifugal_pump | RAW SEWAGE PUMP #3 | TK-2200, TK-2300 | DRAIN, SB-2500, VENT TO ROOF |  | D-010-0 |
| SB-1200 | box | SCREEN SPLITTER BOX | RSW FROM LIFT STATION #1, RSW FROM LIFT STATION #2, RWW SUMP PUMP | DRAIN, SCR-1001, SCR-1201, SMP-1001 |  | D-007-0 |
| SB-2500 | box | SBR INFLUENT SPLITTER BOX | ASP-5550, ASP-5560, PSW PLANT SERVICE WATER (see D-002), RWP-2310, RWP-2320, RWP-2330 | SBR-2600, SBR-2700 |  | D-011-0 |
| SBR-2600 | reactor | SBR #1 (sequencing batch reactor) | PSW PLANT SERVICE WATER (see D-002), SB-2500 | SLP-2610, TK-3110 |  | D-011-0 |
| SBR-2700 | reactor | SBR #2 (sequencing batch reactor) | PSW PLANT SERVICE WATER (see D-002), SB-2500 | SLP-2710, TK-3120, VENT / ATMOSPHERE |  | D-011-0 |
| SCC-4900 | conveyor | SCREW CONVEYOR (cake) | SCP-4800 | BIN-4910, DRAIN |  | D-015-0 |
| SCP-1101 | conveyor | SLUDGE SCREW | FIL-1101 | BIN-1102, DRN TO SUMP PUMP | existing | D-007-0 |
| SCP-4800 | filter_press | SCREW PRESS (screw press system) | COMP-4820, MX-4810, SP-4830 | DRAIN, SCC-4900, TK-2200, TK-2300 |  | D-015-0 |
| SCR-1001 | screen | Spiral screen No. 1 | PSW PLANT SERVICE WATER, SB-1200 | BIN-1001, FIL-1101, GCB-1700, TK-2200, TK-2300 | existing | D-007-0 |
| SCR-1201 | screen | SPIRAL SCREEN (No. 2) | PSW PLANT SERVICE WATER, SB-1200 | BIN-1201, FIL-1101, GCB-1700, TK-2200, TK-2300 |  | D-007-0 |
| SEP-1640 | positive_displacement_pump | Septage pump | TK-1630 | DRAIN, GCB-1700, VENT TO ROOF |  | D-008-0 |
| SEP-1650 | positive_displacement_pump | Septage pump | TK-1630 | DRAIN, GCB-1700, VENT TO ROOF |  | D-008-0 |
| SEPTAGE-TRUCK | other | SEPTAGE TRUCK (septage loading area) |  | FOR SAMPLER (FUTURE), RT-1610 |  | D-008-0 |
| SLP-2610 | slurry_pump | Sludge (WAS) pump | SBR-2600 | SAMPLE DRAIN, SSD-4100, SSD-4200, VENT / ATMOSPHERE |  | D-011-0 |
| SLP-2710 | slurry_pump | Sludge (WAS) pump | SBR-2700 | SAMPLE DRAIN, SSD-4100, SSD-4200, VENT / ATMOSPHERE |  | D-011-0 |
| SLP-4710 | positive_displacement_pump | Sludge feed pump (VFD) | DT-4300 | DRAIN, MX-4810, VENT / RELIEF |  | D-015-0 |
| SLP-4720 | positive_displacement_pump | Sludge feed pump (VFD) | DT-4300 | DRAIN, MX-4810, VENT / RELIEF |  | D-015-0 |
| SMP-1001 | sampler | INFLUENT COMPOSITE SAMPLER (OUTSIDE) | SB-1200 |  | existing | D-007-0 |
| SMP-3310 | sampler | EFFLUENT COMPOSITE SAMPLER | PSF-3300 |  |  | D-012-0 |
| SP-4830 | centrifugal_pump | BOOSTER PUMP (supplied by dewatering equipment supplier) | TK-3800 | DRAIN, SCP-4800, Screw press wash water header |  | D-015-0 |
| SSD-4100 | agitated_tank | DIGESTER #1 (aerobic sludge digester) | SLP-2610, SLP-2710 | DT-4300, SSD-4200 |  | D-014-0 |
| SSD-4200 | agitated_tank | DIGESTER #2 (aerobic sludge digester) | SLP-2610, SLP-2710, SSD-4100 | DT-4300, VENT |  | D-014-0 |
| TK-1630 | tank | SEPTAGE TANK | GRD-1620 | DRAIN, SEP-1640, SEP-1650 |  | D-008-0 |
| TK-2200 | sump | WET WELL #1 | DCT-4110, DCT-4210, FIL-1101, GCB-1700, GCL-2000, SCP-4800, SCR-1001, SCR-1201 | DRAIN, RWP-2310, RWP-2320, RWP-2330, TK-2300, VENT TO ROOF |  | D-010-0 |
| TK-2300 | sump | WET WELL #2 | DCT-4110, DCT-4210, FIL-1101, GCB-1700, SCP-4800, SCR-1001, SCR-1201, TK-2200 | DRAIN, PSF-3300, RWP-2310, RWP-2320, RWP-2330 |  | D-010-0 |
| TK-3110 | tank | EQUALIZATION TANK #1 | SBR-2600 | TK-3120, UV-3200 |  | D-011-0 |
| TK-3120 | tank | EQUALIZATION TANK #2 | SBR-2700, TK-3110 | PSF-3300, UV-3200, VENT / ATMOSPHERE |  | D-011-0 |
| TK-3800 | sump | Plant service water wet well | PSF-3300, PSWP-3810, PSWP-3820, TK-3840 | SP-4830 |  | D-012-0 |
| TK-3840 | pressure_vessel | PLANT SERVICE WATER PRESSURE TANK | PSWP-3810, PSWP-3820 | TK-3800 |  | D-012-0 |
| UV-3200 | uv_unit | UV CHANNEL (UV package) | TK-3110, TK-3120 | PSF-3300 |  | D-012-0 |
| UV-3201 | uv_unit | UV bank 1 |  |  |  | D-012-0 |
| UV-3202 | uv_unit | UV bank 2 |  |  |  | D-012-0 |
| UV-3203 | uv_unit | UV bank 3 |  |  |  | D-012-0 |

## Instruments

Location is where the instrument senses the process. Pipe locations read `line (upstream item -> downstream item)`.

| Tag | Variable | Function | Mounted | Senses | Loop |
|---|---|---|---|---|---|
| AE-1221 | analysis | element | field | HEADWORKS ROOM (atmosphere) | A-1221 |
| AE-1222 | analysis | element | field | HEADWORKS ROOM (atmosphere) | A-1222 |
| AE-1621 | analysis | element | field | SEPTAGE RECEIVING ROOM (atmosphere) | A-1621 |
| AE-1622 | analysis | element | field | SEPTAGE RECEIVING ROOM (atmosphere) | A-1622 |
| AE-1721 | analysis | element | field | GRIT ROOM (atmosphere) | A-1721 |
| AE-1722 | analysis | element | field | GRIT ROOM (atmosphere) | A-1722 |
| AE-2601 | analysis | element | field | SBR-2600 | A-2601 |
| AE-2602 | analysis | element | field | SBR-2600 |  |
| AE-2701 | analysis | element | field | SBR-2700 | A-2701 |
| AE-2702 | analysis | element | field | SBR-2700 |  |
| AE-2801 | analysis | element | field | 100-WAS-H1 (BAV-2802 -> reducer) | A-2801 |
| AE-3201 | analysis | element | field | UV-3200 | A-3201 |
| AE-3202 | analysis | element | field | UV-3200 | A-3202 |
| AE-4101 | analysis | element | field | SSD-4100 | A-4101 |
| AE-4102 | analysis | element | field | SSD-4100 | A-4102 |
| AE-4201 | analysis | element | field | SSD-4200 | A-4201 |
| AE-4202 | analysis | element | field | SSD-4200 | A-4202 |
| AI-1221 | analysis | indicator | plc |  | A-1221 |
| AI-1222 | analysis | indicator | plc |  | A-1222 |
| AI-1621 | analysis | indicator | plc |  | A-1621 |
| AI-1622 | analysis | indicator | plc |  | A-1622 |
| AI-1721 | analysis | indicator | plc |  | A-1721 |
| AI-1722 | analysis | indicator | plc |  | A-1722 |
| AI-3201 | analysis | indicator | plc |  | A-3201 |
| AI-3202 | analysis | indicator | plc |  | A-3202 |
| AIT-1221 | analysis | transmitter | field | HEADWORKS ROOM (atmosphere) | A-1221 |
| AIT-1222 | analysis | transmitter | field | HEADWORKS ROOM (atmosphere) | A-1222 |
| AIT-1621 | analysis | transmitter | field | SEPTAGE RECEIVING ROOM (atmosphere) | A-1621 |
| AIT-1622 | analysis | transmitter | field | SEPTAGE RECEIVING ROOM (atmosphere) | A-1622 |
| AIT-1721 | analysis | transmitter | field | GRIT ROOM (atmosphere) | A-1721 |
| AIT-1722 | analysis | transmitter | field | GRIT ROOM (atmosphere) | A-1722 |
| AIT-2601 | analysis | transmitter | field | SBR-2600 | A-2601 |
| AIT-2701 | analysis | transmitter | field | SBR-2700 | A-2701 |
| AIT-2801 | analysis | transmitter | field | 100-WAS-H1 (BAV-2802 -> reducer) | A-2801 |
| AIT-3201 | analysis | transmitter | field | UV-3200 | A-3201 |
| AIT-3202 | analysis | transmitter | field | UV-3200 | A-3202 |
| AIT-4101 | analysis | transmitter | field | SSD-4100 | A-4101 |
| AIT-4102 | analysis | transmitter | field | SSD-4100 | A-4102 |
| AIT-4201 | analysis | transmitter | field | SSD-4200 | A-4201 |
| AIT-4202 | analysis | transmitter | field | SSD-4200 | A-4202 |
| DP-3831 | density | other | field | STR-3831 | D-3831 |
| DP-3911 | density | other | field | filter | D-3911 |
| DP-3921 | density | other | field | filter | D-3921 |
| DP-3931 | density | other | field | filter | D-3931 |
| DP-4011 | density | other | field | filter | D-4011 |
| DP-4021 | density | other | field | filter | D-4021 |
| DPI-3831 | density | indicator | plc |  | D-3831 |
| DPT-3831 | density | transmitter | field | STR-3831 | D-3831 |
| DPT-3911 | density | transmitter | field | filter | D-3911 |
| DPT-3921 | density | transmitter | field | filter | D-3921 |
| DPT-3931 | density | transmitter | field | filter | D-3931 |
| DPT-4011 | density | transmitter | field | filter | D-4011 |
| DPT-4021 | density | transmitter | field | filter | D-4021 |
| EL-1200A | voltage | other | local_panel |  | E-1200 |
| EL-1200B | voltage | other | local_panel |  | E-1200 |
| EL-1200C | voltage | other | local_panel |  | E-1200 |
| EL-1200D | voltage | other | local_panel |  | E-1200 |
| EL-1250 | voltage | other | local_panel |  |  |
| EL-1600 | voltage | other | local_panel |  |  |
| EL-1620A | voltage | other | local_panel |  | E-1620 |
| EL-1620B | voltage | other | local_panel |  | E-1620 |
| EL-1620C | voltage | other | local_panel |  | E-1620 |
| EL-1620D | voltage | other | local_panel |  | E-1620 |
| EL-1640 | voltage | other | local_panel |  |  |
| EL-1700 | voltage | other | local_panel |  | E-1700 |
| EL-1700A | voltage | other | local_panel |  | E-1700 |
| EL-1700B | voltage | other | local_panel |  | E-1700 |
| EL-1701 | voltage | other | local_panel |  | E-1701 |
| EL-1701A | voltage | other | local_panel |  | E-1701 |
| EL-1701B | voltage | other | local_panel |  | E-1701 |
| EL-1900A | voltage | other | local_panel |  | E-1900 |
| EL-1900B | voltage | other | local_panel |  | E-1900 |
| EL-1900C | voltage | other | local_panel |  | E-1900 |
| EL-2000A | voltage | other | local_panel |  | E-2000 |
| EL-2000B | voltage | other | local_panel |  | E-2000 |
| EL-2310 | voltage | other | local_panel |  |  |
| EL-3910 | voltage | other | local_panel |  |  |
| EL-3920 | voltage | other | local_panel |  |  |
| EL-3930 | voltage | other | local_panel |  |  |
| EL-5300 | voltage | other | local_panel |  |  |
| EL-5501A | voltage | other | local_panel |  | E-5501 |
| EL-5501B | voltage | other | local_panel |  | E-5501 |
| FC-5300 | flow | controller | plc |  | F-5300 |
| FE-1001 | flow | element | field | in-line on 200-RWW-E1 (RSW FROM LIFT STATION #1 -> KGV-1001) | F-1001 |
| FE-1201 | flow | element | field | in-line on 200-RWW-H1 (RSW FROM LIFT STATION #2 -> KGV-1201) | F-1201 |
| FE-1601 | flow | element | field | in-line on 100-SEPS-H1 (GRD-1620 -> BAV-1605) | F-1601 |
| FE-1641 | flow | element | field | in-line on 100-SEPS-E1 (reducer -> reducer) | F-1641 |
| FE-2352 | flow | element | field | in-line on 200-PPE-E1 (KGV-2332 -> reducer) | F-2352 |
| FE-2801 | flow | element | field | in-line on 100-WAS-H1 (reducer -> reducer) | F-2801 |
| FE-3201 | flow | element | field | in-line on 300-SE-H1 (reducer -> BUV-3201) | F-3201 |
| FE-3301 | flow | element | field | PSF-3300 | F-3301 |
| FE-3831 | flow | element | field | in-line on 100-PSW-E1 (reducer -> reducer) | F-3831 |
| FE-4410 | flow | element | field | in-line on 200-SUP-E1 (reducer -> reducer) | F-4410 |
| FE-4731 | flow | element | field | in-line on 100-DS-E1 (reducer -> reducer) | F-4731 |
| FE-4812 | flow | element | field | in-line on 40-PLY-E1 (reducer -> BAV-4811) | F-4812 |
| FE-5342 | flow | element | field | in-line on 25-PW-E1 (PRV-5342 -> MX-5330) | F-5342 |
| FI-1001 | flow | indicator | plc |  | F-1001 |
| FI-1201 | flow | indicator | plc |  | F-1201 |
| FI-1641 | flow | indicator | plc |  | F-1641 |
| FI-2352 | flow | indicator | plc |  | F-2352 |
| FI-3201 | flow | indicator | plc |  | F-3201 |
| FI-3301 | flow | indicator | plc |  | F-3301 |
| FI-3831 | flow | indicator | plc |  | F-3831 |
| FI-4410 | flow | indicator | plc |  | F-4410 |
| FIT-1001 | flow | transmitter | field | in-line on 200-RWW-E1 (RSW FROM LIFT STATION #1 -> KGV-1001) | F-1001 |
| FIT-1201 | flow | transmitter | field | in-line on 200-RWW-H1 (RSW FROM LIFT STATION #2 -> KGV-1201) | F-1201 |
| FIT-1601 | flow | transmitter | field | in-line on 100-SEPS-H1 (GRD-1620 -> BAV-1605) | F-1601 |
| FIT-1641 | flow | transmitter | field | in-line on 100-SEPS-E1 (reducer -> reducer) | F-1641 |
| FIT-2352 | flow | transmitter | field | in-line on 200-PPE-E1 (KGV-2332 -> reducer) | F-2352 |
| FIT-2801 | flow | transmitter | field | in-line on 100-WAS-H1 (reducer -> reducer) | F-2801 |
| FIT-3201 | flow | transmitter | field | in-line on 300-SE-H1 (reducer -> BUV-3201) | F-3201 |
| FIT-3301 | flow | transmitter | plc | PSF-3300 | F-3301 |
| FIT-3831 | flow | transmitter | field | in-line on 100-PSW-E1 (reducer -> reducer) | F-3831 |
| FIT-4410 | flow | transmitter | field | in-line on 200-SUP-E1 (reducer -> reducer) | F-4410 |
| FIT-4731 | flow | transmitter | field | in-line on 100-DS-E1 (reducer -> reducer) | F-4731 |
| FIT-4812 | flow | transmitter | field | in-line on 40-PLY-E1 (reducer -> BAV-4811) | F-4812 |
| FIT-5342 | flow | transmitter | field | in-line on 25-PW-E1 (PRV-5342 -> MX-5330) | F-5342 |
| FQI-1001 | integrate/totalize flow | indicator | plc |  | F-1001 |
| FQI-1201 | integrate/totalize flow | indicator | plc |  | F-1201 |
| FQI-1601 | integrate/totalize flow | indicator | plc |  | F-1601 |
| FQI-1641 | integrate/totalize flow | indicator | plc |  | F-1641 |
| FQI-2352 | integrate/totalize flow | indicator | plc |  | F-2352 |
| FQI-3201 | integrate/totalize flow | indicator | plc |  | F-3201 |
| FQI-3301 | integrate/totalize flow | indicator | plc |  | F-3301 |
| FQI-3831 | integrate/totalize flow | indicator | plc |  | F-3831 |
| FQI-4410 | integrate/totalize flow | indicator | plc |  | F-4410 |
| FS-5331 | flow | switch | field | in-line on line (BAV-5325 -> MX-5330) |  |
| FY-1200 | flow | relay | plc |  |  |
| HS-1200A | hand | hand_switch | local_panel |  | H-1200 |
| HS-1200B | hand | hand_switch | local_panel |  | H-1200 |
| HS-1200C | hand | hand_switch | local_panel |  | H-1200 |
| HS-1200D | hand | hand_switch | local_panel |  | H-1200 |
| HS-1201 | hand | hand_switch | local_panel |  | H-1201 |
| HS-1620 | hand | hand_switch | local_panel |  | H-1620 |
| HS-1640A | hand | hand_switch | local_panel |  | H-1640 |
| HS-1640B | hand | hand_switch | local_panel |  | H-1640 |
| HS-1700 | hand | hand_switch | local_panel |  |  |
| HS-1701 | hand | hand_switch | local_panel |  | H-1701 |
| HS-1701A | hand | hand_switch | local_panel |  | H-1701 |
| HS-1900 | hand | hand_switch | local_panel |  | H-1900 |
| HS-2000 | hand | hand_switch | local_panel |  | H-2000 |
| HS-2000A | hand | hand_switch | local_panel |  | H-2000 |
| HS-2000B | hand | hand_switch | local_panel |  | H-2000 |
| HS-2000B#2 | hand | hand_switch | local_panel |  | H-2000#2 |
| HS-2000B#3 | hand | hand_switch | local_panel |  | H-2000#3 |
| HS-2310A | hand | hand_switch | local_panel |  | H-2310 |
| HS-2310B | hand | hand_switch | local_panel |  | H-2310 |
| HS-3820A | hand | hand_switch | local_panel |  | H-3820 |
| HS-3820B | hand | hand_switch | local_panel |  | H-3820 |
| HS-3910 | hand | hand_switch | local_panel |  | H-3910 |
| HS-3920 | hand | hand_switch | local_panel |  | H-3920 |
| HS-3930 | hand | hand_switch | local_panel |  | H-3930 |
| HS-4710A | hand | hand_switch | local_panel |  | H-4710 |
| HS-4710B | hand | hand_switch | local_panel |  | H-4710 |
| HS-5300 | hand | hand_switch | local_panel |  | H-5300 |
| HS-5500A | hand | hand_switch | local_panel |  | H-5500 |
| HS-5500B | hand | hand_switch | local_panel |  | H-5500 |
| HS-5501 | hand | hand_switch | local_panel |  | H-5501 |
| HSI-1001 | hand | hand_switch | plc |  |  |
| HSI-1201 | hand | hand_switch | plc |  | H-1201 |
| HSI-1640 | hand | hand_switch | plc |  | H-1640 |
| HSI-1701 | hand | hand_switch | plc |  | H-1701 |
| HSI-2000 | hand | hand_switch | plc |  | H-2000 |
| HSI-2310 | hand | hand_switch | plc |  | H-2310 |
| HSI-3820 | hand | hand_switch | plc |  | H-3820 |
| HSI-4700 | hand | hand_switch | plc |  |  |
| HSI-4710 | hand | hand_switch | plc |  | H-4710 |
| HSI-5300 | hand | hand_switch | plc |  | H-5300 |
| HSI-5500 | hand | hand_switch | plc |  | H-5500 |
| HSI-5501 | hand | hand_switch | plc |  | H-5501 |
| LAH-1001 | level | alarm | plc |  | L-1001 |
| LAH-1201 | level | alarm | plc |  | L-1201 |
| LAH-1201#2 | level | alarm | plc |  |  |
| LAH-1632 | level | alarm | plc |  | L-1632 |
| LAH-1701 | level | alarm | plc |  | L-1701 |
| LAH-1723 | level | alarm | plc |  | L-1723 |
| LAH-2303 | level | alarm | plc |  | L-2303 |
| LAH-2501 | level | alarm | plc |  | L-2501 |
| LAHH-2304 | level | alarm | plc |  | L-2304 |
| LAHH-2360 | level | alarm | plc |  | L-2360 |
| LAHH-5501 | level | alarm | plc |  | L-5501 |
| LAL-1631 | level | alarm | plc |  | L-1631 |
| LAL-2302 | level | alarm | plc |  | L-2302 |
| LAL-3121 | level | alarm | plc |  | L-3121 |
| LAL-3802 | level | alarm | plc |  | L-3802 |
| LAL-4301 | level | alarm | plc |  | L-4301 |
| LALL-2301 | level | alarm | plc |  | L-2301 |
| LALL-2301#2 | level | alarm | plc |  |  |
| LALL-3803 | level | alarm | plc |  | L-3803 |
| LE-1001 | level | element | field | SCR-1001 | L-1001 |
| LE-1201 | level | element | field | SCR-1201 | L-1201 |
| LE-1631 | level | element | field | TK-1630 | L-1631 |
| LE-1701 | level | element | field | GCB-1700 | L-1701 |
| LE-2201 | level | element | field | TK-2200 | L-2201 |
| LE-2601 | level | element | field | SBR-2600 | L-2601 |
| LE-2701 | level | element | field | SBR-2700 | L-2701 |
| LE-3111 | level | element | field | TK-3110 | L-3111 |
| LE-3302 | level | element | field | PSF-3300 | L-3302 |
| LE-3801 | level | element | field | TK-3800 | L-3801 |
| LE-4101 | level | element | field | SSD-4100 | L-4101 |
| LE-4201 | level | element | field | SSD-4200 | L-4201 |
| LE-4301 | level | element | field | DT-4300 | L-4301 |
| LE-5511 | level | element | field | AT-5510 | L-5511 |
| LE-5521 | level | element | field | AT-5520 | L-5521 |
| LI-1001 | level | indicator | plc |  | L-1001 |
| LI-1201 | level | indicator | plc |  | L-1201 |
| LI-1631 | level | indicator | plc |  | L-1631 |
| LI-1701 | level | indicator | plc |  | L-1701 |
| LI-2201 | level | indicator | plc |  | L-2201 |
| LI-3111 | level | indicator | plc |  | L-3111 |
| LI-3302 | level | indicator | plc |  | L-3302 |
| LI-3801 | level | indicator | plc |  | L-3801 |
| LI-5511 | level | indicator | plc |  | L-5511 |
| LI-5521 | level | indicator | plc |  | L-5521 |
| LIT-1001 | level | transmitter | field | SCR-1001 | L-1001 |
| LIT-1101 | level | transmitter | field | FIL-1101 |  |
| LIT-1201 | level | transmitter | field | SCR-1201 | L-1201 |
| LIT-1631 | level | transmitter | field | TK-1630 | L-1631 |
| LIT-1701 | level | transmitter | field | GCB-1700 | L-1701 |
| LIT-2201 | level | transmitter | field | TK-2200 | L-2201 |
| LIT-2601 | level | transmitter | field | SBR-2600 | L-2601 |
| LIT-2701 | level | transmitter | field | SBR-2700 | L-2701 |
| LIT-3111 | level | transmitter | field | TK-3110 | L-3111 |
| LIT-3302 | level | transmitter | field | PSF-3300 | L-3302 |
| LIT-3801 | level | transmitter | field | TK-3800 | L-3801 |
| LIT-4101 | level | transmitter | field | SSD-4100 | L-4101 |
| LIT-4201 | level | transmitter | field | SSD-4200 | L-4201 |
| LIT-4301 | level | transmitter | field | DT-4300 | L-4301 |
| LIT-5511 | level | transmitter | field | AT-5510 | L-5511 |
| LIT-5521 | level | transmitter | field | AT-5520 | L-5521 |
| LSH-1201 | level | switch | field | SB-1200 | L-1201 |
| LSH-1632 | level | switch | field | TK-1630 | L-1632 |
| LSH-2303 | level | switch | field | TK-2300 | L-2303 |
| LSH-2501 | level | switch | field | SB-2500 | L-2501 |
| LSH-2601 | level | switch | field | SBR-2600 | L-2601 |
| LSH-2701 | level | switch | field | SBR-2700 | L-2701 |
| LSH-3122 | level | switch | field | TK-3120 |  |
| LSH-3123 | level | switch | field | TK-3120 |  |
| LSH-3124 | level | switch | field | TK-3120 |  |
| LSH-3801 | level | switch | field | TK-3800 | L-3801 |
| LSH-4101 | level | switch | field | SSD-4100 | L-4101 |
| LSH-4201 | level | switch | field | SSD-4200 | L-4201 |
| LSH-4302 | level | switch | field | DT-4300 |  |
| LSHH-1723 | level | switch | field | GRIT ROOM (atmosphere) | L-1723 |
| LSHH-2304 | level | switch | field | TK-2300 | L-2304 |
| LSHH-2360 | level | switch | field | PLANT LIFT STATION BASEMENT | L-2360 |
| LSHH-3125 | level | switch | field | TK-3120 |  |
| LSHH-5501 | level | switch | field | ALUM SYSTEM SECONDARY CONTAINMENT AREA / TO SPILL CONTAINMENT | L-5501 |
| LSL-1631 | level | switch | field | TK-1630 | L-1631 |
| LSL-2302 | level | switch | field | TK-2300 | L-2302 |
| LSL-3121 | level | switch | field | TK-3120 | L-3121 |
| LSL-3201 | level | switch | field | UV-3200 |  |
| LSL-3802 | level | switch | field | TK-3800 | L-3802 |
| LSL-4301 | level | switch | field | DT-4300 | L-4301 |
| LSLL-2301 | level | switch | field | TK-2300 | L-2301 |
| LSLL-3803 | level | switch | field | TK-3800 | L-3803 |
| PAH-1642 | pressure | alarm | plc |  | P-1642 |
| PAH-3822 | pressure | alarm | plc |  | P-3822 |
| PAH-4711 | pressure | alarm | plc |  | P-4711 |
| PAL-1101 | pressure | alarm | plc |  | P-1101 |
| PAL-1641 | pressure | alarm | plc |  | P-1641 |
| PAL-4710 | pressure | alarm | plc |  | P-4710 |
| PC-4841 | pressure | controller | local_panel |  | P-4841 |
| PE-2310 | pressure | element | field | 200-PPE-E1 (Diaphragm seal -> CHV-2310) | P-2310 |
| PE-2320 | pressure | element | field | 200-PPE-E1 (Diaphragm seal -> CHV-2320) | P-2320 |
| PE-2330 | pressure | element | field | 200-PPE-E1 (Diaphragm seal -> CHV-2330) | P-2330 |
| PE-4801 | pressure | element | field | 150-DS-E1 (Diaphragm seal -> SCP-4800) | P-4801 |
| PI-1911 | pressure | indicator | field | 100-ARL-F3-C (Diaphragm seal -> BCV-1910) |  |
| PI-1921 | pressure | indicator | field | 100-ARL-F3-C (Diaphragm seal -> BCV-1920) |  |
| PI-2310 | pressure | indicator | field | 200-PPE-E1 (Diaphragm seal -> CHV-2310) | P-2310 |
| PI-2320 | pressure | indicator | field | 200-PPE-E1 (Diaphragm seal -> CHV-2320) | P-2320 |
| PI-2330 | pressure | indicator | field | 200-PPE-E1 (Diaphragm seal -> CHV-2330) | P-2330 |
| PI-3811 | pressure | indicator | field | 100-PSW-E1 (PSWP-3810 -> CHV-3811) |  |
| PI-3821 | pressure | indicator | field | 100-ARL-H1 (PSWP-3820 -> CHV-3821) |  |
| PI-3831 | pressure | indicator | plc |  | P-3831 |
| PI-3841 | pressure | indicator | field | TK-3840 | P-3841 |
| PI-3911 | pressure | indicator | field | 200-AAS-H1 (expansion joint -> CHV-3911) | P-3911 |
| PI-3921 | pressure | indicator | field | 150-AAS-H1 (expansion joint -> CHV-3921) | P-3921 |
| PI-3931 | pressure | indicator | field | 200-AAS-H1 (expansion joint -> CHV-3931) | P-3931 |
| PI-4011 | pressure | indicator | field | 150-AAS-H1 (expansion joint -> CHV-4011) | P-4011 |
| PI-4021 | pressure | indicator | field | 150-AAS-H1 (expansion joint -> CHV-4021) | P-4021 |
| PI-4831 | pressure | indicator | field | 80-PSW-H1 (BUV-4832 -> Screw press wash water header) | P-4831 |
| PI-4841 | pressure | indicator | field | line (PRV-4841 -> STR-4841) | P-4841 |
| PI-5311 | pressure | indicator | field | line (PRV-5311 -> BAV-5315) | P-5311 |
| PI-5321 | pressure | indicator | field | line (PRV-5321 -> BAV-5325) | P-5321 |
| PI-5331 | pressure | indicator | field | 40-PLY-E1 (MX-5330 -> reducer) | P-5331 |
| PI-5342 | pressure | indicator | field | 25-PW-E1 (FE-5342 -> MX-5330) |  |
| PI-5581 | pressure | indicator | field | 25-AL-E4 (PRV-5551 -> BAV-5553) |  |
| PIT-1101 | pressure | transmitter | field | line (CHV-1101 -> strainer) | P-1101 |
| PIT-3831 | pressure | transmitter | field | 100-PSW-E1 (STR-3831 -> BUV-3831) | P-3831 |
| PIT-4801 | pressure | transmitter | field | 150-DS-E1 (Diaphragm seal -> SCP-4800) | P-4801 |
| PS-3911 | pressure | switch | field | 200-AAS-H1 (expansion joint -> CHV-3911) | P-3911 |
| PS-3921 | pressure | switch | field | 150-AAS-H1 (expansion joint -> CHV-3921) | P-3921 |
| PS-3931 | pressure | switch | field | 200-AAS-H1 (expansion joint -> CHV-3931) | P-3931 |
| PS-4011 | pressure | switch | field | 150-AAS-H1 (expansion joint -> CHV-4011) | P-4011 |
| PS-4021 | pressure | switch | field | 150-AAS-H1 (expansion joint -> CHV-4021) | P-4021 |
| PSH-1642 | pressure | switch | field | 100-SEPS-E1 (Diaphragm seal -> CHV-1641) | P-1642 |
| PSH-1652 | pressure | switch | field | 100-SEPS-E1 (Diaphragm seal -> CHV-1651) | P-1652 |
| PSH-3812 | pressure | switch | field | 100-PSW-E1 (PSWP-3810 -> CHV-3811) | P-3812 |
| PSH-3822 | pressure | switch | field | 100-ARL-H1 (PSWP-3820 -> CHV-3821) | P-3822 |
| PSH-4711 | pressure | switch | field | 100-DS-E1 (Diaphragm seal -> CHV-4711) | P-4711 |
| PSH-4721 | pressure | switch | field | 100-DS-E1 (Diaphragm seal -> CHV-4721) | P-4721 |
| PSH-4822 | pressure | switch | field | line (COMP-4820 -> PRV-4841) |  |
| PSL-1101 | pressure | switch | field | 15-HW-H1 (HW HOT WATER SYSTEM -> BAV-1102) | P-1101 |
| PSL-1641 | pressure | switch | field | 100-SEPS-E1 (Diaphragm seal -> SEP-1640) | P-1641 |
| PSL-1651 | pressure | switch | field | 100-SEPS-E1 (Diaphragm seal -> SEP-1650) | P-1651 |
| PSL-4710 | pressure | switch | field | 150-DS-E1 (Diaphragm seal -> reducer) | P-4710 |
| PSL-4720 | pressure | switch | field | 150-DS-E1 (Diaphragm seal -> reducer) | P-4720 |
| PSL-4821 | pressure | switch | field | line (COMP-4820 -> PRV-4841) | P-4821 |
| PSL-4831 | pressure | switch | field | 80-PSW-H1 (BAV-4831 -> SP-4830) | P-4831 |
| PSL-4841 | pressure | switch | field | line (COMP-4820 -> PRV-4841) | P-4841 |
| SAL-4900 | speed/frequency | alarm | plc |  |  |
| SC-3820 | speed/frequency | controller | plc |  | S-3820 |
| SC-4700 | speed/frequency | controller | plc |  | S-4700 |
| SC-4710 | speed/frequency | controller | plc |  | S-4710 |
| SC-5300 | speed/frequency | controller | plc |  | S-5300 |
| SC-5500 | speed/frequency | controller | plc |  | S-5500 |
| SI-3820 | speed/frequency | indicator | plc |  | S-3820 |
| SI-4710 | speed/frequency | indicator | plc |  | S-4710 |
| SI-5300 | speed/frequency | indicator | plc |  | S-5300 |
| TAL-1101 | temperature | alarm | plc |  | T-1101 |
| TI-3911 | temperature | indicator | field | 200-AAS-H1 (expansion joint -> CHV-3911) | T-3911 |
| TI-3921 | temperature | indicator | field | 150-AAS-H1 (expansion joint -> CHV-3921) | T-3921 |
| TI-3931 | temperature | indicator | field | 200-AAS-H1 (expansion joint -> CHV-3931) | T-3931 |
| TI-4011 | temperature | indicator | field | 150-AAS-H1 (expansion joint -> CHV-4011) | T-4011 |
| TI-4021 | temperature | indicator | field | 150-AAS-H1 (expansion joint -> CHV-4021) | T-4021 |
| TS-1640 | temperature | switch | field | SEP-1640 | T-1640 |
| TS-1650 | temperature | switch | field | SEP-1650 | T-1650 |
| TS-3911 | temperature | switch | field | 200-AAS-H1 (expansion joint -> CHV-3911) | T-3911 |
| TS-3921 | temperature | switch | field | 150-AAS-H1 (expansion joint -> CHV-3921) | T-3921 |
| TS-3931 | temperature | switch | field | 200-AAS-H1 (expansion joint -> CHV-3931) | T-3931 |
| TS-4011 | temperature | switch | field | 150-AAS-H1 (expansion joint -> CHV-4011) | T-4011 |
| TS-4021 | temperature | switch | field | 150-AAS-H1 (expansion joint -> CHV-4021) | T-4021 |
| TS-4710 | temperature | switch | field | SLP-4710 | T-4710 |
| TS-4720 | temperature | switch | field | SLP-4720 | T-4720 |
| TS-5550 | temperature | switch | field | ASP-5550 | T-5550 |
| TS-5560 | temperature | switch | field | ASP-5560 | T-5560 |
| TSL-1101 | temperature | switch | field | 15-HW-H1 (HW HOT WATER SYSTEM -> BAV-1102) | T-1101 |
| WI-5301 | weight/force | indicator | plc |  | W-5301 |
| WIT-5301 | weight/force | transmitter | field | PYST-5301 | W-5301 |
| XA-1001 | unclassified | alarm | plc |  | X-1001 |
| XA-1001#2 | unclassified | alarm | plc |  |  |
| XA-1201 | unclassified | alarm | plc |  | X-1201 |
| XA-1221 | unclassified | alarm | plc |  |  |
| XA-1222 | unclassified | alarm | plc |  |  |
| XA-1600 | unclassified | alarm | plc |  |  |
| XA-1620 | unclassified | alarm | plc |  | X-1620 |
| XA-1621 | unclassified | alarm | plc |  | X-1621 |
| XA-1622 | unclassified | alarm | plc |  | X-1622 |
| XA-1640 | unclassified | alarm | plc |  | X-1640 |
| XA-1700 | unclassified | alarm | plc |  | X-1700 |
| XA-1721 | unclassified | alarm | plc |  | X-1721 |
| XA-1722 | unclassified | alarm | plc |  | X-1722 |
| XA-2310 | unclassified | alarm | plc |  | X-2310 |
| XA-3200A | unclassified | alarm | plc |  | X-3200 |
| XA-3200B | unclassified | alarm | plc |  | X-3200 |
| XA-3200C | unclassified | alarm | plc |  | X-3200 |
| XA-3310 | unclassified | alarm | plc |  |  |
| XA-3820 | unclassified | alarm | plc |  | X-3820 |
| XA-4700 | unclassified | alarm | plc |  | X-4700 |
| XA-4710 | unclassified | alarm | plc |  | X-4710 |
| XA-4900 | unclassified | alarm | plc |  | X-4900 |
| XA-5300 | unclassified | alarm | plc |  | X-5300 |
| XA-5500A | unclassified | alarm | plc |  | X-5500 |
| XA-5500B | unclassified | alarm | plc |  | X-5500 |
| XAH-1621 | unclassified | alarm | local_panel |  | X-1621 |
| XAH-1621#2 | unclassified | alarm | plc |  |  |
| XAH-1622 | unclassified | alarm | local_panel |  | X-1622 |
| XAH-1622#2 | unclassified | alarm | plc |  |  |
| XAH-1721 | unclassified | alarm | local_panel |  | X-1721 |
| XAH-1721#2 | unclassified | alarm | plc |  |  |
| XAH-1722 | unclassified | alarm | local_panel |  | X-1722 |
| XAH-1722#2 | unclassified | alarm | plc |  |  |
| XI-1001 | unclassified | indicator | plc |  | X-1001 |
| XI-1201 | unclassified | indicator | plc |  | X-1201 |
| XI-1640 | unclassified | indicator | plc |  | X-1640 |
| XI-1700 | unclassified | indicator | plc |  | X-1700 |
| XI-2310 | unclassified | indicator | plc |  | X-2310 |
| XI-3820 | unclassified | indicator | plc |  | X-3820 |
| XI-4700 | unclassified | indicator | plc |  | X-4700 |
| XI-4710 | unclassified | indicator | plc |  | X-4710 |
| XI-4800 | unclassified | indicator | plc |  |  |
| XI-4900A | unclassified | indicator | plc |  | X-4900 |
| XI-4900B | unclassified | indicator | plc |  | X-4900 |
| XI-5300 | unclassified | indicator | plc |  | X-5300 |
| XI-5500 | unclassified | indicator | plc |  | X-5500 |
| XS-1001A | unclassified | switch | plc |  | X-1001 |
| XS-1001B | unclassified | switch | plc |  | X-1001 |
| XS-1201A | unclassified | switch | plc |  | X-1201 |
| XS-1201B | unclassified | switch | plc |  | X-1201 |
| XS-1620 | unclassified | switch | plc |  | X-1620 |
| XS-1640 | unclassified | switch | plc |  | X-1640 |
| XS-1700 | unclassified | switch | plc |  | X-1700 |
| XS-1700#2 | unclassified | switch | plc |  | X-1700#2 |
| XS-1701 | unclassified | switch | plc |  |  |
| XS-2000 | unclassified | switch | plc |  |  |
| XS-2310 | unclassified | switch | plc |  | X-2310 |
| XS-3820 | unclassified | switch | plc |  | X-3820 |
| XS-4700 | unclassified | switch | plc |  | X-4700 |
| XS-4710 | unclassified | switch | plc |  | X-4710 |
| XS-4900A | unclassified | switch | plc |  | X-4900 |
| XS-4900B | unclassified | switch | plc |  | X-4900 |
| XS-5300 | unclassified | switch | plc |  | X-5300 |
| XS-5500 | unclassified | switch | plc |  | X-5500 |
| XS-5501 | unclassified | switch | local_panel |  | X-5501 |
| XS-5501A | unclassified | switch | plc |  | X-5501 |
| XS-5501B | unclassified | switch | plc |  | X-5501 |
| XS-5501C | unclassified | switch | plc |  | X-5501 |
| XSC-1002 | unclassified | switch | plc |  | Z-1002 |
| XSC-1702 | unclassified | switch | plc |  | Z-1702 |
| XSC-3851 | unclassified | switch | plc |  | Z-3851 |
| XSC-4102 | unclassified | switch | plc |  | Z-4102 |
| XSO-1002 | unclassified | switch | plc |  | Z-1002 |
| XSO-1005 | unclassified | switch | plc |  | X-1005 |
| XSO-1702 | unclassified | switch | plc |  | Z-1702 |
| XSO-3312 | unclassified | switch | plc |  | X-3312 |
| XSO-3851 | unclassified | switch | plc |  | Z-3851 |
| XSO-4102 | unclassified | switch | plc |  | Z-4102 |
| YC-1600 | event/state | controller | plc |  | Y-1600 |
| YI-1600 | event/state | indicator | plc |  | Y-1600 |
| YI-1600#2 | event/state | indicator | plc |  |  |
| YO-1600 | event/state | other | plc |  | Y-1600 |
| ZAC-1611 | position | controller | plc |  | Z-1611 |
| ZAO-1611 | position | alarm | plc |  | Z-1611 |
| ZC-1611 | position | controller | local_panel |  | Z-1611 |
| ZC-3201 | position | controller | plc |  | Z-3201 |
| ZH-1600 | position | other | plc |  |  |
| ZI-3201 | position | indicator | plc |  | Z-3201 |
| ZIC-1002 | position | indicator | plc |  | Z-1002 |
| ZIC-1611 | position | indicator | plc |  | Z-1611 |
| ZIC-1702 | position | indicator | plc |  | Z-1702 |
| ZIC-2206 | position | indicator | plc |  | Z-2206 |
| ZIC-3201 | position | indicator | plc |  | Z-3201 |
| ZIC-3851 | position | indicator | plc |  | Z-3851 |
| ZIC-4102 | position | indicator | plc |  | Z-4102 |
| ZIO-1002 | position | indicator | plc |  | Z-1002 |
| ZIO-1611 | position | indicator | plc |  | Z-1611 |
| ZIO-1702 | position | indicator | plc |  | Z-1702 |
| ZIO-2206 | position | indicator | plc |  | Z-2206 |
| ZIO-3201 | position | indicator | plc |  | Z-3201 |
| ZIO-3851 | position | indicator | plc |  | Z-3851 |
| ZIO-4102 | position | indicator | plc |  | Z-4102 |
| ZS-1611 | position | switch | field | PLV-1611 | Z-1611 |
| ZS-4801 | position | switch | field | SCP-4800 |  |
| ZS-4802 | position | switch | field | SCP-4800 |  |
| ZSH-2206 | position | switch | field | KGV-2206 | Z-2206 |
| ZSH-2306 | position | switch | field | KGV-2306 | Z-2306 |
| ZSL-2206 | position | switch | field | KGV-2206 | Z-2206 |
| ZSL-2306 | position | switch | field | KGV-2306 | Z-2306 |
| ZSO-3120 | position | switch | plc |  | Z-3120 |
| ZSS-4900 | position | switch | field | SCC-4900 |  |
| ZT-1611 | position | transmitter | field | PLV-1611 | Z-1611 |

## Control loops

| Loop | Type | Sensor(s) | Controller(s) | Final element(s) | Description |
|---|---|---|---|---|---|
| A-1221 | monitoring | AE-1221, AIT-1221 |  |  | Monitoring loop A-1221 (analysis). Sensed by AE-1221, AIT-1221 (HEADWORKS ROOM (atmosphere)). |
| A-1222 | monitoring | AE-1222, AIT-1222 |  |  | Monitoring loop A-1222 (analysis). Sensed by AE-1222, AIT-1222 (HEADWORKS ROOM (atmosphere)). |
| A-1621 | monitoring | AE-1621, AIT-1621 |  |  | Monitoring loop A-1621 (analysis). Sensed by AE-1621, AIT-1621 (SEPTAGE RECEIVING ROOM (atmosphere)). |
| A-1622 | monitoring | AE-1622, AIT-1622 |  |  | Monitoring loop A-1622 (analysis). Sensed by AE-1622, AIT-1622 (SEPTAGE RECEIVING ROOM (atmosphere)). |
| A-1721 | monitoring | AE-1721, AIT-1721 |  |  | Monitoring loop A-1721 (analysis). Sensed by AE-1721, AIT-1721 (GRIT ROOM (atmosphere)). |
| A-1722 | monitoring | AE-1722, AIT-1722 |  |  | Monitoring loop A-1722 (analysis). Sensed by AE-1722, AIT-1722 (GRIT ROOM (atmosphere)). |
| A-2601 | monitoring | AE-2601, AIT-2601 |  |  | Monitoring loop A-2601 (analysis). Sensed by AE-2601, AIT-2601 (SBR-2600). |
| A-2701 | monitoring | AE-2701, AIT-2701 |  |  | Monitoring loop A-2701 (analysis). Sensed by AE-2701, AIT-2701 (SBR-2700). |
| A-2801 | monitoring | AE-2801, AIT-2801 |  |  | Monitoring loop A-2801 (analysis). Sensed by AE-2801, AIT-2801 (100-WAS-H1 (BAV-2802 -> reducer)). |
| A-3201 | monitoring | AE-3201, AIT-3201 |  |  | Monitoring loop A-3201 (analysis). Sensed by AE-3201, AIT-3201 (UV-3200). |
| A-3202 | monitoring | AE-3202, AIT-3202 |  |  | Monitoring loop A-3202 (analysis). Sensed by AE-3202, AIT-3202 (UV-3200). |
| A-4101 | monitoring | AE-4101, AIT-4101 |  |  | Monitoring loop A-4101 (analysis). Sensed by AE-4101, AIT-4101 (SSD-4100). |
| A-4102 | monitoring | AE-4102, AIT-4102 |  |  | Monitoring loop A-4102 (analysis). Sensed by AE-4102, AIT-4102 (SSD-4100). |
| A-4201 | monitoring | AE-4201, AIT-4201 |  |  | Monitoring loop A-4201 (analysis). Sensed by AE-4201, AIT-4201 (SSD-4200). |
| A-4202 | monitoring | AE-4202, AIT-4202 |  |  | Monitoring loop A-4202 (analysis). Sensed by AE-4202, AIT-4202 (SSD-4200). |
| D-3831 | monitoring | DPT-3831 |  |  | Monitoring loop D-3831 (density). Sensed by DPT-3831 (STR-3831). |
| D-3911 | monitoring | DPT-3911 |  |  | Monitoring loop D-3911 (density). Sensed by DPT-3911 (filter). |
| D-3921 | monitoring | DPT-3921 |  |  | Monitoring loop D-3921 (density). Sensed by DPT-3921 (filter). |
| D-3931 | monitoring | DPT-3931 |  |  | Monitoring loop D-3931 (density). Sensed by DPT-3931 (filter). |
| D-4011 | monitoring | DPT-4011 |  |  | Monitoring loop D-4011 (density). Sensed by DPT-4011 (filter). |
| D-4021 | monitoring | DPT-4021 |  |  | Monitoring loop D-4021 (density). Sensed by DPT-4021 (filter). |
| E-1200 | monitoring |  |  |  | Monitoring loop E-1200 (voltage). |
| E-1620 | monitoring |  |  |  | Monitoring loop E-1620 (voltage). |
| E-1700 | monitoring |  |  |  | Monitoring loop E-1700 (voltage). |
| E-1701 | monitoring |  |  |  | Monitoring loop E-1701 (voltage). |
| E-1900 | monitoring |  |  |  | Monitoring loop E-1900 (voltage). |
| E-2000 | monitoring |  |  |  | Monitoring loop E-2000 (voltage). |
| E-5501 | monitoring |  |  |  | Monitoring loop E-5501 (voltage). |
| F-1001 | monitoring | FE-1001, FIT-1001 |  |  | Monitoring loop F-1001 (flow). Sensed by FE-1001, FIT-1001 (in-line on 200-RWW-E1 (RSW FROM LIFT STATION #1 -> KGV-1001)). |
| F-1201 | monitoring | FE-1201, FIT-1201 |  |  | Monitoring loop F-1201 (flow). Sensed by FE-1201, FIT-1201 (in-line on 200-RWW-H1 (RSW FROM LIFT STATION #2 -> KGV-1201)). |
| F-1601 | monitoring | FE-1601, FIT-1601 |  |  | Monitoring loop F-1601 (flow). Sensed by FE-1601, FIT-1601 (in-line on 100-SEPS-H1 (GRD-1620 -> BAV-1605)). |
| F-1641 | monitoring | FE-1641, FIT-1641 |  |  | Monitoring loop F-1641 (flow). Sensed by FE-1641, FIT-1641 (in-line on 100-SEPS-E1 (reducer -> reducer)). |
| F-2352 | monitoring | FE-2352, FIT-2352 |  |  | Monitoring loop F-2352 (flow). Sensed by FE-2352, FIT-2352 (in-line on 200-PPE-E1 (KGV-2332 -> reducer)). |
| F-2801 | monitoring | FE-2801, FIT-2801 |  |  | Monitoring loop F-2801 (flow). Sensed by FE-2801, FIT-2801 (in-line on 100-WAS-H1 (reducer -> reducer)). |
| F-3201 | monitoring | FE-3201, FIT-3201 |  |  | Monitoring loop F-3201 (flow). Sensed by FE-3201, FIT-3201 (in-line on 300-SE-H1 (reducer -> BUV-3201)). |
| F-3301 | control | FE-3301, FIT-3301 |  | SMP-3310 | Control loop F-3301 (flow). Sensed by FE-3301, FIT-3301 (PSF-3300). Acts on SMP-3310. |
| F-3831 | monitoring | FE-3831, FIT-3831 |  |  | Monitoring loop F-3831 (flow). Sensed by FE-3831, FIT-3831 (in-line on 100-PSW-E1 (reducer -> reducer)). |
| F-4410 | monitoring | FE-4410, FIT-4410 |  |  | Monitoring loop F-4410 (flow). Sensed by FE-4410, FIT-4410 (in-line on 200-SUP-E1 (reducer -> reducer)). |
| F-4731 | monitoring | FE-4731, FIT-4731 |  |  | Monitoring loop F-4731 (flow). Sensed by FE-4731, FIT-4731 (in-line on 100-DS-E1 (reducer -> reducer)). |
| F-4812 | monitoring | FE-4812, FIT-4812 |  |  | Monitoring loop F-4812 (flow). Sensed by FE-4812, FIT-4812 (in-line on 40-PLY-E1 (reducer -> BAV-4811)). |
| F-5300 | control |  | FC-5300 | SNV-5342 | Control loop F-5300 (flow). Controlled by FC-5300 (plc). Acts on SNV-5342 on 25-PW-E1. |
| F-5342 | monitoring | FE-5342, FIT-5342 |  |  | Monitoring loop F-5342 (flow). Sensed by FE-5342, FIT-5342 (in-line on 25-PW-E1 (PRV-5342 -> MX-5330)). |
| H-1200 | interlock |  |  | SCR-1201, SNV-1201 | Interlock loop H-1200 (hand). Acts on SCR-1201; SNV-1201 on 50-PSW-E1. |
| H-1201 | interlock |  |  | SCR-1201 | Interlock loop H-1201 (hand). Acts on SCR-1201. |
| H-1620 | manual |  |  | GRD-1620 | Manual loop H-1620 (hand). Acts on GRD-1620. |
| H-1640 | interlock |  |  | SEP-1640 | Interlock loop H-1640 (hand). Acts on SEP-1640. |
| H-1701 | manual |  |  | MX-1701 | Manual loop H-1701 (hand). Acts on MX-1701. |
| H-1900 | manual |  |  | GTP-1920, GTP-1910 | Manual loop H-1900 (hand). Acts on GTP-1920; GTP-1910. |
| H-2000 | interlock |  |  | GCL-2000 | Interlock loop H-2000 (hand). Acts on GCL-2000. |
| H-2000#2 | interlock |  |  | MX-1701 | Interlock loop H-2000#2 (hand). Acts on MX-1701. |
| H-2000#3 | interlock |  |  | GCL-2000 | Interlock loop H-2000#3 (hand). Acts on GCL-2000. |
| H-2310 | interlock |  |  | RWP-2330, RWP-2320, RWP-2310 | Interlock loop H-2310 (hand). Acts on RWP-2330; RWP-2320; RWP-2310. |
| H-3820 | interlock |  |  | PSWP-3820, PSWP-3810 | Interlock loop H-3820 (hand). Acts on PSWP-3820; PSWP-3810. |
| H-3910 | manual |  |  | BLO-3910 | Manual loop H-3910 (hand). Acts on BLO-3910. |
| H-3920 | manual |  |  | BLO-3920 | Manual loop H-3920 (hand). Acts on BLO-3920. |
| H-3930 | manual |  |  | BLO-3930 | Manual loop H-3930 (hand). Acts on BLO-3930. |
| H-4710 | interlock |  |  | SLP-4720, SLP-4710 | Interlock loop H-4710 (hand). Acts on SLP-4720; SLP-4710. |
| H-5300 | manual |  |  | MX-5330 | Manual loop H-5300 (hand). Acts on MX-5330. |
| H-5500 | interlock |  |  | ASP-5560, ASP-5550 | Interlock loop H-5500 (hand). Acts on ASP-5560; ASP-5550. |
| H-5501 | monitoring |  |  |  | Monitoring loop H-5501 (hand). |
| L-1001 | monitoring | LE-1001, LIT-1001 |  |  | Monitoring loop L-1001 (level). Sensed by LE-1001, LIT-1001 (SCR-1001). |
| L-1201 | monitoring | LSH-1201, LE-1201, LIT-1201 |  |  | Monitoring loop L-1201 (level). Sensed by LSH-1201, LE-1201, LIT-1201 (SB-1200; SCR-1201). |
| L-1631 | monitoring | LE-1631, LIT-1631, LSL-1631 |  |  | Monitoring loop L-1631 (level). Sensed by LE-1631, LIT-1631, LSL-1631 (TK-1630). |
| L-1632 | monitoring | LSH-1632 |  |  | Monitoring loop L-1632 (level). Sensed by LSH-1632 (TK-1630). |
| L-1701 | monitoring | LE-1701, LIT-1701 |  |  | Monitoring loop L-1701 (level). Sensed by LE-1701, LIT-1701 (GCB-1700). |
| L-1723 | monitoring | LSHH-1723 |  |  | Monitoring loop L-1723 (level). Sensed by LSHH-1723 (GRIT ROOM (atmosphere)). |
| L-2201 | monitoring | LE-2201, LIT-2201 |  |  | Monitoring loop L-2201 (level). Sensed by LE-2201, LIT-2201 (TK-2200). |
| L-2301 | interlock | LSLL-2301 |  |  | Interlock loop L-2301 (level). Sensed by LSLL-2301 (TK-2300). |
| L-2302 | monitoring | LSL-2302 |  |  | Monitoring loop L-2302 (level). Sensed by LSL-2302 (TK-2300). |
| L-2303 | monitoring | LSH-2303 |  |  | Monitoring loop L-2303 (level). Sensed by LSH-2303 (TK-2300). |
| L-2304 | monitoring | LSHH-2304 |  |  | Monitoring loop L-2304 (level). Sensed by LSHH-2304 (TK-2300). |
| L-2360 | monitoring | LSHH-2360 |  |  | Monitoring loop L-2360 (level). Sensed by LSHH-2360 (PLANT LIFT STATION BASEMENT). |
| L-2501 | monitoring | LSH-2501 |  |  | Monitoring loop L-2501 (level). Sensed by LSH-2501 (SB-2500). |
| L-2601 | monitoring | LSH-2601, LE-2601, LIT-2601 |  |  | Monitoring loop L-2601 (level). Sensed by LSH-2601, LE-2601, LIT-2601 (SBR-2600). |
| L-2701 | monitoring | LSH-2701, LE-2701, LIT-2701 |  |  | Monitoring loop L-2701 (level). Sensed by LSH-2701, LE-2701, LIT-2701 (SBR-2700). |
| L-3111 | monitoring | LE-3111, LIT-3111 |  |  | Monitoring loop L-3111 (level). Sensed by LE-3111, LIT-3111 (TK-3110). |
| L-3121 | monitoring | LSL-3121 |  |  | Monitoring loop L-3121 (level). Sensed by LSL-3121 (TK-3120). |
| L-3302 | monitoring | LE-3302, LIT-3302 |  |  | Monitoring loop L-3302 (level). Sensed by LE-3302, LIT-3302 (PSF-3300). |
| L-3801 | monitoring | LE-3801, LIT-3801, LSH-3801 |  |  | Monitoring loop L-3801 (level). Sensed by LE-3801, LIT-3801, LSH-3801 (TK-3800). |
| L-3802 | monitoring | LSL-3802 |  |  | Monitoring loop L-3802 (level). Sensed by LSL-3802 (TK-3800). |
| L-3803 | interlock | LSLL-3803 |  |  | Interlock loop L-3803 (level). Sensed by LSLL-3803 (TK-3800). |
| L-4101 | monitoring | LSH-4101, LE-4101, LIT-4101 |  |  | Monitoring loop L-4101 (level). Sensed by LSH-4101, LE-4101, LIT-4101 (SSD-4100). |
| L-4201 | monitoring | LSH-4201, LE-4201, LIT-4201 |  |  | Monitoring loop L-4201 (level). Sensed by LSH-4201, LE-4201, LIT-4201 (SSD-4200). |
| L-4301 | interlock | LE-4301, LIT-4301, LSL-4301 |  |  | Interlock loop L-4301 (level). Sensed by LE-4301, LIT-4301, LSL-4301 (DT-4300). |
| L-5501 | monitoring | LSHH-5501 |  |  | Monitoring loop L-5501 (level). Sensed by LSHH-5501 (ALUM SYSTEM SECONDARY CONTAINMENT AREA / TO SPILL CONTAINMENT). |
| L-5511 | monitoring | LE-5511, LIT-5511 |  |  | Monitoring loop L-5511 (level). Sensed by LE-5511, LIT-5511 (AT-5510). |
| L-5521 | monitoring | LE-5521, LIT-5521 |  |  | Monitoring loop L-5521 (level). Sensed by LE-5521, LIT-5521 (AT-5520). |
| P-1101 | monitoring | PSL-1101, PIT-1101 |  |  | Monitoring loop P-1101 (pressure). Sensed by PSL-1101, PIT-1101 (15-HW-H1 (HW HOT WATER SYSTEM -> BAV-1102); line (CHV-1101 -> strainer)). |
| P-1641 | interlock | PSL-1641 |  | SEP-1640 | Interlock loop P-1641 (pressure). Sensed by PSL-1641 (100-SEPS-E1 (Diaphragm seal -> SEP-1640)). Acts on SEP-1640. |
| P-1642 | interlock | PSH-1642 |  | SEP-1640 | Interlock loop P-1642 (pressure). Sensed by PSH-1642 (100-SEPS-E1 (Diaphragm seal -> CHV-1641)). Acts on SEP-1640. |
| P-1651 | interlock | PSL-1651 |  | SEP-1650 | Interlock loop P-1651 (pressure). Sensed by PSL-1651 (100-SEPS-E1 (Diaphragm seal -> SEP-1650)). Acts on SEP-1650. |
| P-1652 | interlock | PSH-1652 |  | SEP-1650 | Interlock loop P-1652 (pressure). Sensed by PSH-1652 (100-SEPS-E1 (Diaphragm seal -> CHV-1651)). Acts on SEP-1650. |
| P-2310 | monitoring | PE-2310, PI-2310 |  |  | Monitoring loop P-2310 (pressure). Sensed by PE-2310, PI-2310 (200-PPE-E1 (Diaphragm seal -> CHV-2310)). |
| P-2320 | monitoring | PE-2320, PI-2320 |  |  | Monitoring loop P-2320 (pressure). Sensed by PE-2320, PI-2320 (200-PPE-E1 (Diaphragm seal -> CHV-2320)). |
| P-2330 | monitoring | PE-2330, PI-2330 |  |  | Monitoring loop P-2330 (pressure). Sensed by PE-2330, PI-2330 (200-PPE-E1 (Diaphragm seal -> CHV-2330)). |
| P-3812 | interlock | PSH-3812 |  | PSWP-3810 | Interlock loop P-3812 (pressure). Sensed by PSH-3812 (100-PSW-E1 (PSWP-3810 -> CHV-3811)). Acts on PSWP-3810. |
| P-3822 | interlock | PSH-3822 |  | PSWP-3820 | Interlock loop P-3822 (pressure). Sensed by PSH-3822 (100-ARL-H1 (PSWP-3820 -> CHV-3821)). Acts on PSWP-3820. |
| P-3831 | monitoring | PIT-3831 |  |  | Monitoring loop P-3831 (pressure). Sensed by PIT-3831 (100-PSW-E1 (STR-3831 -> BUV-3831)). |
| P-3841 | monitoring | PI-3841 |  |  | Monitoring loop P-3841 (pressure). Sensed by PI-3841 (TK-3840). |
| P-3911 | interlock | PI-3911, PS-3911 |  | BLO-3910 | Interlock loop P-3911 (pressure). Sensed by PI-3911, PS-3911 (200-AAS-H1 (expansion joint -> CHV-3911)). Acts on BLO-3910. |
| P-3921 | interlock | PI-3921, PS-3921 |  | BLO-3920 | Interlock loop P-3921 (pressure). Sensed by PI-3921, PS-3921 (150-AAS-H1 (expansion joint -> CHV-3921)). Acts on BLO-3920. |
| P-3931 | interlock | PI-3931, PS-3931 |  | BLO-3930 | Interlock loop P-3931 (pressure). Sensed by PI-3931, PS-3931 (200-AAS-H1 (expansion joint -> CHV-3931)). Acts on BLO-3930. |
| P-4011 | interlock | PI-4011, PS-4011 |  | BLO-4010 | Interlock loop P-4011 (pressure). Sensed by PI-4011, PS-4011 (150-AAS-H1 (expansion joint -> CHV-4011)). Acts on BLO-4010. |
| P-4021 | interlock | PI-4021, PS-4021 |  | BLO-4020 | Interlock loop P-4021 (pressure). Sensed by PI-4021, PS-4021 (150-AAS-H1 (expansion joint -> CHV-4021)). Acts on BLO-4020. |
| P-4710 | interlock | PSL-4710 |  | SLP-4710 | Interlock loop P-4710 (pressure). Sensed by PSL-4710 (150-DS-E1 (Diaphragm seal -> reducer)). Acts on SLP-4710. |
| P-4711 | interlock | PSH-4711 |  | SLP-4710 | Interlock loop P-4711 (pressure). Sensed by PSH-4711 (100-DS-E1 (Diaphragm seal -> CHV-4711)). Acts on SLP-4710. |
| P-4720 | interlock | PSL-4720 |  | SLP-4720 | Interlock loop P-4720 (pressure). Sensed by PSL-4720 (150-DS-E1 (Diaphragm seal -> reducer)). Acts on SLP-4720. |
| P-4721 | interlock | PSH-4721 |  | SLP-4720 | Interlock loop P-4721 (pressure). Sensed by PSH-4721 (100-DS-E1 (Diaphragm seal -> CHV-4721)). Acts on SLP-4720. |
| P-4801 | monitoring | PE-4801, PIT-4801 |  |  | Monitoring loop P-4801 (pressure). Sensed by PE-4801, PIT-4801 (150-DS-E1 (Diaphragm seal -> SCP-4800)). |
| P-4821 | monitoring | PSL-4821 |  |  | Monitoring loop P-4821 (pressure). Sensed by PSL-4821 (line (COMP-4820 -> PRV-4841)). |
| P-4831 | monitoring | PSL-4831, PI-4831 |  |  | Monitoring loop P-4831 (pressure). Sensed by PSL-4831, PI-4831 (80-PSW-H1 (BAV-4831 -> SP-4830); 80-PSW-H1 (BUV-4832 -> Screw press wash water header)). |
| P-4841 | control | PSL-4841, PI-4841 | PC-4841 | SNV-4841 | Control loop P-4841 (pressure). Sensed by PSL-4841, PI-4841 (line (COMP-4820 -> PRV-4841); line (PRV-4841 -> STR-4841)). Controlled by PC-4841 (local_panel). Acts on SNV-4841. |
| P-5311 | monitoring | PI-5311 |  |  | Monitoring loop P-5311 (pressure). Sensed by PI-5311 (line (PRV-5311 -> BAV-5315)). |
| P-5321 | monitoring | PI-5321 |  |  | Monitoring loop P-5321 (pressure). Sensed by PI-5321 (line (PRV-5321 -> BAV-5325)). |
| P-5331 | monitoring | PI-5331 |  |  | Monitoring loop P-5331 (pressure). Sensed by PI-5331 (40-PLY-E1 (MX-5330 -> reducer)). |
| S-3820 | control |  | SC-3820 | PSWP-3820, PSWP-3810 | Control loop S-3820 (speed/frequency). Controlled by SC-3820 (plc). Acts on PSWP-3820; PSWP-3810. |
| S-4700 | control |  | SC-4700 |  | Control loop S-4700 (speed/frequency). Controlled by SC-4700 (plc). Cascade master: sets the setpoint of S-4710. |
| S-4710 | control |  | SC-4710 | SLP-4720, SLP-4710 | Control loop S-4710 (speed/frequency). Controlled by SC-4710 (plc). Acts on SLP-4720; SLP-4710. Cascade slave of S-4700. |
| S-5300 | control |  | SC-5300 | PLP-5320, PLP-5310 | Control loop S-5300 (speed/frequency). Controlled by SC-5300 (plc). Acts on PLP-5320; PLP-5310. |
| S-5500 | control |  | SC-5500 | ASP-5560, ASP-5550 | Control loop S-5500 (speed/frequency). Controlled by SC-5500 (plc). Acts on ASP-5560; ASP-5550. |
| T-1101 | monitoring | TSL-1101 |  |  | Monitoring loop T-1101 (temperature). Sensed by TSL-1101 (15-HW-H1 (HW HOT WATER SYSTEM -> BAV-1102)). |
| T-1640 | interlock | TS-1640 |  | SEP-1640 | Interlock loop T-1640 (temperature). Sensed by TS-1640 (SEP-1640). Acts on SEP-1640. |
| T-1650 | interlock | TS-1650 |  | SEP-1650 | Interlock loop T-1650 (temperature). Sensed by TS-1650 (SEP-1650). Acts on SEP-1650. |
| T-3911 | interlock | TI-3911, TS-3911 |  | BLO-3910 | Interlock loop T-3911 (temperature). Sensed by TI-3911, TS-3911 (200-AAS-H1 (expansion joint -> CHV-3911)). Acts on BLO-3910. |
| T-3921 | interlock | TI-3921, TS-3921 |  | BLO-3920 | Interlock loop T-3921 (temperature). Sensed by TI-3921, TS-3921 (150-AAS-H1 (expansion joint -> CHV-3921)). Acts on BLO-3920. |
| T-3931 | interlock | TI-3931, TS-3931 |  | BLO-3930 | Interlock loop T-3931 (temperature). Sensed by TI-3931, TS-3931 (200-AAS-H1 (expansion joint -> CHV-3931)). Acts on BLO-3930. |
| T-4011 | interlock | TI-4011, TS-4011 |  | BLO-4010 | Interlock loop T-4011 (temperature). Sensed by TI-4011, TS-4011 (150-AAS-H1 (expansion joint -> CHV-4011)). Acts on BLO-4010. |
| T-4021 | interlock | TI-4021, TS-4021 |  | BLO-4020 | Interlock loop T-4021 (temperature). Sensed by TI-4021, TS-4021 (150-AAS-H1 (expansion joint -> CHV-4021)). Acts on BLO-4020. |
| T-4710 | interlock | TS-4710 |  | SLP-4710 | Interlock loop T-4710 (temperature). Sensed by TS-4710 (SLP-4710). Acts on SLP-4710. |
| T-4720 | interlock | TS-4720 |  | SLP-4720 | Interlock loop T-4720 (temperature). Sensed by TS-4720 (SLP-4720). Acts on SLP-4720. |
| T-5550 | interlock | TS-5550 |  | ASP-5550 | Interlock loop T-5550 (temperature). Sensed by TS-5550 (ASP-5550). Acts on ASP-5550. |
| T-5560 | interlock | TS-5560 |  | ASP-5560 | Interlock loop T-5560 (temperature). Sensed by TS-5560 (ASP-5560). Acts on ASP-5560. |
| W-5301 | monitoring | WIT-5301 |  |  | Monitoring loop W-5301 (weight/force). Sensed by WIT-5301 (PYST-5301). |
| X-1001 | on_off | XS-1001A, XS-1001B |  | SCR-1001 | On off loop X-1001 (unclassified). Sensed by XS-1001A, XS-1001B. Acts on SCR-1001. |
| X-1005 | on_off | XSO-1005 |  | SNV-1005 | On off loop X-1005 (unclassified). Sensed by XSO-1005. Acts on SNV-1005. |
| X-1201 | on_off | XS-1201A, XS-1201B |  | SCR-1201 | On off loop X-1201 (unclassified). Sensed by XS-1201A, XS-1201B. Acts on SCR-1201. |
| X-1620 | on_off | XS-1620 |  | GRD-1620 | On off loop X-1620 (unclassified). Sensed by XS-1620. Acts on GRD-1620. |
| X-1621 | monitoring | XAH-1621 |  |  | Monitoring loop X-1621 (unclassified). Sensed by XAH-1621. |
| X-1622 | monitoring | XAH-1622 |  |  | Monitoring loop X-1622 (unclassified). Sensed by XAH-1622. |
| X-1640 | on_off | XS-1640 |  | SEP-1640 | On off loop X-1640 (unclassified). Sensed by XS-1640. Acts on SEP-1640. |
| X-1700 | monitoring | XS-1700 |  |  | Monitoring loop X-1700 (unclassified). Sensed by XS-1700. |
| X-1700#2 | on_off | XS-1700#2 |  | MX-1701 | On off loop X-1700#2 (unclassified). Sensed by XS-1700#2. Acts on MX-1701. |
| X-1721 | monitoring | XAH-1721 |  |  | Monitoring loop X-1721 (unclassified). Sensed by XAH-1721. |
| X-1722 | monitoring | XAH-1722 |  |  | Monitoring loop X-1722 (unclassified). Sensed by XAH-1722. |
| X-2310 | on_off | XS-2310 |  | RWP-2330, RWP-2320, RWP-2310 | On off loop X-2310 (unclassified). Sensed by XS-2310. Acts on RWP-2330; RWP-2320; RWP-2310. |
| X-3200 | monitoring |  |  |  | Monitoring loop X-3200 (unclassified). |
| X-3312 | on_off | XSO-3312 |  | SNV-3312 | On off loop X-3312 (unclassified). Sensed by XSO-3312. Acts on SNV-3312 on 25-SAM-E1. |
| X-3820 | on_off | XS-3820 |  | PSWP-3820, PSWP-3810 | On off loop X-3820 (unclassified). Sensed by XS-3820. Acts on PSWP-3820; PSWP-3810. |
| X-4700 | monitoring | XS-4700 |  |  | Monitoring loop X-4700 (unclassified). Sensed by XS-4700. |
| X-4710 | on_off | XS-4710 |  | SLP-4720, SLP-4710 | On off loop X-4710 (unclassified). Sensed by XS-4710. Acts on SLP-4720; SLP-4710. |
| X-4900 | on_off | XS-4900A, XS-4900B |  | SCC-4900 | On off loop X-4900 (unclassified). Sensed by XS-4900A, XS-4900B. Acts on SCC-4900. |
| X-5300 | on_off | XS-5300 |  | MX-5330 | On off loop X-5300 (unclassified). Sensed by XS-5300. Acts on MX-5330. |
| X-5500 | on_off | XS-5500 |  | ASP-5560, ASP-5550 | On off loop X-5500 (unclassified). Sensed by XS-5500. Acts on ASP-5560; ASP-5550. |
| X-5501 | monitoring | XS-5501, XS-5501A, XS-5501B, XS-5501C |  |  | Monitoring loop X-5501 (unclassified). Sensed by XS-5501, XS-5501A, XS-5501B, XS-5501C. |
| Y-1600 | control |  | YC-1600 |  | Control loop Y-1600 (event/state). Controlled by YC-1600 (plc). |
| Z-1002 | on_off | XSO-1002, XSC-1002 |  | KGV-1002 | On off loop Z-1002 (position). Sensed by XSO-1002, XSC-1002. Acts on KGV-1002 on 400-RWW-H1. |
| Z-1611 | control | ZT-1611, ZS-1611 | ZC-1611, ZAC-1611 | PLV-1611 | Control loop Z-1611 (position). Sensed by ZT-1611, ZS-1611 (PLV-1611). Controlled by ZC-1611, ZAC-1611 (local_panel, plc). Acts on PLV-1611 on 100-SEPS-H1. |
| Z-1702 | on_off | XSO-1702, XSC-1702 |  | KGV-1702 | On off loop Z-1702 (position). Sensed by XSO-1702, XSC-1702. Acts on KGV-1702 on 400-RWW-H1. |
| Z-2206 | monitoring | ZSH-2206, ZSL-2206 |  |  | Monitoring loop Z-2206 (position). Sensed by ZSH-2206, ZSL-2206 (KGV-2206). |
| Z-2306 | monitoring | ZSH-2306, ZSL-2306 |  |  | Monitoring loop Z-2306 (position). Sensed by ZSH-2306, ZSL-2306 (KGV-2306). |
| Z-3120 | on_off | ZSO-3120 |  | BUV-3120 | On off loop Z-3120 (position). Sensed by ZSO-3120. Acts on BUV-3120 on 400-SE-H1. |
| Z-3201 | control |  | ZC-3201 | BUV-3201 | Control loop Z-3201 (position). Controlled by ZC-3201 (plc). Acts on BUV-3201 on 300-SE-H1. |
| Z-3851 | on_off | XSO-3851, XSC-3851 |  | BUV-3851 | On off loop Z-3851 (position). Sensed by XSO-3851, XSC-3851. Acts on BUV-3851 on 100-PW-E1. |
| Z-4102 | on_off | XSO-4102, XSC-4102 |  | PLV-4102 | On off loop Z-4102 (position). Sensed by XSO-4102, XSC-4102. Acts on PLV-4102 on 150-DS-H1. |

## Off-page connections

| Sheet | Connector | Direction | Other drawing | Linked to |
|---|---|---|---|---|
| D-007-0 | RWW TO GRIT REMOVAL SYSTEM | out | D-009 | RWW 1 D-007 HEADWORKS (D-009-0) |
| D-008-0 | SEPS 1 D-009 GRIT CHAMBER | out | D-009 | SEPS 1 D-008 SEPTAGE PUMP (D-009-0) |
| D-009-0 | DR 1 D-010 PLANT LIFT STATION | out | D-010 | DR 1 D-009 FROM GRIT REMOVAL (D-010-0) |
| D-009-0 | RWW 1 D-007 HEADWORKS | in | D-007 | RWW TO GRIT REMOVAL SYSTEM (D-007-0) |
| D-009-0 | PPE 2 D-010 PLANT LIFT STATION | out | D-010 | PPE 2 D-009 FROM GRIT REMOVAL (D-010-0) |
| D-009-0 | SEPS 1 D-008 SEPTAGE PUMP | in | D-008 | SEPS 1 D-009 GRIT CHAMBER (D-008-0) |
| D-010-0 | AL 3 D-016 FROM ALUM SKID | in | D-016 | AL 3 D-010 PLANT LIFT STATION DISCHARGE HEADER (D-016-0) |
| D-010-0 | DR 1 D-015 DEWATERING ROOM | in | D-015 | DR 1 D-010 PLANT LIFT STATION (D-015-0) |
| D-010-0 | DR 1 D-009 FROM GRIT REMOVAL | in | D-009 | DR 1 D-010 PLANT LIFT STATION (D-009-0) |
| D-010-0 | OV 3 D-012 TO PARSHALL FLUME | out | D-012 | OV 3 D-010 PLANT LIFT STATION (D-012-0) |
| D-010-0 | PPE 2 D-009 FROM GRIT REMOVAL | in | D-009 | PPE 2 D-010 PLANT LIFT STATION (D-009-0) |
| D-010-0 | PPE 1 D-011 TO SBR INFLUENT CHAMBER | out | D-011 | PPE 1 D-010 FROM PLANT LIFT STATION (D-011-0) |
| D-010-0 | SUP 2 D-014 DIGESTER DECANTER | in | D-014 | SUP 2 D-010 PLANT LIFT STATION (D-014-0) |
| D-011-0 | AAS 1 D-013 FROM BLOWER ROOM | in | D-013 | AAS 1 D-011 SBR #1 (D-013-0) |
| D-011-0 | AAS 2 D-013 FROM BLOWER ROOM | in | D-013 | AAS 2 D-011 SBR #2 (D-013-0) |
| D-011-0 | OV 3 D-012 TO PARSHALL FLUME | out | D-012 | OV 3 D-011 FROM EQUALIZATION TANK (D-012-0) |
| D-011-0 | PPE 1 D-010 FROM PLANT LIFT STATION | in | D-010 | PPE 1 D-011 TO SBR INFLUENT CHAMBER (D-010-0) |
| D-011-0 | SE 1 D-012 TO UV CHANNEL | out | D-012 | SE 1 D-011 FROM EQUALIZATION TANK (D-012-0) |
| D-011-0 | WAS 2 D-014 TO DIGESTERS | out | D-014 | WAS 2 D-011 FROM SBR WAS PUMPS (D-014-0) |
| D-012-0 | PSW 1 D-015 TO DEWATERING SYSTEM | out | D-015 | PSW 1 D-012 PLANT SERVICE WATER STATION WET WELL (D-015-0) |
| D-012-0 | OV 3 D-010 PLANT LIFT STATION | in | D-010 | OV 3 D-012 TO PARSHALL FLUME (D-010-0) |
| D-012-0 | OV 3 D-011 FROM EQUALIZATION TANK | in | D-011 | OV 3 D-012 TO PARSHALL FLUME (D-011-0) |
| D-012-0 | SE 1 D-011 FROM EQUALIZATION TANK | in | D-011 | SE 1 D-012 TO UV CHANNEL (D-011-0) |
| D-013-0 | AAS 2 D-014 DIGESTER #1 | out | D-014 | AAS 1 D-013 FROM BLOWER ROOM (D-014-0) |
| D-013-0 | AAS 1 D-014 DIGESTER #2 | out | D-014 | AAS 2 D-013 FROM BLOWER ROOM (D-014-0) |
| D-013-0 | AAS 1 D-011 SBR #1 | out | D-011 | AAS 1 D-013 FROM BLOWER ROOM (D-011-0) |
| D-013-0 | AAS 2 D-011 SBR #2 | out | D-011 | AAS 2 D-013 FROM BLOWER ROOM (D-011-0) |
| D-014-0 | AAS 1 D-013 FROM BLOWER ROOM | in | D-013 | AAS 2 D-014 DIGESTER #1 (D-013-0) |
| D-014-0 | AAS 2 D-013 FROM BLOWER ROOM | in | D-013 | AAS 1 D-014 DIGESTER #2 (D-013-0) |
| D-014-0 | DS 1 D-015 SLUDGE TRANSFER PUMPS | out | D-015 | DS 1 D-014 DIGESTER DAY TANK (D-015-0) |
| D-014-0 | SUP 2 D-010 PLANT LIFT STATION | out | D-010 | SUP 2 D-014 DIGESTER DECANTER (D-010-0) |
| D-014-0 | WAS 2 D-011 FROM SBR WAS PUMPS | in | D-011 | WAS 2 D-014 TO DIGESTERS (D-011-0) |
| D-015-0 | DR 1 D-010 PLANT LIFT STATION | out | D-010 | DR 1 D-015 DEWATERING ROOM (D-010-0) |
| D-015-0 | DS 1 D-014 DIGESTER DAY TANK | in | D-014 | DS 1 D-015 SLUDGE TRANSFER PUMPS (D-014-0) |
| D-015-0 | PSW 1 D-012 PLANT SERVICE WATER STATION WET WELL | in | D-012 | PSW 1 D-015 TO DEWATERING SYSTEM (D-012-0) |
| D-016-0 | AL 3 D-010 PLANT LIFT STATION DISCHARGE HEADER | out | D-010 | AL 3 D-016 FROM ALUM SKID (D-010-0) |

## Data quality

0 errors, 22 warnings and 26 informational items; see `qa_report.md`. Every node carries `confidence` and the sheet region it was read from (`provenance`). This graph was machine-extracted from drawings and must be verified by a qualified engineer before use in design, operations or safety work.
