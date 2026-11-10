"""HVAC vocabulary and Brick mapping (Phase 1) without changing P&ID DEXPI behaviour."""

from __future__ import annotations

import pytest

from pidkg.ontology import (
    BRICK_EDGE_RELATIONSHIPS,
    EQUIPMENT_BRICK,
    EQUIPMENT_DEXPI,
    EQUIPMENT_KINDS,
    HVAC_EQUIPMENT_KINDS,
)

# Frozen snapshot: P&ID DEXPI mapping must not change in this ticket.
EQUIPMENT_DEXPI_SNAPSHOT = {
    "tank": "Tank",
    "vessel": "Vessel",
    "pressure_vessel": "PressureVessel",
    "pump": "Pump",
    "centrifugal_pump": "CentrifugalPump",
    "positive_displacement_pump": "ReciprocatingPump",
    "metering_pump": "ReciprocatingPump",
    "slurry_pump": "CentrifugalPump",
    "sump_pump": "CentrifugalPump",
    "compressor": "Compressor",
    "blower": "Blower",
    "fan": "Fan",
    "heat_exchanger": "HeatExchanger",
    "cooler": "HeatExchanger",
    "heater": "HeatExchanger",
    "boiler": "Boiler",
    "furnace": "Furnace",
    "column": "Column",
    "reactor": "Vessel",
    "agitated_tank": "Tank",
    "agitator": "Agitator",
    "mixer": "Mixer",
    "static_mixer": "StaticMixer",
    "filter": "Filter",
    "filter_press": "Filter",
    "membrane_filter": "Filter",
    "strainer_unit": "Filter",
    "screen": "Sieve",
    "cyclone": "CycloneSeparator",
    "hydrocyclone": "CycloneSeparator",
    "separator": "Separator",
    "clarifier": "Separator",
    "thickener": "Separator",
    "flotation_cell": "Separator",
    "centrifuge": "Centrifuge",
    "dryer": "Dryer",
    "mill": "Mill",
    "crusher": "Crusher",
    "conveyor": "Conveyor",
    "feeder": "Feeder",
    "hopper": "Silo",
    "bin": "Silo",
    "silo": "Silo",
    "sump": "Tank",
    "pond": "Tank",
    "box": "Tank",
    "electrowinning_cell": "Vessel",
    "kiln": "Furnace",
    "scrubber": "Column",
    "ion_exchange": "Column",
    "uv_unit": "Equipment",
    "sampler": "Equipment",
    "package_unit": "Equipment",
    "motor": "ElectricMotor",
    "other": "Equipment",
}

REQUIRED_HVAC_KINDS = (
    "ahu",
    "fcu",
    "vav",
    "cav",
    "cooling_coil",
    "heating_coil",
    "damper",
    "fire_damper",
    "chiller",
    "cooling_tower",
    "heat_pump",
    "diffuser",
    "grille",
)


def test_equipment_dexpi_unchanged():
    assert EQUIPMENT_DEXPI == EQUIPMENT_DEXPI_SNAPSHOT
    assert EQUIPMENT_KINDS[: len(EQUIPMENT_DEXPI)] == tuple(EQUIPMENT_DEXPI)


@pytest.mark.parametrize("kind", REQUIRED_HVAC_KINDS)
def test_hvac_kinds_in_equipment_kinds(kind):
    assert kind in EQUIPMENT_KINDS
    assert kind in HVAC_EQUIPMENT_KINDS


def test_equipment_kinds_is_pid_plus_hvac_union():
    pid_set = set(EQUIPMENT_DEXPI)
    hvac_set = set(HVAC_EQUIPMENT_KINDS)
    assert pid_set.isdisjoint(hvac_set)
    assert set(EQUIPMENT_KINDS) == pid_set | hvac_set


def test_brick_edge_relationship_map():
    assert BRICK_EDGE_RELATIONSHIPS["FEEDS"].brick == "feeds"
    assert BRICK_EDGE_RELATIONSHIPS["MEASURES"].brick == "hasPoint"
    assert BRICK_EDGE_RELATIONSHIPS["ACTUATES"].brick == "hasPoint"
    assert BRICK_EDGE_RELATIONSHIPS["PART_OF"].brick == "hasPart"
    assert BRICK_EDGE_RELATIONSHIPS["MEASURES"].invert_for_brick is True
    assert BRICK_EDGE_RELATIONSHIPS["ACTUATES"].invert_for_brick is True
    assert BRICK_EDGE_RELATIONSHIPS["FEEDS"].invert_for_brick is False


@pytest.mark.parametrize(
    "kind,brick_class",
    [
        ("ahu", "AHU"),
        ("fcu", "FCU"),
        ("vav", "VAV"),
        ("chiller", "Chiller"),
        ("cooling_tower", "Cooling_Tower"),
        ("damper", "Damper"),
    ],
)
def test_hvac_equipment_brick_classes(kind, brick_class):
    assert EQUIPMENT_BRICK.get(kind) == brick_class


def test_unknown_kind_dexpi_default_unchanged():
    assert EQUIPMENT_DEXPI.get("ahu", "Equipment") == "Equipment"
    assert EQUIPMENT_DEXPI.get("not_a_real_kind_xyz", "Equipment") == "Equipment"
