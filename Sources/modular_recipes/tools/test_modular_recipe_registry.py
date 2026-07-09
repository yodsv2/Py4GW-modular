"""Offline registry checks for Python modular recipes."""

from __future__ import annotations

import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
    from Sources.modular_recipes.tools import _stubs
else:
    from . import _stubs


def main() -> int:
    _stubs.install()
    from Sources.modular_recipes.catalog import all_specs
    from Sources.modular_recipes.catalog import get_recipe_factory
    from Sources.modular_recipes.catalog import get_recipe_module
    from Sources.modular_recipes.catalog import get_spec
    from Sources.modular_recipes.catalog import recipe_route_points
    from Sources.modular_recipes.prebuilt.modular_prophecies import PROPHECIES_PHASE_SPECS
    from Sources.modular_recipes.prebuilt.modular_prophecies import build_prophecies_campaign_specs
    from Sources.modular_recipes.prebuilt.modular_prophecies import derive_prophecies_region_spans

    specs = all_specs()
    assert specs
    assert len({(spec.kind, spec.key) for spec in specs}) == len(specs)
    welcome_spec = get_spec("quest", "factions/welcome_to_cantha")
    assert welcome_spec.title == "Welcome to Cantha"
    assert welcome_spec.module == "Sources.modular_recipes.quests.factions.story"
    assert welcome_spec.factory == "welcome_to_cantha"
    module = get_recipe_module("quest", "factions/welcome_to_cantha")
    assert get_recipe_factory(welcome_spec) is module.welcome_to_cantha
    assert module.welcome_to_cantha().__class__.__name__ == "BehaviorTree"
    assert recipe_route_points("quest", "factions/welcome_to_cantha")

    assert get_spec("quest", "fow/reward_time").title == "Reward Time"
    assert get_spec("quest", "FoW/reward_time").key == "fow/reward_time"
    assert get_spec("farm", "Farmer_hamnet").key == "farmer_hamnet"
    assert get_spec("mission", "nightfall/venta_cemetery").factory == "venta_cemetery"
    assert get_spec("quest", "prophecies/forgotten_wisdom").factory == "forgotten_wisdom"
    assert get_spec("quest", "prophecies/the_dukes_daughter").factory == "the_dukes_daughter"

    ascalon_spec = get_spec("mission", "prophecies/the_great_northern_wall")
    assert ascalon_spec.module == "Sources.modular_recipes.missions.prophecies.ascalon"
    ascalon_module = get_recipe_module(ascalon_spec)
    assert hasattr(ascalon_module, "the_great_northern_wall")
    assert hasattr(ascalon_module, "fort_ranik")
    desert_spec = get_spec("mission", "prophecies/dunes_of_despair")
    assert desert_spec.module == "Sources.modular_recipes.missions.prophecies.crystal_desert"
    assert get_recipe_factory(desert_spec).__name__ == "dunes_of_despair"

    prophecies_specs = build_prophecies_campaign_specs()
    assert len(prophecies_specs) == len(PROPHECIES_PHASE_SPECS)
    assert derive_prophecies_region_spans(PROPHECIES_PHASE_SPECS)
    print("modular_recipe_registry: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
