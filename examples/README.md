# Example graphs

These are three graphs built with `pid-to-kg` from P&IDs in public technical documents for three unrelated facilities. Each plant is a separate graph with no shared ids.

The source PDFs are **not** redistributed here. Each folder contains:

- `graph.json`: the knowledge graph
- `summary.md`: the LLM-ready summary
- `qa_report.md`: the final QA state
- `extract/page_NN.json`: the per-sheet extractions Claude wrote, useful as examples of the extraction schema

`graph.duckdb` is not committed. To regenerate it: `python skills/pid-to-kg/scripts/build_kg.py <work dir>`, or load `graph.json` directly.

| Plant | PDF type | Sheets | Equipment | Instruments | Valves & fittings | Pipe segments | Loops | Build errors |
|---|---|---|---|---|---|---|---|---|
| [Haile](haile/summary.md): gold mine water treatment plant | vector, text outlined (no text layer) | 14 (1 PFD + 13 P&IDs) | 70 | 70 | 222 | 460 | 26 | 0 |
| [Ruttan](ruttan/summary.md): mine-site remediation lime treatment plant | vector, text outlined | 2 (as-built) | 38 | 71 | 67 | 115 | 26 | 0 |
| [Virden](virden/summary.md): municipal wastewater treatment plant | scanned raster, ~190 dpi | 10 | 87 | 452 | 342 | 574 | 164 | 0 |

## Notes per plant

**Haile** (14 sheets: PFD G-200 and P&IDs 660-PI-200 to 212). QA keeps these warnings:
- Off-page flags that point to drawings not in the set (contact water, the lime feed loop, the cyanide thickener, and similar).
- Two flags whose drawing reference disagrees with the line number. The pairing follows the line number, and the mismatch is flagged.
- `660-TK-008` is called a "sludge transfer box" on the PFD and the "lime reaction tank" on the P&ID.
- `660-TK-06` and `660-TK-006` are the same tank with inconsistent tags.
- Duplex pumps whose two gauges or flowmeters carry the same printed tag.

These are drawing inconsistencies, reported rather than silently "fixed".

**Ruttan**: the PDF holds both the 2023 as-built sheets (M701/M702) and the 2014 draft tender sheets (M772/M773) for the same plant. The graph uses the as-built sheets only. The draft pages are recorded as excluded in the work manifest.

**Virden** (D-007 to D-016): headworks, septage receiving, grit removal, plant lift station, SBRs and equalization, UV and plant service water, blowers, digesters, dewatering and alum.
- All 36 off-page connectors pair across the ten sheets.
- Greyed equipment is recorded as `status: existing`.
- PLC/SCADA I/O bands are captured as instruments with `location: plc`.
- Many vendor-panel pilot lights and selector switches are listed in `unreadable` rather than modelled one by one.

## Accuracy spot check

One sheet per plant was hand-checked into a gold file (`gold/`) and scored with `eval_kg.py`. The scorer checks:
- tag precision and recall
- equipment-level flow precision and recall
- instrument placement accuracy
- loop recall

The first scoring pass found three kinds of problem.

| Problem | Example | Fixed in |
|---|---|---|
| Extraction error | Virden D-010: an index slip put all three pump-discharge pressure elements on pump 3's line | the page extraction |
| Builder gap | Ruttan FIT-1/FIT-2, drawn with a panel bubble, did not inherit their flow element's location | `pidkg/build.py`, which applies to every plant |
| Gold error | The graph found real cross-sheet flows the annotator had missed, such as digester supernatant and dewatering filtrate to the lift-station wet wells, the grit bypass, and the wet-well overflow to the Parshall flume | the gold file, after each flow was checked on the drawings |

After these fixes, all three sheets score 1.00 on tags, flow, instrument placement and loops.

**Read these numbers as a consistency check, not a benchmark.** The gold sets were made by the same annotator who ran the extraction, and part of their correction was prompted by the graph. Independent annotations are welcome as contributions.
