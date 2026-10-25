# ruttan: process knowledge graph summary

Built from `ruttan.pdf` (2 sheets) by pid-to-kg 0.1.0 on 2026-10-25. The graph has 333 nodes and 478 edges; this summary covers equipment-level flow, instruments and control loops. Query `graph.duckdb` or `graph.json` for pipe-segment and valve detail.

| Equipment | Instruments | Valves & fittings | Pipe segments | Control loops | Off-page links |
|---|---|---|---|---|---|
| 38 | 71 | 67 | 115 | 26 | 10 |

## Sheets

| Page | Drawing | Title | Type |
|---|---|---|---|
| 1 | M701 | P&ID Water Treatment Plant (Ruttan Mine Site Remediation, Contract C-700) | pid |
| 2 | M702 | P&ID Pumping Stations (Ruttan Mine Site Remediation, Contract C-700) | pid |

## Process flow (equipment to equipment)

Each line reads *upstream → downstream*, with the pipe lines and in-line items between them. Pipes, valves and instruments are collapsed; use `kg_query.py path` for the full route.

- **Lower header spare 8" blind end** → **RUTTAN OPEN PIT (EL 280.0 max / 245.0 min MASL)**: lines 14"-CTW-004, 2"-CTW-006; through gate valve, relief valve
- **Lower header spare 8" blind end** → **REACTOR-2** (REACTOR 2 (V=20,000 USGAL)): lines 14"-CTW-004, 10"-CTW-004; through reducer, reducer, FE-2; crosses sheets
- **REACTOR-2** (REACTOR 2 (V=20,000 USGAL)) → **MILL POND (EL 285.76 m)**: lines 14"-TW-002; crosses sheets
- **MILL POND (EL 285.76 m)** → **BREHAUT LAKE (FUTURE)**: lines 14"-TW-003
- **MILL POND (EL 285.76 m)** → **RUTTAN LAKE**: lines 14"-TW-003
- **LIME TRUCK (pneumatic unloading)** → **S-1** (PORTABLE SLAKER S-1 (V=23,200 USGAL)): lines 4"-L-001
- **S-1** (PORTABLE SLAKER S-1 (V=23,200 USGAL)) → **SLAKER TRANSFER PUMP (progressive cavity)**: lines 4"-LS-013; through reducer, butterfly valve, reducer
- **SLAKER TRANSFER PUMP (progressive cavity)** → **STORAGE-2** (Lime slurry STORAGE 2 (V=25,000 USGAL)): lines 4"-LS-005, 4"-LS-006; through reducer, butterfly valve, check valve
- **SLAKER TRANSFER PUMP (progressive cavity)** → **STORAGE-1** (Lime slurry STORAGE 1 (V=25,000 USGAL)): lines 4"-LS-005; through reducer, butterfly valve, check valve
- **STORAGE-2** (Lime slurry STORAGE 2 (V=25,000 USGAL)) → **REACTOR-2** (REACTOR 2 (V=20,000 USGAL)): lines 4"-LS-018
- **STORAGE-2** (Lime slurry STORAGE 2 (V=25,000 USGAL)) → **INJECTION PUMP 2 (progressive cavity)**: lines 4"-LS-010; through butterfly valve, butterfly valve
- **STORAGE-1** (Lime slurry STORAGE 1 (V=25,000 USGAL)) → **REACTOR-1** (REACTOR 1 (V=20,000 USGAL)): lines 4"-LS-017
- **STORAGE-1** (Lime slurry STORAGE 1 (V=25,000 USGAL)) → **INJECTION PUMP 1 (progressive cavity)**: lines 4"-LS-009; through butterfly valve, butterfly valve
- **STORAGE-1** (Lime slurry STORAGE 1 (V=25,000 USGAL)) → **PU-9** (STORAGE TRANSFER PUMP (progressive cavity)): lines 4"-LS-007; through butterfly valve, reducer
- **INJECTION PUMP 2 (progressive cavity)** → **REACTOR-2** (REACTOR 2 (V=20,000 USGAL)): lines 4"-LS-012; through reducer, sample point, sample point, sample point
- **REACTOR-1** (REACTOR 1 (V=20,000 USGAL)) → **MILL POND (EL 285.76 m)**: lines 14"-TW-001; crosses sheets
- **INJECTION PUMP 1 (progressive cavity)** → **REACTOR-1** (REACTOR 1 (V=20,000 USGAL)): lines 4"-LS-011; through reducer, check valve, Breather vent
- **PU-9** (STORAGE TRANSFER PUMP (progressive cavity)) → **STORAGE-2** (Lime slurry STORAGE 2 (V=25,000 USGAL)): lines 4"-LS-008; through reducer, check valve, butterfly valve
- **Lime SILO with vibratory bin discharger** → **Lime screw conveyor (silo to slaker)**
- **Lime screw conveyor (silo to slaker)** → **S-1** (PORTABLE SLAKER S-1 (V=23,200 USGAL)): through reducer
- **VENDOR SKID MOBILE PUMP STATION** → **ANNEX TANK**: lines 4"-RW-003, 4"-RW-005, 4"-RW-006, 1 1/2"-RW-008; through gate valve, butterfly valve, strainer, check valve, ball valve, flexible hose; crosses sheets
- **VENDOR SKID MOBILE PUMP STATION** → **S-1** (PORTABLE SLAKER S-1 (V=23,200 USGAL)): lines 4"-RW-003, 4"-RW-005, 4"-RW-006, 4"-RW-XXX; through gate valve, butterfly valve, strainer, check valve, butterfly valve; crosses sheets
- **VENDOR SKID MOBILE PUMP STATION** → **SLAKER TRANSFER PUMP (progressive cavity)**: lines 4"-RW-003, 4"-RW-005, 4"-RW-006, 4"-RW-007, 4"-LS-013; through gate valve, butterfly valve, strainer, check valve, reducer, ball valve, flexible hose, ball valve, reducer, butterfly valve, reducer; crosses sheets
- **ANNEX TANK** → **Annex booster pump (untagged)**: through reducer
- **Annex booster pump (untagged)** → **EXPANSION TANK**: through needle valve, reducer, check valve, gate valve, flexible hose
- **Annex booster pump (untagged)** → **ANNEX S.N.V.**: through needle valve, reducer, gate valve
- **RAW WATER POND** → **PU-4** (Raw water pump (100 GPM, 20 PSI)): lines 4"-RW-002; through check valve
- **RAW WATER POND** → **PU-3** (Raw water pump (100 GPM, 20 PSI), in sea can): lines 4"-RW-001; through check valve
- **PU-4** (Raw water pump (100 GPM, 20 PSI)) → **ANNEX TANK**: lines 4"-RW-005, 4"-RW-006, 1 1/2"-RW-008; through check valve, gate valve, butterfly valve, strainer, check valve, ball valve, flexible hose; crosses sheets
- **PU-4** (Raw water pump (100 GPM, 20 PSI)) → **S-1** (PORTABLE SLAKER S-1 (V=23,200 USGAL)): lines 4"-RW-005, 4"-RW-006, 4"-RW-XXX; through check valve, gate valve, butterfly valve, strainer, check valve, butterfly valve; crosses sheets
- **PU-4** (Raw water pump (100 GPM, 20 PSI)) → **SLAKER TRANSFER PUMP (progressive cavity)**: lines 4"-RW-005, 4"-RW-006, 4"-RW-007, 4"-LS-013; through check valve, gate valve, butterfly valve, strainer, check valve, reducer, ball valve, flexible hose, ball valve, reducer, butterfly valve, reducer; crosses sheets
- **PU-3** (Raw water pump (100 GPM, 20 PSI), in sea can) → **ANNEX TANK**: lines 4"-RW-006, 1 1/2"-RW-008; through check valve, butterfly valve, strainer, check valve, ball valve, flexible hose; crosses sheets
- **PU-3** (Raw water pump (100 GPM, 20 PSI), in sea can) → **S-1** (PORTABLE SLAKER S-1 (V=23,200 USGAL)): lines 4"-RW-006, 4"-RW-XXX; through check valve, butterfly valve, strainer, check valve, butterfly valve; crosses sheets
- **PU-3** (Raw water pump (100 GPM, 20 PSI), in sea can) → **SLAKER TRANSFER PUMP (progressive cavity)**: lines 4"-RW-006, 4"-RW-007, 4"-LS-013; through check valve, butterfly valve, strainer, check valve, reducer, ball valve, flexible hose, ball valve, reducer, butterfly valve, reducer; crosses sheets
- **PU-1** (Submersible pump with integral check valve) → **RUTTAN OPEN PIT (EL 280.0 max / 245.0 min MASL)**: lines 8"-CTW-010, 14"-CTW-004, 2"-CTW-006; through reducer, 8" TAP, gate valve, relief valve
- **PU-1** (Submersible pump with integral check valve) → **REACTOR-2** (REACTOR 2 (V=20,000 USGAL)): lines 8"-CTW-010, 14"-CTW-004, 10"-CTW-004; through reducer, 8" TAP, reducer, reducer, FE-2; crosses sheets
- **PU-14** (Submersible pump with integral check valve) → **RUTTAN OPEN PIT (EL 280.0 max / 245.0 min MASL)**: lines 8"-CTW-008, 14"-CTW-004, 2"-CTW-006; through reducer, 8" TAP, gate valve, relief valve
- **PU-14** (Submersible pump with integral check valve) → **REACTOR-2** (REACTOR 2 (V=20,000 USGAL)): lines 8"-CTW-008, 14"-CTW-004, 10"-CTW-004; through reducer, 8" TAP, reducer, reducer, FE-2; crosses sheets
- **PU-15** (Submersible pump with integral check valve) → **RUTTAN OPEN PIT (EL 280.0 max / 245.0 min MASL)**: lines 14"-CTW-003, 2"-CTW-005; through gate valve, relief valve
- **PU-15** (Submersible pump with integral check valve) → **REACTOR-1** (REACTOR 1 (V=20,000 USGAL)): lines 14"-CTW-003, 10"-CTW-003; through reducer, reducer, FE-1; crosses sheets
- **PU-2** (Submersible pump with integral check valve) → **RUTTAN OPEN PIT (EL 280.0 max / 245.0 min MASL)**: lines 8"-CTW-009, 14"-CTW-003, 2"-CTW-005; through reducer, 8" TAP, gate valve, relief valve
- **PU-2** (Submersible pump with integral check valve) → **REACTOR-1** (REACTOR 1 (V=20,000 USGAL)): lines 8"-CTW-009, 14"-CTW-003, 10"-CTW-003; through reducer, 8" TAP, reducer, reducer, FE-1; crosses sheets

Drains, vents and overflows (not process flow):
- Raw water spare/drain connection ← PU-3, PU-4, VENDOR SKID MOBILE PUMP STATION
- VENT TO OUTDOORS (slaker) ← S-1

## Equipment

| Tag | Kind | Description | Fed by | Feeds | Status | Sheets |
|---|---|---|---|---|---|---|
| AG-1 | agitator | AGITATOR AG-1 (Storage 1) |  |  |  | M701 |
| AG-2 | agitator | AGITATOR AG-2 (Storage 2) |  |  |  | M701 |
| ANNEX S.N.V. | other | ANNEX S.N.V. | Annex booster pump (untagged) |  |  | M701 |
| ANNEX TANK | tank | ANNEX TANK | PU-3, PU-4, VENDOR SKID MOBILE PUMP STATION | Annex booster pump (untagged) |  | M701 |
| Annex booster pump (untagged) | centrifugal_pump | Annex booster pump (untagged) | ANNEX TANK | ANNEX S.N.V., EXPANSION TANK |  | M701 |
| BREHAUT LAKE (FUTURE) | pond | BREHAUT LAKE (FUTURE) | MILL POND (EL 285.76 m) |  | future | M702 |
| EXPANSION TANK | vessel | EXPANSION TANK | Annex booster pump (untagged) |  |  | M701 |
| INJECTION PUMP 1 (progressive cavity) | positive_displacement_pump | INJECTION PUMP 1 (progressive cavity) | STORAGE-1 | REACTOR-1 |  | M701 |
| INJECTION PUMP 2 (progressive cavity) | positive_displacement_pump | INJECTION PUMP 2 (progressive cavity) | STORAGE-2 | REACTOR-2 |  | M701 |
| LIME TRUCK (pneumatic unloading) | other | LIME TRUCK (pneumatic unloading) |  | S-1 |  | M701 |
| Lime SILO with vibratory bin discharger | silo | Lime SILO with vibratory bin discharger |  | Lime screw conveyor (silo to slaker) |  | M701 |
| Lime screw conveyor (silo to slaker) | conveyor | Lime screw conveyor (silo to slaker) | Lime SILO with vibratory bin discharger | S-1 |  | M701 |
| MILL POND (EL 285.76 m) | pond | MILL POND (EL 285.76 m) | REACTOR-1, REACTOR-2 | BREHAUT LAKE (FUTURE), RUTTAN LAKE |  | M702 |
| PU-1 | sump_pump | Submersible pump with integral check valve |  | REACTOR-2, RUTTAN OPEN PIT (EL 280.0 max / 245.0 min MASL) |  | M702 |
| PU-14 | sump_pump | Submersible pump with integral check valve |  | REACTOR-2, RUTTAN OPEN PIT (EL 280.0 max / 245.0 min MASL) |  | M702 |
| PU-15 | sump_pump | Submersible pump with integral check valve |  | REACTOR-1, RUTTAN OPEN PIT (EL 280.0 max / 245.0 min MASL) |  | M702 |
| PU-2 | sump_pump | Submersible pump with integral check valve |  | REACTOR-1, RUTTAN OPEN PIT (EL 280.0 max / 245.0 min MASL) |  | M702 |
| PU-3 | centrifugal_pump | Raw water pump (100 GPM, 20 PSI), in sea can | RAW WATER POND | ANNEX TANK, Raw water spare/drain connection, S-1, SLAKER TRANSFER PUMP (progressive cavity) |  | M702 |
| PU-4 | centrifugal_pump | Raw water pump (100 GPM, 20 PSI) | RAW WATER POND | ANNEX TANK, Raw water spare/drain connection, S-1, SLAKER TRANSFER PUMP (progressive cavity) |  | M702 |
| PU-9 | positive_displacement_pump | STORAGE TRANSFER PUMP (progressive cavity) | STORAGE-1 | STORAGE-2 |  | M701 |
| R1-1 | agitator | Reactor 1 agitator 1 |  |  |  | M701 |
| R1-2 | agitator | Reactor 1 agitator 2 |  |  |  | M701 |
| R1-3 | agitator | Reactor 1 agitator 3 |  |  |  | M701 |
| R1-4 | agitator | Reactor 1 agitator 4 |  |  |  | M701 |
| R2-1 | agitator | Reactor 2 agitator 1 |  |  |  | M701 |
| R2-2 | agitator | Reactor 2 agitator 2 |  |  |  | M701 |
| R2-3 | agitator | Reactor 2 agitator 3 |  |  |  | M701 |
| R2-4 | agitator | Reactor 2 agitator 4 |  |  |  | M701 |
| RAW WATER POND | pond | RAW WATER POND |  | PU-3, PU-4 |  | M702 |
| REACTOR-1 | agitated_tank | REACTOR 1 (V=20,000 USGAL) | INJECTION PUMP 1 (progressive cavity), PU-15, PU-2, STORAGE-1 | MILL POND (EL 285.76 m) |  | M701 |
| REACTOR-2 | agitated_tank | REACTOR 2 (V=20,000 USGAL) | INJECTION PUMP 2 (progressive cavity), Lower header spare 8" blind end, PU-1, PU-14, STORAGE-2 | MILL POND (EL 285.76 m) |  | M701 |
| RUTTAN LAKE | pond | RUTTAN LAKE | MILL POND (EL 285.76 m) |  |  | M702 |
| RUTTAN OPEN PIT (EL 280.0 max / 245.0 min MASL) | pond | RUTTAN OPEN PIT (EL 280.0 max / 245.0 min MASL) | Lower header spare 8" blind end, PU-1, PU-14, PU-15, PU-2 |  |  | M702 |
| S-1 | mixer | PORTABLE SLAKER S-1 (V=23,200 USGAL) | LIME TRUCK (pneumatic unloading), Lime screw conveyor (silo to slaker), PU-3, PU-4, VENDOR SKID MOBILE PUMP STATION | SLAKER TRANSFER PUMP (progressive cavity), VENT TO OUTDOORS (slaker) |  | M701 |
| SLAKER TRANSFER PUMP (progressive cavity) | positive_displacement_pump | SLAKER TRANSFER PUMP (progressive cavity) | PU-3, PU-4, S-1, VENDOR SKID MOBILE PUMP STATION | STORAGE-1, STORAGE-2 |  | M701 |
| STORAGE-1 | agitated_tank | Lime slurry STORAGE 1 (V=25,000 USGAL) | SLAKER TRANSFER PUMP (progressive cavity) | INJECTION PUMP 1 (progressive cavity), PU-9, REACTOR-1 |  | M701 |
| STORAGE-2 | agitated_tank | Lime slurry STORAGE 2 (V=25,000 USGAL) | PU-9, SLAKER TRANSFER PUMP (progressive cavity) | INJECTION PUMP 2 (progressive cavity), REACTOR-2 |  | M701 |
| VENDOR SKID MOBILE PUMP STATION | package_unit | VENDOR SKID MOBILE PUMP STATION |  | ANNEX TANK, Raw water spare/drain connection, S-1, SLAKER TRANSFER PUMP (progressive cavity) |  | M702 |

## Instruments

Location is where the instrument senses the process. Pipe locations read `line (upstream item -> downstream item)`.

| Tag | Variable | Function | Mounted | Senses | Loop |
|---|---|---|---|---|---|
| AE-12 | analysis | element | field | REACTOR-1 |  |
| AE-22 | analysis | element | field | REACTOR-2 |  |
| FE-1 | flow | element | field | in-line on 10"-CTW-003 (reducer -> REACTOR-1) | F-1 |
| FE-2 | flow | element | field | in-line on 10"-CTW-004 (reducer -> REACTOR-2) | F-2 |
| FIT-1 | flow | transmitter | main_panel | in-line on 10"-CTW-003 (reducer -> REACTOR-1) | F-1 |
| FIT-2 | flow | transmitter | main_panel | in-line on 10"-CTW-004 (reducer -> REACTOR-2) | F-2 |
| HS-14A | hand | hand_switch | field |  | S-14 |
| HS-14B | hand | hand_switch | main_panel |  | S-14 |
| HS-15A | hand | hand_switch | field |  | S-15 |
| HS-15B | hand | hand_switch | main_panel |  | S-15 |
| HS-1A | hand | hand_switch | field |  | S-1 |
| HS-1B | hand | hand_switch | main_panel |  | S-1 |
| HS-2A | hand | hand_switch | field |  | S-2 |
| HS-2B | hand | hand_switch | main_panel |  | S-2 |
| HS-5 | hand | hand_switch | field |  | H-5 |
| HS-9 | hand | hand_switch | field |  | H-9 |
| HS-A1 | hand | hand_switch | field |  | H-A1 |
| HS-A2 | hand | hand_switch | field |  | H-A2 |
| HS-A5 | hand | hand_switch | field |  | H-A5 |
| HS-C1 | hand | hand_switch | field |  | H-C1 |
| HS-P3 | hand | hand_switch | field |  | H-P3 |
| HS-P4 | hand | hand_switch | field |  | H-P4 |
| HS-R11 | hand | hand_switch | field |  | H-R11 |
| HS-R12 | hand | hand_switch | field |  | H-R12 |
| HS-R13 | hand | hand_switch | field |  | H-R13 |
| HS-R14 | hand | hand_switch | field |  | H-R14 |
| HS-R21 | hand | hand_switch | field |  | H-R21 |
| HS-R22 | hand | hand_switch | field |  | H-R22 |
| HS-R23 | hand | hand_switch | field |  | H-R23 |
| HS-R24 | hand | hand_switch | field |  | H-R24 |
| HS-S1 | hand | hand_switch | field |  | H-S1 |
| HS-S2 | hand | hand_switch | field |  | H-S2 |
| HS-S2#2 | hand | hand_switch | field |  | H-S2#2 |
| HS-V1 | hand | hand_switch | field |  | H-V1 |
| LT-1 | level | transmitter | field | STORAGE-1 |  |
| LT-2 | level | transmitter | field | STORAGE-2 |  |
| PI (untagged) | pressure | indicator | field | 2"-CTW-005 (PU-15 -> gate valve) |  |
| PI-A1 | pressure | indicator | field | line (reducer -> gate valve) |  |
| PI-A2 | pressure | indicator | field | line (reducer -> gate valve) |  |
| SC-1 | speed/frequency | controller | local_panel |  | S-1 |
| SC-14 | speed/frequency | controller | local_panel |  | S-14 |
| SC-15 | speed/frequency | controller | local_panel |  | S-15 |
| SC-2 | speed/frequency | controller | local_panel |  | S-2 |
| SK-1 | speed/frequency | controller | main_panel |  | S-1 |
| SK-14 | speed/frequency | controller | main_panel |  | S-14 |
| SK-15 | speed/frequency | controller | main_panel |  | S-15 |
| SK-2 | speed/frequency | controller | main_panel |  | S-2 |
| XC-14A | unclassified | controller | local_panel |  | S-14 |
| XC-14B | unclassified | controller | main_panel |  | S-14 |
| XC-15A | unclassified | controller | local_panel |  | S-15 |
| XC-15B | unclassified | controller | main_panel |  | S-15 |
| XC-1A | unclassified | controller | local_panel |  | S-1 |
| XC-1B | unclassified | controller | main_panel |  | S-1 |
| XC-2A | unclassified | controller | local_panel |  | S-2 |
| XC-2B | unclassified | controller | main_panel |  | S-2 |
| YAX-14A | event/state | alarm | main_panel |  | S-14 |
| YAX-15A | event/state | alarm | main_panel |  | S-15 |
| YAX-1A | event/state | alarm | main_panel |  | S-1 |
| YAX-2A | event/state | alarm | main_panel |  | S-2 |
| YI-14B | event/state | indicator | main_panel |  | S-14 |
| YI-15B | event/state | indicator | main_panel |  | S-15 |
| YI-1B | event/state | indicator | main_panel |  | S-1 |
| YI-2B | event/state | indicator | main_panel |  | S-2 |
| YSX-14A | event/state | switch | local_panel |  | S-14 |
| YSX-14B | event/state | switch | local_panel |  | S-14 |
| YSX-15A | event/state | switch | local_panel |  | S-15 |
| YSX-15B | event/state | switch | local_panel |  | S-15 |
| YSX-1A | event/state | switch | local_panel |  | S-1 |
| YSX-1B | event/state | switch | local_panel |  | S-1 |
| YSX-2A | event/state | switch | local_panel |  | S-2 |
| YSX-2B | event/state | switch | local_panel |  | S-2 |

## Control loops

| Loop | Type | Sensor(s) | Controller(s) | Final element(s) | Description |
|---|---|---|---|---|---|
| F-1 | monitoring | FE-1, FIT-1 |  |  | Monitoring loop F-1 (flow). Sensed by FE-1, FIT-1 (in-line on 10"-CTW-003 (reducer -> REACTOR-1)). |
| F-2 | monitoring | FE-2, FIT-2 |  |  | Monitoring loop F-2 (flow). Sensed by FE-2, FIT-2 (in-line on 10"-CTW-004 (reducer -> REACTOR-2)). |
| H-5 | manual |  |  | S-1 | Manual loop H-5 (hand). Acts on S-1. |
| H-9 | manual |  |  | PU-9 | Manual loop H-9 (hand). Acts on PU-9. |
| H-A1 | manual |  |  | AG-1 | Manual loop H-A1 (hand). Acts on AG-1. |
| H-A2 | manual |  |  | AG-2 | Manual loop H-A2 (hand). Acts on AG-2. |
| H-A5 | manual |  |  | Annex booster pump (untagged) | Manual loop H-A5 (hand). Acts on Annex booster pump (untagged). |
| H-C1 | manual |  |  | Lime screw conveyor (silo to slaker) | Manual loop H-C1 (hand). Acts on Lime screw conveyor (silo to slaker). |
| H-P3 | manual |  |  | PU-3 | Manual loop H-P3 (hand). Acts on PU-3. |
| H-P4 | manual |  |  | PU-4 | Manual loop H-P4 (hand). Acts on PU-4. |
| H-R11 | manual |  |  | R1-1 | Manual loop H-R11 (hand). Acts on R1-1. |
| H-R12 | manual |  |  | R1-2 | Manual loop H-R12 (hand). Acts on R1-2. |
| H-R13 | manual |  |  | R1-3 | Manual loop H-R13 (hand). Acts on R1-3. |
| H-R14 | manual |  |  | R1-4 | Manual loop H-R14 (hand). Acts on R1-4. |
| H-R21 | manual |  |  | R2-1 | Manual loop H-R21 (hand). Acts on R2-1. |
| H-R22 | manual |  |  | R2-2 | Manual loop H-R22 (hand). Acts on R2-2. |
| H-R23 | manual |  |  | R2-3 | Manual loop H-R23 (hand). Acts on R2-3. |
| H-R24 | manual |  |  | R2-4 | Manual loop H-R24 (hand). Acts on R2-4. |
| H-S1 | manual |  |  | INJECTION PUMP 1 (progressive cavity) | Manual loop H-S1 (hand). Acts on INJECTION PUMP 1 (progressive cavity). |
| H-S2 | manual |  |  | INJECTION PUMP 2 (progressive cavity) | Manual loop H-S2 (hand). Acts on INJECTION PUMP 2 (progressive cavity). |
| H-S2#2 | manual |  |  | SLAKER TRANSFER PUMP (progressive cavity) | Manual loop H-S2#2 (hand). Acts on SLAKER TRANSFER PUMP (progressive cavity). |
| H-V1 | manual |  |  | Lime SILO with vibratory bin discharger | Manual loop H-V1 (hand). Acts on Lime SILO with vibratory bin discharger. |
| S-1 | control | YSX-1A, YSX-1B | SK-1, SC-1, XC-1A, XC-1B | PU-1 | Control loop S-1 (speed/frequency). Sensed by YSX-1A, YSX-1B. Controlled by SK-1, SC-1, XC-1A, XC-1B (local_panel, main_panel). Acts on PU-1. |
| S-14 | control | YSX-14A, YSX-14B | SK-14, SC-14, XC-14A, XC-14B | PU-14 | Control loop S-14 (speed/frequency). Sensed by YSX-14A, YSX-14B. Controlled by SK-14, SC-14, XC-14A, XC-14B (local_panel, main_panel). Acts on PU-14. |
| S-15 | control | YSX-15A, YSX-15B | SK-15, SC-15, XC-15A, XC-15B | PU-15 | Control loop S-15 (speed/frequency). Sensed by YSX-15A, YSX-15B. Controlled by SK-15, SC-15, XC-15A, XC-15B (local_panel, main_panel). Acts on PU-15. |
| S-2 | control | YSX-2A, YSX-2B | SK-2, SC-2, XC-2A, XC-2B | PU-2 | Control loop S-2 (speed/frequency). Sensed by YSX-2A, YSX-2B. Controlled by SK-2, SC-2, XC-2A, XC-2B (local_panel, main_panel). Acts on PU-2. |

## Off-page connections

| Sheet | Connector | Direction | Other drawing | Linked to |
|---|---|---|---|---|
| M701 | CONTAMINATED WATER M702 FROM OPEN PIT SUBMERSIBLE PUMPS | in | M702 | CONTAMINATED WATER M701 (M702) |
| M701 | CONTAMINATED WATER M702 FROM OPEN PIT SUBMERSIBLE PUMPS | in | M702 | CONTAMINATED WATER M701 (M702) |
| M701 | RAW WATER M702 | in | M702 | RAW WATER M701 (M702) |
| M701 | TREATED WATER M702 | out | M702 | TREATED WATER M701 (M702) |
| M701 | TREATED WATER M702 | out | M702 | TREATED WATER M701 (M702) |
| M702 | CONTAMINATED WATER M701 | out | M701 | CONTAMINATED WATER M702 FROM OPEN PIT SUBMERSIBLE PUMPS (M701) |
| M702 | CONTAMINATED WATER M701 | out | M701 | CONTAMINATED WATER M702 FROM OPEN PIT SUBMERSIBLE PUMPS (M701) |
| M702 | RAW WATER M701 | out | M701 | RAW WATER M702 (M701) |
| M702 | TREATED WATER M701 | in | M701 | TREATED WATER M702 (M701) |
| M702 | TREATED WATER M701 | in | M701 | TREATED WATER M702 (M701) |

## Data quality

0 errors, 2 warnings and 1 informational items; see `qa_report.md`. Every node carries `confidence` and the sheet region it was read from (`provenance`). This graph was machine-extracted from drawings and must be verified by a qualified engineer before use in design, operations or safety work.
