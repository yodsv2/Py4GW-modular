"""Shared helpers for prebuilt Python modular BottingTree recipes."""

from __future__ import annotations

from collections.abc import Callable
from collections.abc import Sequence

from Py4GWCoreLib.BottingTree import BottingTree
from Sources.modular_recipes.catalog import RecipeSpec
from Sources.modular_recipes.catalog import planner_steps_for_specs
from Sources.modular_recipes.catalog import specs_from_rows


def specs_from_campaign_rows(rows: Sequence[tuple[str, str, str, str]]) -> list[RecipeSpec]:
    return specs_from_rows(rows)


def create_modular_botting_tree(
    *,
    name: str,
    specs: Sequence[RecipeSpec],
    start_index: int = 0,
    loop: bool = False,
    debug_hook: Callable[[str], None] | None = None,
) -> BottingTree:
    planner_steps = planner_steps_for_specs(list(specs), start_index=max(0, int(start_index)), debug_hook=debug_hook)
    botting_tree = BottingTree(bot_name=name, pause_on_combat=False, isolation_enabled=False)
    botting_tree.SetCurrentNamedPlannerSteps(planner_steps, name=name, auto_start=False, reset=True, repeat=bool(loop))
    return botting_tree
