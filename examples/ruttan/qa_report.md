# QA report: ruttan

Generated 2026-10-25T21:05:58+00:00 by pid-to-kg 0.1.0.

**0 errors, 2 warnings, 1 info.**

Errors must be fixed in the page extraction files before the graph is trusted. Warnings are things to re-check on the drawing (the *Re-check* column names the tiles). Info items are for the record.

| Severity | Code | Count |
|---|---|---|
| warning | `duplicate_tag` | 1 |
| warning | `possible_missed_tags` | 1 |
| info | `inferred_flow_direction` | 1 |

## Details

| Severity | Page | Code | Item | Message | Re-check |
|---|---|---|---|---|---|
| warning | 1 | `duplicate_tag` | HS-S2#2 | tag 'HS-S2' is used by more than one item on this sheet; the copy 'HS-S2B' was kept separate as 'HS-S2#2' | r2c3 |
| warning | 1 | `possible_missed_tags` |  | 1 tags found by ocr are not in the graph: D-4SS |  |
| info |  | `inferred_flow_direction` |  | 2 flow edges have inferred (not drawn) direction |  |
