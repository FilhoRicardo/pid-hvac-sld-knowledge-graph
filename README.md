# pid-to-kg

**Turn P&ID drawings into a process knowledge graph that an LLM can reason over.**

`pid-to-kg` is a [Claude skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) that reads piping and instrumentation diagrams (P&IDs) and PFDs from PDF and builds a knowledge graph of the process. The PDFs can be vector exports or scanned images. The graph captures:

- **Process flow:** what is upstream and downstream of every tank, pump, valve and pipe segment.
- **Measurement:** which instrument measures which variable, and exactly where it sits in the flow.
- **Control:** control loops from sensor through controller to final element, including I/P relays, cascades, interlocks and VFD drives.

The output is meant to be one layer of a chemical-manufacturing **context layer**. An LLM application can query it to answer questions such as "what feeds this clarifier?", "which transmitters sit downstream of P-101?" or "what does FIC-0502 manipulate?" from the drawings themselves.

```
P&ID PDF ──► probe ──► render + tile ──► hints (text layer / OCR)
 (vector or scanned)                         │
                         Claude reads each sheet visually ──► extract/page_NN.json
                                                                   │
                       build: merge sheets · expand pipes · pair off-page links
                              · locate instruments · infer loops · QA
                                                                   │
            graph.json  ·  graph.duckdb  ·  summary.md  ·  qa_report.md
```

## Why it is built this way

| Decision | Reason |
|---|---|
| **Claude's vision reads the drawings; Python does everything else.** | Symbol recognition and line tracing on real drawings (rotated sheets, outlined text, low-resolution scans, greyed-out existing plant) is visual reasoning. Classification, rendering, merging, loop inference, QA and storage are deterministic, testable code. |
| **Vector and scanned PDFs take different routes.** | The probe sorts each page into one of six classes. *Vector drawings with outlined text* have no text layer at all, which is common in CAD exports, so a pure text-extraction approach returns nothing on them. |
| **Resolution adapts to the drawing.** | OCR measures the text size and the page is rendered so that small text is legible in every tile. Orientation is detected automatically. |
| **JSON is the canonical format, DuckDB the query layer.** | JSON is diffable, schema-validated and readable by any tool or LLM. DuckDB is a single embedded file that answers SQL questions, including recursive upstream/downstream macros, with no server. That suits graphs of hundreds to tens of thousands of nodes. For larger estates, `export.py` writes a Neo4j import bundle or GraphML. YAML was not used: it adds parsing pitfalls and nothing else. |
| **Pipes are nodes.** | A line is split into segments between its valves and in-line items, so an instrument tap has an exact location. "Where is PT-101?" then has a precise answer. |
| **Standards-aligned.** | Instruments are parsed per **ISA-5.1** (variable, functions, loop). Nodes carry the closest **DEXPI** class for interoperability. |
| **Everything has provenance and confidence.** | Every node records the sheet and region it came from. QA lists what to re-check, and on which tile. |

## Quick start

**1. Install the skill.** The repo is a Claude Code plugin. Either add it as a plugin, or copy `skills/pid-to-kg/` into `~/.claude/skills/` (personal) or `.claude/skills/` (project). Then install the Python dependencies:

```bash
pip install -r skills/pid-to-kg/scripts/requirements.txt   # Python 3.10+
```

**2. Ask Claude.**

> Build a knowledge graph from `drawings/plant-a-pids.pdf`.

Claude then runs the workflow in [`SKILL.md`](skills/pid-to-kg/SKILL.md) and reports the outputs and any open issues:

1. probe the PDF
2. render the pages
3. read each sheet
4. build the graph
5. work through the QA report

**3. Use the graph.**

```bash
python skills/pid-to-kg/scripts/kg_query.py work/plant-a/kg downstream 660-TK-001 --equipment
python skills/pid-to-kg/scripts/kg_query.py work/plant-a/kg instruments --on 660-PP-011
python skills/pid-to-kg/scripts/kg_query.py work/plant-a/kg loop FIC-0502
python skills/pid-to-kg/scripts/kg_query.py work/plant-a/kg sql "SELECT * FROM equipment_flow"
```

Or put `summary.md` straight into an LLM's context. It is the compact, token-efficient view of the plant.

## Outputs

| File | What it is |
|---|---|
| `graph.json` | Canonical graph (schema: [`graph.schema.json`](skills/pid-to-kg/references/schema/graph.schema.json)) |
| `graph.duckdb` | Tables `nodes`, `edges`, `issues`; views `equipment`, `equipment_flow`, `instruments`, `loops`, `signals`; macros `upstream(id)`, `downstream(id)` |
| `summary.md` | Equipment-level flow, equipment table, instrument table with locations, loop table, off-page links |
| `qa_report.md` | Errors, warnings and info, each with the tiles to re-check |

The ontology is described in [`references/ontology.md`](skills/pid-to-kg/references/ontology.md):

- **Node types:** Plant, Sheet, Equipment, PipeSegment, Component, Instrument, ControlLoop, OffPageConnector, Boundary.
- **Edge types:** `FLOWS_TO`, `FEEDS`, `MEASURES`, `SIGNAL_TO`, `ACTUATES`, `MEMBER_OF`, `CASCADES_TO`, `TRIPS`, `PART_OF`.

## Tested on real drawings

The skill was developed against three unrelated facilities. It covers both PDF routes, and each plant is a separate graph. Details and per-plant notes are in [`examples/`](examples/README.md).

| Plant | PDF type | Sheets | Equipment | Instruments | Loops | Build errors |
|---|---|---|---|---|---|---|
| Gold mine water treatment | vector, text outlined | 14 | 70 | 70 | 26 | 0 |
| Mine remediation lime plant | vector, text outlined | 2 (as-built) | 38 | 71 | 26 | 0 |
| Municipal wastewater plant | scanned, ~190 dpi | 10 | 87 | 452 | 164 | 0 |

What a downstream LLM can now answer from the wastewater graph, with no drawings in context:

```text
$ kg_query.py virden/kg path TK-2300 UV-3200
TK-2300 → RWP-2310 → SB-2500 → SBR-2600 → TK-3110 → UV-3200    (across 4 sheets)

$ kg_query.py virden/kg instruments --on RWP-2310
PE-2310 / PI-2310   pressure   200-PPE-E1 (Diaphragm seal -> CHV-2310)   loop P-2310

$ kg_query.py virden/kg loop SC-3820
Control loop S-3820 (speed/frequency). Controlled by SC-3820 (plc). Acts on PSWP-3820; PSWP-3810.
```

Testing also changed the skill. The probe found that two of the three "vector" PDFs have **no text layer at all**: every label is drawn as outlines. That led to the `vector_outlined` route, rendering resolution set from the measured text size, and OCR orientation detection, since every sheet was rotated.

The QA loop then surfaced real-world drawing problems the builder now handles and reports:
- the same tag printed on two different items
- tags reused across sheets
- off-page flags pointing at the wrong drawing
- an as-built and a draft revision of the same plant in one PDF



## Repository layout

```
skills/pid-to-kg/
  SKILL.md                    workflow Claude follows
  references/                 extraction procedure, ISA-5.1 guide, symbol guide, ontology, JSON schemas
  scripts/                    probe, render, hints, build, query, export, eval, crop
  scripts/pidkg/              library: models, ISA parsing, builder, loops, QA, storage, summary
tests/                        pytest suite with a synthetic two-sheet plant and synthetic PDFs
examples/                     graphs, extractions and gold spot-check files for the three test plants (source PDFs not redistributed)
```

## Development

```bash
pip install -e ".[dev]"
pytest
python skills/pid-to-kg/scripts/build_kg.py --write-schemas   # after changing pidkg/models.py
```

## Limitations

- **Extraction quality depends on legibility.** Low-resolution scans lose small text. Unreadable items are recorded as such, never guessed.
- **Loops come from ISA tag numbers and drawn signal lines.** Logic that lives only in control narratives or cause-and-effect charts is not on the P&ID and is not captured.
- **Line direction is taken from arrows and equipment logic.** Edges whose direction had to be inferred are marked `flow_direction: inferred`.
- **The DEXPI mapping is informative.** It is not a certified DEXPI export.

## Disclaimer

The graph is machine-extracted from drawings. It must be reviewed by a qualified engineer before it is used for design, operations, management of change, or safety studies such as HAZOP or LOPA.

## License

MIT. See [LICENSE](LICENSE).
